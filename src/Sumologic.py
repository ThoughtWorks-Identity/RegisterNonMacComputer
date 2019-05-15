import requests
import json
import traceback


class Sumologic:
    def __init__(self, configuration_properties):
        sumo_logic_url, meta = configuration_properties['sumo_logic_url']
        self.sumo_logic_url = sumo_logic_url.strip()

    def log(self, data):
        try:
            print('logging to sumo', data)
            print('logging to sumo #{}# url'.format(self.sumo_logic_url))
            result = requests.post(url=self.sumo_logic_url,
                                   data=json.dumps(data),
                                   headers={'content-type': 'application/json'})
            print('post to sumo response', result)
        except:
            traceback.print_exc()
            print('An error occurred while logging to sumo logic')
