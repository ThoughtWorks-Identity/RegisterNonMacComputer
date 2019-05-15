import os
import sys
import traceback
import urllib.parse
import webbrowser

from jproperties import Properties

import Computer
from Sumologic import Sumologic


def load_configuration_properties():
    configuration_properties = Properties()
    if getattr(sys, 'frozen', False):
        bundle_dir = sys._MEIPASS
    else:
        # we are running in a normal Python environment
        bundle_dir = os.path.dirname(os.path.abspath(__file__))

    with open(bundle_dir + '/configuration.properties', 'rb') as config_props_file:
        configuration_properties.load(config_props_file, "utf-8")

    return configuration_properties


def open_browser_for_registration(configuration_properties, data):
    registration_url, meta = configuration_properties['registration_url']
    winzog_url = "{}{}".format(registration_url.strip(), urllib.parse.urlencode(data).strip())

    print(winzog_url)
    webbrowser.open_new_tab(winzog_url)


def main():
    configuration_properties = load_configuration_properties()
    sumologic = Sumologic(configuration_properties)
    try:
        data = Computer.get_data()
        sumologic.log(data)
        open_browser_for_registration(configuration_properties, data['device_data'])
    except:
        error_string = traceback.format_exc()
        sumologic.log({'error': error_string})


if __name__ == '__main__':
    main()
    