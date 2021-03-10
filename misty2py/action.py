"""This script implements the action keywords matching to Misty's API endpoints, sending action requests and data shortcuts.
"""
import requests
import json
from os import path
import sys

this_directory = path.abspath(path.dirname(__file__))
ACTIONS_JSON = str(path.join(this_directory, "allowed_actions.json"))
DATA_JSON = str(path.join(this_directory, "allowed_data.json"))

class Post():
    """A class representing the POST url request method.

    Attributes:
        ip (str): The IP address where the requests are sent.
        allowed_actions (dict): The dictionary of custom action keywords matching to the Misty's API endpoints.
        allowed_data (dict): The dictionary of custom data shortcuts matching to the json dictionaries required my Misty's API.
    """

    def __init__(self, ip : str, custom_allowed_actions = {}, custom_allowed_data = {}) -> None:
        """Initialises a Post object.

        Args:
            ip (str): The IP address where the requests are sent.
            custom_allowed_actions (dict, optional): The dictionary of action keywords. Defaults to {}.
            custom_allowed_data (dict, optional): The dictionary of data shortcuts. Defaults to {}.
        """

        self.ip = ip

        allowed_actions = custom_allowed_actions
        f = open(ACTIONS_JSON)
        allowed_actions.update(json.loads(f.read()))
        f.close()
        self.allowed_actions = allowed_actions

        allowed_data = custom_allowed_data
        f = open(DATA_JSON)
        allowed_data.update(json.loads(f.read()))
        f.close()
        self.allowed_data = allowed_data

    def perform_action(self, endpoint : str, data: dict, request_method: str = "post") -> dict:
        """Sends a POST request.

        Args:
            endpoint (str): The API endpoint to which the request is sent.
            data (dict): The json data supplied in the body of the request.
            request_method (str, optional): The request method. Defaults to "post".

        Returns:
            dict: The API response.
        """

        if request_method=="post":
            r = requests.post('http://%s/%s' % (self.ip, endpoint), json = data)
        else:
            r = requests.delete('http://%s/%s' % (self.ip, endpoint), json = data)
        try:
            return r.json()
        except:
            return {'status' : 'Success', 'content' : r.content}
        

class Action(Post):
    """A class representing an action request for Misty. A subclass of Post().
    """

    def perform_action(self, action_name: str, data, data_method : str) -> dict:
        """Sends an action request to Misty.

        Args:
            action_name (str): The action keyword specifying which action is requested.
            data (string or dict): The data shortcut representing the data supplied in the body of the request or the json dictionary to be supplied in the body of the request.
            data_method (str): "dict" if the data is supplied as a json dictionary, "string" if the data is supplied as a data shortcut.

        Returns:
            dict: the response from the API.
        """

        if not action_name in self.allowed_actions.keys():
            return {"status" : "Failed", "message" : "Command `%s` not supported." % action_name}
        else:
            if data_method == "dict":
                try:
                    return super().perform_action(self.allowed_actions[action_name]["endpoint"], data, request_method=self.allowed_actions[action_name]["method"])
                except:
                    return {"status" : "Failed", "message" : "Error: %s." %  sys.exc_info()[1]}
            elif data_method == "string" and data in self.allowed_data:
                try:
                    return super().perform_action(self.allowed_actions[action_name]["endpoint"], self.allowed_data[data], request_method=self.allowed_actions[action_name]["method"])
                except:
                    return {"status" : "Failed", "message" : "Error: %s." %  sys.exc_info()[1]}
            else:
                return {"status" : "Failed", "message" : "Data shortcut `%s` not supported." % data}
        