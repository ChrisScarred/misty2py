"""The main script for the misty2py package.
"""
from misty2py.information import *
from misty2py.action import *
from misty2py.utils import *
from misty2py.socket import *


class Misty:
    """A class representing a Misty robot.

    Attributes
    ----------
    ip : str
        The IP address of this Misty robot.
    infos : Info()
        The object of Info class that belongs to this Misty.
    actions : Action()
        The object of Action class that belongs to this Misty.
    websockets : dict
        A dictionary of active websocket subscriptions (keys being the event name, values the Socket() object).
    """

    def __init__(self, ip: str, custom_info={}, custom_actions={}, custom_data={}) -> None:
        """Initialises an instance of a Misty robot.

        Parameters
        ----------
        ip : str
            The IP address of this Misty robot.
        custom_info : dict, optional
            Custom information keywords in the form of dictionary with key being the keyword and value being the API endpoint, by default {}
        custom_actions : dict, optional
            Custom actions keywords in the form of dictionary with key being the keyword and value being the API endpoint, by default {}
        custom_data : dict, optional
            Custom data shortcuts in the form of dictionary with key being the shortcut and value being the json data in the form of a dictionary, by default {}
        """
        self.ip = ip
        self.infos = Info(ip, custom_allowed_infos=custom_info)
        self.actions = Action(ip, custom_allowed_actions=custom_actions, custom_allowed_data=custom_data)
        self.websockets = {}

    def __str__(self) -> str:
        """Transforms a Misty() object into a string.

        Returns
        -------
        str
            A string identifiyng this Misty robot.
        """
        return "A Misty II robot with IP address %s" % self.ip

    def perform_action(self, action_name: str, data = {}) -> bool:
        """Sends Misty a request to perform an action.

        Parameters
        ----------
        action_name : str
            The keyword specifying the action to perform.
        data : str or dict, optional
            The data to send in the request body in the form of a data shortcut or a json dictionary, by default {}

        Returns
        -------
        dict
            response from the API
        """
        if action_name == "led_trans" and isinstance(data, dict) and len(data)>=2 and len(data)<=4:
            try:
                data = construct_transition_dict(data, self.actions.allowed_data)
            except:
                return {"result" : "Failed", "message" : "Data not in correct format."}

        data_method = ""
        if isinstance(data, dict):
            data_method = "dict"
        else:
            data_method = "string"
        r = self.actions.perform_action(action_name, data, data_method)
        return r

    def get_info(self, info_name: str, params: dict = {}) -> dict:
        """Obtains information from Misty.

        Args:
            info_name (str): The information keyword specifying which kind of information to retrieve.
            params (dict): dict of parameter name and parameter value. Defaults to {}.

        Returns:
            dict: The requested information in the form of a json dictionary.
        """
        r = self.infos.get_info(info_name, params)
        return r

    def subscribe_websocket(self, type_str, event_name = "event", return_property = None, debounce = 0, len = 10):
        try:
            s = Socket(self.ip, type_str, event_name, return_property, debounce, len)
        except:
            return {"result" : "Failed", "message" : "Unknown error occurred."}

        self.websockets[event_name] = s
        return {"result" : "Success", "message" : "Subscribed to the websocket `%s`" % type_str}

    def get_websocket_data(self, event_name, data_type = "data"):
        if event_name in self.websockets.keys():
            if data_type == "data":
                try:
                    return {"result" : "Success", "message" : self.websockets[event_name].data}
                except:
                    return {"result" : "Failed", "message" : "Unknown error occurred."}

            elif data_type == "log":
                try:
                    return {"result" : "Success", "message" : self.websockets[event_name].log}
                except:
                    return {"result" : "Failed", "message" : "Unknown error occurred."}

            else:
                return {"result" : "Failed", "message" : "`%s` is not a valid data type for websocket subscriptions." % data_type}

        else:
            return {"result" : "Failed", "message" : "Websocket `%s` is not subscribed to." % event_name}

    def unsubscribe_websocket(self, event_name):
        if event_name in self.websockets.keys():
            try:
                self.websockets[event_name].unsubscribe()
                mes = {"result" : "Success", "message" : "Websocket `%s` unsubscribed. Log: %s" % (event_name, str(self.websockets[event_name].log))}
            except:
                mes = {"result" : "Failed", "message" : "Unknown error occurred."}
            self.websockets.pop(event_name)
            return mes
        else:
            return {"result" : "Failed", "message" : "Websocket `%s` is not subscribed to." % event_name}