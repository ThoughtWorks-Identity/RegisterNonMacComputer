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


def is_error(model):
    return model is None or model.strip() == '' or model.strip().lower() == 'not specified'


def get_model(sumologic, serial):
    model = get_from_wmic('model', 'computersystem')
    if is_error(model):
        sumologic.log({'message': {
            'type': 'warning', 
            'text': 'Model for serial number {} from wmic computersystem get model returned "{}"'.format(serial, model)
        }})
        model = get_from_wmic('name', 'csproduct')
        if is_error(model):
            sumologic.log({'message': {
                'type': 'error', 
                'text': 'Model for serial number {} from wmic csproduct get name returned "{}".'.format(serial, model) \
                    + 'Could not determine model of laptop'
            }})
    return model        
        

def get_device_data(sumologic):
    serial = get_from_wmic('serialnumber', 'bios')
    return {
        'serial': serial,
        'non_mac': "true",
        'manufacturer': get_from_wmic('manufacturer', 'computersystem'),
        'model': get_model(sumologic, serial),
        'wifi_mac': getmac.get_mac_address()
    }


def get_bit_locker_status():
    return check_service('BDESVC')


def get_data(sumologic):
    return {
        "device_data": get_device_data(sumologic),
        "sophos": get_sophos_status(),
        "bitlocker": get_bit_locker_status(),
        "os_version": get_windows_os_version(),
    }
