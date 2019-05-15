import requests
import json
import traceback
import logging

module_logger = logging.getLogger('Winzog.Sumologic')

class Sumologic:
    def __init__(self, configuration_properties):
        self.logger = logging.getLogger('Winzog.Sumologic.Sumologic')
        sumo_logic_url, meta = configuration_properties['sumo_logic_url']
        self.sumo_logic_url = sumo_logic_url.strip()

    def log(self, data):
        try:
            self.logger.debug('logging to sumo {}'.format(data))
            self.logger.debug('logging to sumo #{}# url'.format(self.sumo_logic_url))
            result = requests.post(url=self.sumo_logic_url,
                                   data=json.dumps(data),
                                   headers={'content-type': 'application/json'})
            self.logger.debug('post to sumo response {}'.format(result))
        except:
            traceback.print_exc()
            error_string = traceback.format_exc()
            self.logger.debug('An error occurred while logging to sumo logic {}'.format(error_string))
