"""This script implements the information keywords matching to Misty's API endpoints and sending information requests.
"""
import requests
import json
from os import path


this_directory = path.abspath(path.dirname(__file__))
INFOS_JSON = str(path.join(this_directory, "allowed_infos.json"))

class Get():
    """A class representing the GET url request method.

    Attributes
    ----------
    ip : str
        The IP address where the requests are sent
    allowed_infos : dict
        The dictionary of information keywords matching to the Misty's API endpoints.
    """

    def __init__(self, ip : str, allowed_infos_file = INFOS_JSON) -> None:
        """Initialises a Get object.

        Parameters
        ----------
        ip : str
            The IP address where the requests are sent
        allowed_infos_file : str, optional
            The name of the file containing the dictionary of information keywords, by default INFOS_JSON
        """
        self.ip = ip

        allowed_infos = {}
        f = open(allowed_infos_file)
        allowed_infos.update(json.loads(f.read()))
        f.close()

        if INFOS_JSON != allowed_infos_file:
            f = open(INFOS_JSON)
            allowed_infos.update(json.loads(f.read()))
            f.close()

        self.allowed_infos = allowed_infos
    
    def get_info(self, endpoint : str) -> dict:
        """Sends a GET request.

        Parameters
        ----------
        endpoint : str
            The API endpoint to which the request is sent.

        Returns
        -------
        dict
            The request response.
        """
        r = requests.get('http://%s/%s' % (self.ip, endpoint))
        return r.json()


class Info(Get):
    """A class representing an information request from Misty. A subclass of Get().
    """

    def get_info(self, info_name: str) -> dict:
        """Sends an information request to Misty.

        Parameters
        ----------
        info_name : str
            The information keyword specifying which information is requested.

        Returns
        -------
        dict
            Misty's response.
        """
        
        if not info_name in self.allowed_infos.keys():
            r = {"result" : "Fail"}
        else:
            r = super().get_info(self.allowed_infos[info_name])
        return r