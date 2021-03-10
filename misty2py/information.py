"""This script implements the information keywords matching to Misty's API endpoints and sending information requests.
"""
import requests
import json
from os import path
from urllib.parse import urlencode

this_directory = path.abspath(path.dirname(__file__))
INFOS_JSON = str(path.join(this_directory, "allowed_infos.json"))

class Get():
    """A class representing the GET url request method.

    Attributes:
        ip (str): The IP address where the requests are sent
        allowed_infos (dict): The dictionary of information keywords matching to the Misty's API endpoints.
    """

    def __init__(self, ip : str, custom_allowed_infos = {}) -> None:
        """Initialises a Get object.

        Args:
            ip (str): The IP address where the requests are sent.
            custom_allowed_infos (dict, optional): The dictionary of custom information keywords. Defaults to {}.
        """

        self.ip = ip

        allowed_infos = custom_allowed_infos
        f = open(INFOS_JSON)
        allowed_infos.update(json.loads(f.read()))
        f.close()

        self.allowed_infos = allowed_infos
    
    def get_info(self, endpoint : str) -> dict:
        """Sends a GET request.

        Args:
            endpoint (str): The API endpoint to which the request is sent.

        Returns:
            dict: The request response.
        """

        r = requests.get('http://%s/%s' % (self.ip, endpoint))
        try:
            return r.json()
        except:
            return {'status' : 'Success', 'content' : r.content}


class Info(Get):
    """A class representing an information request from Misty. A subclass of Get().
    """

    def get_info(self, info_name: str, params: dict = {}) -> dict:
        """Sends an information request to Misty.

        Args:
            info_name (str): The information keyword specifying which information is requested.
            params (dict): dict of parameter name and parameter value. Defaults to {}.

        Returns:
            dict: Misty's response.
        """
        
        if not info_name in self.allowed_infos.keys():
            r = {"status" : "Failed", "message" : "Command `%s` not supported." % info_name}
        else:
            endpoint = self.allowed_infos[info_name]

            if len(params) > 0:
                endpoint += "?"
                query_string = urlencode(params)
                endpoint += query_string
            try:
                r = super().get_info(endpoint)
            except:
                r = {"status" : "Failed", "message" : "Unknown error - perhaps your Misty edition does not support this endpoint?"}
        return r