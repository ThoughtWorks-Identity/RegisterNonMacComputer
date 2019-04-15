import wmi
# wmi also requires a pip install pypiwin32
import json
import getmac
import requests

for config in wmi.WMI().Win32_ComputerSystemProduct():
    data = {'serial_number': config.IdentifyingNumber, 'laptop_vendor': config.Vendor, 'laptop_type': config.Name}

print(getmac.get_mac_address())
print(data)
