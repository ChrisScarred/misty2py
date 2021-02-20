import requests


class Get():
    def __init__(self, ip) -> None:
        self.ip = ip
    
    def get_info(self, endpoint : str) -> dict:
        r = requests.get('http://%s/%s' % (self.ip, endpoint))
        return r.json()

class Info(Get):
    pass