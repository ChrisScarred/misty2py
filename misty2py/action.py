"""This script implements the action keywords matching to Misty's API endpoints, sending action requests and data shortcuts.
"""
from typing import Dict, Union
import requests
import json
from os import path
import sys

from misty2py.utils import construct_transition_dict

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

    def __init__(self, ip : str, custom_allowed_actions: Dict = {}, custom_allowed_data: Dict = {}) -> None:
        """Initialises a Post object.

        Args:
            ip (str): The IP address where the requests are sent.
            custom_allowed_actions (Dict, optional): The dictionary of action keywords. Defaults to {}.
            custom_allowed_data (Dict, optional): The dictionary of data shortcuts. Defaults to {}.
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

    def perform_action(self, endpoint : str, data: Dict, request_method: str = "post") -> Dict:
        """Sends a POST request.

        Args:
            endpoint (str): The API endpoint to which the request is sent.
            data (Dict): The json data supplied in the body of the request.
            request_method (str, optional): The request method. Defaults to "post".

        Returns:
            Dict: The API response.
        """

        if request_method=="post":
            response = requests.post('http://%s/%s' % (self.ip, endpoint), json = data)
        else:
            response = requests.delete('http://%s/%s' % (self.ip, endpoint), json = data)
        try:
            return response.json()
        except:
            return {'status' : 'Success', 'content' : response.content}
        

class Action(Post):
    """A class representing an action request for Misty. A subclass of Post().
    """

    def perform_action(self, action_name: str, data: Union[str, Dict], data_method: str) -> Dict:
        """Sends an action request to Misty.

        Args:
            action_name (str): The action keyword specifying which action is requested.
            data (Union[str, Dict]): The data shortcut representing the data supplied in the body of the request or the json dictionary to be supplied in the body of the request.
            data_method (str): "dict" if the data is supplied as a json dictionary, "string" if the data is supplied as a data shortcut.

        Returns:
            Dict: the response from the API.
        """

        if not action_name in self.allowed_actions.keys():
            return {
                "status" : "Failed", 
                "message" : "Command `%s` not supported." % action_name
            }

        else:
            if data_method == "dict":
                try:
                    return super().perform_action(
                        self.allowed_actions[action_name]["endpoint"], 
                        data, 
                        request_method=self.allowed_actions[action_name]["method"]
                    )

                except:
                    return {
                        "status" : "Failed",
                        "message" : "Error: %s." %  sys.exc_info()[1]
                    }

            elif data_method == "string" and data in self.allowed_data:
                try:
                    return super().perform_action(
                        self.allowed_actions[action_name]["endpoint"], 
                        self.allowed_data[data], 
                        request_method=self.allowed_actions[action_name]["method"]
                    )

                except:
                    return {
                        "status" : "Failed", 
                        "message" : "Error: %s." %  sys.exc_info()[1]
                    }

            else:
                return {
                    "status" : "Failed", 
                    "message" : "Data shortcut `%s` not supported." % data
                }
        
    def action_handler(self, action_name: str, data: Union[Dict, str]) -> Dict:
        """Sends Misty a request to perform an action.

        Args:
            action_name (str): The keyword specifying the action to perform.
            data (Union[Dict, str]): The data to send in the request body in the form of a data shortcut or a json dictionary.

        Returns:
            Dict: response from the API
        """
        
        if action_name == "led_trans" and isinstance(data, Dict) and len(data) >= 2 and len(data) <= 4:
            
            try:
                data = construct_transition_dict(data, self.allowed_data)

            except ValueError as e:
                return {
                    "status" : "Failed", 
                    "message" : "The data is not in correct format.", 
                    "details": e
                }

        data_method = ""

        if isinstance(data, Dict):
            data_method = "dict"

        else:
            data_method = "string"
        
        return self.perform_action(action_name, data, data_method)
