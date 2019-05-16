import subprocess
import getmac
import platform


def get_from_dmidecode(key):
    command = ['dmidecode', '-s', key]
    return subprocess.check_output(command)

def get_device_data():
     return {
        'serial': get_from_dmidecode('system-serial-number'),
        'non_mac': "true",
        'manufacturer': get_from_dmidecode('system-manufacturer'),
        'model': get_from_dmidecode('system-product-name'),
        'wifi_mac': getmac.get_mac_address()
    }

def get_data():
    return {
        "device_data": get_device_data(),
        "os_version": platform.platform(),
    }
