import requests
import json


INFOS_JSON = "misty/allowed_infos.json"

class Get():
    def __init__(self, ip, allowed_infos_file = INFOS_JSON) -> None:
        self.ip = ip
        f = open(allowed_infos_file)
        self.allowed_infos = json.loads(f.read())
    
    def get_info(self, endpoint : str) -> dict:
        r = requests.get('http://%s/%s' % (self.ip, endpoint))
        return r.json()

class Info(Get):
    def get_info(self, info_name: str) -> dict:
        if not info_name in self.allowed_infos.keys():
            r = {"result" : "Fail"}
        else:
            r = super().get_info(self.allowed_infos[info_name])
        return r