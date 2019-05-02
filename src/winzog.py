import wmi
# wmi also requires a pip install pypiwin32
import json
import getmac
import requests
import webbrowser
import os
from urllib.parse import quote
import sys

# This should suffice for now. When we have more variables consider using the
# ConfigParser module
def getBaseUrl():
    if getattr(sys, 'frozen', False):
        bundle_dir = sys._MEIPASS
    else:
        # we are running in a normal Python environment
        bundle_dir = os.path.dirname(os.path.abspath(__file__))

    with open(bundle_dir+'/registrationWebAppUrl.txt', 'r') as registrationWebAppUrlFile:
        base_url = registrationWebAppUrlFile.read()

    print(base_url)
    return base_url
    
base_url = getBaseUrl()

for config in wmi.WMI().Win32_ComputerSystemProduct():
    data = {'serial_number': config.IdentifyingNumber, 'laptop_vendor': config.Vendor, 'laptop_type': config.Name}

    try:
        serial = config.IdentifyingNumber
        model = config.Vendor + " " + config.Name
    except:
        print("Something went wrong!")

for k,v in data.items():
    data[k] = quote(v)

mac = getmac.get_mac_address()

print(getmac.get_mac_address())
print(data)

print(serial)
print(model)

winzog_url = base_url + "serial={0}&model={1}".format(serial, model)

print(winzog_url)
webbrowser.open_new_tab(winzog_url)
