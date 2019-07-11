import subprocess
import getmac
import platform


def get_from_dmidecode(key):
    return execute_command(['sudo', 'dmidecode', '-s', key])


def execute_command(command):
    output = subprocess.check_output(command).decode('UTF-8')
    return output.strip()


def is_error(model):
    return model is None or model.strip() == '' or model.strip().lower() == 'not specified'


def get_model(sumologic, serial):
    model = execute_command(['cat', '/sys/devices/virtual/dmi/id/product_name'])
    if is_error(model):
        sumologic.log({'message': {
            'type': 'warning',
            'text': 'Model for serial number {} from '
                    'cat /sys/devices/virtual/dmi/id/product_name returned "{}".'
                    .format(serial, model)
        }})
        model = get_from_dmidecode('system-version')
        if is_error(model):
            sumologic.log({'message': {
                'type': 'warning',
                'text': 'Model for serial number {} from '
                        'sudo dmidecode -s system-version returned "{}".'
                        .format(serial, model)
            }})
            model = get_from_dmidecode('system-product-name')
            if is_error(model):
                sumologic.log({'message': {
                    'type': 'error',
                    'text': 'Model for serial number {} from '
                            'sudo dmidecode -s system-product-name returned "{}".'
                            .format(serial, model)
                }})
                raise Exception("Unable to find model for this computer. Please report the issue to MDM - Techops")
    return model


def get_device_data(sumologic):
    serial = get_from_dmidecode('system-serial-number')
    return {
        'serial': serial,
        'non_mac': "true",
        'manufacturer': get_from_dmidecode('system-manufacturer'),
        'model': get_model(sumologic, serial),
        'wifi_mac': getmac.get_mac_address()
    }


def get_data(sumologic):
    return {
        "device_data": get_device_data(sumologic),
        "os_version": platform.platform(),
    }
