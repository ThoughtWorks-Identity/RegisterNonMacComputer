import wmi
# wmi also requires a pip install pypiwin32
import getmac
from pathlib import Path
import platform
import re
from subprocess import check_output, CalledProcessError


def is_service_running(sc_query_output):
    return bool(re.search(r'\s*?STATE\s*?:\s*?4\s*?RUNNING', sc_query_output))


def check_service(query):
    try:
        sc_query_output = check_output(query).decode('utf-8')
        return {
            "is_installed": "true",
            "is_running": "true" if is_service_running(sc_query_output) else "false"
        }
    except CalledProcessError:
        return {
            "is_installed": "false",
            "is_running": "false"
        }

def get_sophos_status():
    return check_service('sc query SAVService')

def get_windows_os_version():
    return platform.platform()

def get_device_data():
    config = wmi.WMI().Win32_ComputerSystemProduct()[0]
    return {
        'serial': config.IdentifyingNumber,
        'non_mac': "true",
        'manufacturer': config.Vendor,
        'model': config.Name,
        'wifi_mac': getmac.get_mac_address()
    }

def get_bit_locker_status(): 
    return check_service('sc query BDESVC')
    

def get_data():
    
    return {
        "device_data": get_device_data(),
        "sophos": get_sophos_status(),
        "bitlocker": get_bit_locker_status(),
        "windows_version": get_windows_os_version(),
    }
  
