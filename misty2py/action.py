"""This script implements the action keywords matching to Misty's API endpoints, sending action requests and data shortcuts.
"""
import requests
import json
from os import path


this_directory = path.abspath(path.dirname(__file__))
ACTIONS_JSON = str(path.join(this_directory, "allowed_actions.json"))
DATA_JSON = str(path.join(this_directory, "allowed_data.json"))

class Post():
    """A class representing the POST url request method.

    Attributes
    ----------
    ip : str
        The IP address where the requests are sent
    allowed_actions : dict
        The dictionary of custom action keywords matching to the Misty's API endpoints.
    allowed_data : dict
        The dictionary of custom data shortcuts matching to the json dictionaries required my Misty's API.
    """

    def __init__(self, ip : str, custom_allowed_actions = {}, custom_allowed_data = {}) -> None:
        """Initialises a Post object.

        Parameters
        ----------
        ip : str
            The IP address where the requests are sent
        custom_allowed_actions : str, optional
            The dictionary of action keywords, by default {}
        custom_allowed_data : str, optional
            The dictionary of data shortcuts, by default {}
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

    def perform_action(self, endpoint : str, data: dict, request_method: str = "post") -> bool:
        """Sends a POST request.

        Parameters
        ----------
        endpoint : str
            The API endpoint to which the request is sent.
        data : dict
            The json data supplied in the body of the request.

        Returns
        -------
        bool
            Whether or not the request was successful.
        """
        if request_method=="post":
            r = requests.post('http://%s/%s' % (self.ip, endpoint), json = data)
            dct = r.json()
            return dct["status"] == "Success"


class Action(Post):
    """A class representing an action request for Misty. A subclass of Post().
    """

    def perform_action(self, action_name: str, string : str, dct : dict, data_method : str) -> bool:
        """Sends an action request to Misty.

        Parameters
        ----------
        action_name : str
            The action keyword specifying which action is requested.
        string : str
            The data shortcut representing the data supplied in the body of the request.
        dct : dict
            The json dictionary to be supplied in the body of the request.
        method : str
            "dict" if the data is supplied as a json dictionary, "string" if the data is supplied as a data shortcut.

        Returns
        -------
        bool
            Whether or not the action request was successful.
        """

        r = False
        if action_name in self.allowed_actions.keys():
            if data_method == "dict":
                r = super().perform_action(self.allowed_actions[action_name]["endpoint"], dct, request_method=self.allowed_actions[action_name]["method"])
            elif data_method == "string" and string in self.allowed_data:
                r = super().perform_action(self.allowed_actions[action_name]["endpoint"], self.allowed_data[string], request_method=self.allowed_actions[action_name]["method"])
        return r