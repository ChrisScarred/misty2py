import requests
import json


ACTIONS_JSON = "misty/allowed_actions.json"
DATA_JSON = "misty/allowed_data.json"

class Post():
    def __init__(self, ip, allowed_actions_file = ACTIONS_JSON, allowed_data_file = DATA_JSON) -> None:
        self.ip = ip

        f = open(allowed_actions_file)
        self.allowed_actions = json.loads(f.read())
        f.close()

        f = open(allowed_data_file)
        self.allowed_data = json.loads(f.read())
        f.close()

    def perform_action(self, endpoint : str, data: dict) -> bool:
        r = requests.post('http://%s/%s' % (self.ip, endpoint), json = data)
        dct = r.json()
        return dct["status"] == "Success"

class Action(Post):
    def perform_action(self, action_name: str, string : str, dct : dict, method : str) -> bool:
        r = False
        if action_name in self.allowed_actions.keys():
            if method == "dict":
                r = super().perform_action(self.allowed_actions[action_name], dct)
            elif method == "string" and string in self.allowed_data:
                r = super().perform_action(self.allowed_actions[action_name], self.allowed_data[string])
        return r