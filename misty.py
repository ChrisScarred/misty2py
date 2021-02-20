import requests


class Misty:
    def __init__(self, IP: str):
        self.ip = IP

    def action(self, endpoint: str, data: dict) -> dict:
        r = requests.post('http://%s/%s' % (self.ip, endpoint), json = data)
        return r.json()

    def information(self, endpoint: str) -> dict:
        r = requests.get('http://%s/%s' % (self.ip, endpoint))
        return r.json()
