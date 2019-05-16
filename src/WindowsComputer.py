import wmi
import getmac
import platform


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
    return check_service('BDESVC')


def get_data():
    return {
        "device_data": get_device_data(),
        "sophos": get_sophos_status(),
        "bitlocker": get_bit_locker_status(),
        "os_version": get_windows_os_version(),
    }
