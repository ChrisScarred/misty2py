import requests


class Post():
    def __init__(self, ip) -> None:
        self.ip = ip
    
    def perform_action(self, endpoint : str, data: dict) -> bool:
        r = requests.post('http://%s/%s' % (self.ip, endpoint), json = data)
        dct = r.json()
        return dct["status"] == "Success"

class Action(Post):
    pass