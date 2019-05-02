import wmi
# wmi also requires a pip install pypiwin32
import getmac
import webbrowser
import os
import sys
import urllib.parse


# This should suffice for now. When we have more variables consider using the
# ConfigParser module
def getBaseUrl():
    if getattr(sys, 'frozen', False):
        bundle_dir = sys._MEIPASS
    else:
        # we are running in a normal Python environment
        bundle_dir = os.path.dirname(os.path.abspath(__file__))

    with open(bundle_dir + '/registrationWebAppUrl.txt', 'r') as registrationWebAppUrlFile:
        base_url = registrationWebAppUrlFile.read()

    print(base_url)
    return base_url.strip()


base_url = getBaseUrl()
config = wmi.WMI().Win32_ComputerSystemProduct()[0]

data = {
    'serial_number': config.IdentifyingNumber,
    'laptop_vendor': config.Vendor,
    'laptop_type': config.Name,
    'mac': getmac.get_mac_address()
}

print(data)

winzog_url = base_url + urllib.parse.urlencode(data)

print(winzog_url)
webbrowser.open_new_tab(winzog_url)
