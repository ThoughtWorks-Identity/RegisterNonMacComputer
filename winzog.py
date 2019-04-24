import wmi
# wmi also requires a pip install pypiwin32
import json
import getmac
import requests
import webbrowser
import os

base_url = os.environ.get('Winzog_URL')

print(base_url)

for config in wmi.WMI().Win32_ComputerSystemProduct():
    data = {'serial_number': config.IdentifyingNumber, 'laptop_vendor': config.Vendor, 'laptop_type': config.Name}

    try:
        serial = config.IdentifyingNumber
        model = config.Vendor + " " + config.Name
    except:
        print("Something went wrong!")

mac = getmac.get_mac_address()

print(getmac.get_mac_address())
print(data)

print(serial)
print(model)

winzog_url = base_url + "serial={0}&model={1}".format(serial, model)

print(winzog_url)
webbrowser.open_new_tab(winzog_url)