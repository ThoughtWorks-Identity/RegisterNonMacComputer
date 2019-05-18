import wmi
import getmac
import platform
import subprocess
import logging

logger = logging.getLogger('Winzog.WindowsComputer')

def check_service(service_name):
    c = wmi.WMI()
    service_list = c.Win32_Service(Name=service_name)
    if len(service_list) > 0:
        service = service_list[0]
        return {
            "is_installed": "true",
            "is_running": "true" if service.state == 'Running' else "false"
        }
    else:
        return {
            "is_installed": "false",
            "is_running": "false"
        }


def get_sophos_status():
    return check_service('SAVService')


def get_windows_os_version():
    return platform.platform()

def get_from_wmic(key, from_where):
    command = ['wmic',from_where, 'get', key]
    output = subprocess.check_output(command).decode('UTF-8')
    logger.debug('==================>')
    logger.debug(output)
    logger.debug('==================>')
    lines = output.splitlines()
    logger.debug(lines)
    if(len(lines) >= 2):
        return lines[2].strip()
    
    raise RuntimeError("Unable to get wmic {} get {} - got output {}".format(from_where, key, output))

def get_device_data():
    return {
        'serial': get_from_wmic('serialnumber', 'bios'),
        'non_mac': "true",
        'manufacturer': get_from_wmic('manufacturer', 'computersystem'),
        'model': get_from_wmic('model', 'computersystem'),
        'wifi_mac': getmac.get_mac_address()
    }


def get_bit_locker_status():
    return check_service('BDESVC')


def get_data():
    return {
        "device_data": get_device_data(),
        "sophos": get_sophos_status(),
        "bitlocker": get_bit_locker_status(),
        "os_version": get_windows_os_version(),
    }
