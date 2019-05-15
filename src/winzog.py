import os
import sys
import traceback
import urllib.parse
import webbrowser

from jproperties import Properties

import Computer
from Sumologic import Sumologic
from configure_logger import configure_logger


class Winzog: 

    def main(self):
        self.logger = configure_logger()
        self.configuration_properties = self.load_configuration_properties()
        sumologic = Sumologic(self.configuration_properties)
        try:
            self.logger.debug('Getting computer data')
            data = Computer.get_data()
            sumologic.log(data)
            self.open_browser_for_registration(data['device_data'])
        except:
            error_string = traceback.format_exc()
            sumologic.log({'error': error_string})
    

    def load_configuration_properties(self):
        self.logger.debug('Loading configuration proeprties')
        configuration_properties = Properties()
        if getattr(sys, 'frozen', False):
            bundle_dir = sys._MEIPASS
        else:
            # we are running in a normal Python environment
            bundle_dir = os.path.dirname(os.path.abspath(__file__))

        with open(bundle_dir + '/configuration.properties', 'rb') as config_props_file:
            configuration_properties.load(config_props_file, "utf-8")

        return configuration_properties


    def open_browser_for_registration(self, data):
        registration_url, meta = self.configuration_properties['registration_url']
        winzog_url = "{}{}".format(registration_url.strip(), urllib.parse.urlencode(data).strip())

        self.logger.info(winzog_url)
        webbrowser.open_new_tab(winzog_url)
    



if __name__ == '__main__':
    Winzog().main()
    