import subprocess
import getmac
import platform


def get_from_dmidecode(key):
    command = ['sudo', 'dmidecode', '-s', key]
    output = subprocess.check_output(command).decode('UTF-8')
    return output.strip()


def get_model():
    model = get_from_dmidecode('system-version')
    if not model.strip():
        model = get_from_dmidecode('system-product-name')
    if not model.strip():
        raise Exception("Unable to find model for this computer. Please report the issue to MDM - Techops")
    return model.strip()


def get_device_data():
    return {
        'serial': get_from_dmidecode('system-serial-number'),
        'non_mac': "true",
        'manufacturer': get_from_dmidecode('system-manufacturer'),
        'model': get_model(),
        'wifi_mac': getmac.get_mac_address()
    }


def get_data():
    return {
        "device_data": get_device_data(),
        "os_version": platform.platform(),
    }
