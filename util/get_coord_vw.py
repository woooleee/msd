import requests
import yaml

class GeoCoderVworld:
    def __init__(self):
        self.cfg_path = '../security/security.yaml'
        with open(self.cfg_path, 'r') as stream:
            data_loaded = yaml.safe_load(stream)
        self.api_url = data_loaded['VWorldKr']['GeoCoderApi']['endpoint']
        self.api_key = data_loaded['VWorldKr']['key']

    def AddrToCoord(self, addr:str):
        '''
        Return the coordinates tuple of given full address
        :param full_addr(str): full road address ex. '부산광역시 부산진구 범천동 862-1'
        :return x, y: coordinates
        '''

        params = {
            "service": "address",
            "request": "getcoord",
            "crs": "epsg:4326",
            "address": addr,
            "format": "json",
            "type": "road",
            "key": self.api_key
        }

        response = requests.get(self.api_url, params=params)
        if response.status_code == 200:
            response_body = response.json()
            try:
                x = response_body['response']['result']['point']['x']
                y = response_body['response']['result']['point']['y']
                return x, y
            except:
                return 0, 0

        else:
            return 0, 0
