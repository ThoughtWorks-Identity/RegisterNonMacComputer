import wmi
# wmi also requires a pip install pypiwin32
import getmac
import webbrowser
import os
import sys
import urllib.parse
import requests
from jproperties import Properties
import json
import traceback


configuration_properties = Properties()


def load_configuration_properties():
    if getattr(sys, 'frozen', False):
        bundle_dir = sys._MEIPASS
    else:
        # we are running in a normal Python environment
        bundle_dir = os.path.dirname(os.path.abspath(__file__))

    with open(bundle_dir + '/configuration.properties', 'rb') as config_props_file:
        configuration_properties.load(config_props_file, "utf-8")
    

def get_data_from_computer():
    config = wmi.WMI().Win32_ComputerSystemProduct()[0]

    data = {
        'serial': config.IdentifyingNumber,
        'non_mac': "true",
        'manufacturer': config.Vendor,
        'model': config.Name,
        'wifi_mac': getmac.get_mac_address()
    }
    print('The data retreived from computer', data)
    return data


def log_to_sumologic(data):
    try:
        print('logging to sumo', data)
        sumo_logic_url, meta = configuration_properties['sumo_logic_url']
        print('logging to sumo #{}# url'.format(sumo_logic_url.strip()))
        result = requests.post(url=sumo_logic_url.strip(),
                    data=json.dumps(data),
                    headers={'content-type': 'application/json'})
        print('post to sumo response', result)            
    except:
        traceback.print_exc()
        print('An error occurred while logging to sumo logic')                


def open_browser_for_registration(data):
    registration_url, meta = configuration_properties['registration_url']
    winzog_url = "{}{}".format(registration_url.strip(), urllib.parse.urlencode(data).strip()) 

    print(winzog_url)
    webbrowser.open_new_tab(winzog_url)

try:
    load_configuration_properties()
    data = get_data_from_computer()
    log_to_sumologic(data)
    open_browser_for_registration(data)
except:
    error_string = traceback.format_exc()
    log_to_sumologic({ 'error': error_string })


