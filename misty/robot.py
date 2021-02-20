import requests


class Misty:
    def __init__(self, ip: str):
        self.ip = ip

    def __str__(self) -> str:
        return "A Misty II robot with IP address %s" % self.ip

    def action(self, endpoint: str, data: dict) -> dict:
        r = requests.post('http://%s/%s' % (self.ip, endpoint), json = data)
        return r.json()

    def information(self, endpoint: str) -> dict:
        r = requests.get('http://%s/%s' % (self.ip, endpoint))
        return r.json()
