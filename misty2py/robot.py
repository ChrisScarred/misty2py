"""The main script for the misty2py package.
"""
from typing import Union

from misty2py.information import *
from misty2py.action import *
from misty2py.utils import *
from misty2py.misty_event import MistyEventHandler


class Misty:
    """A class representing a Misty robot.

    Attributes:
        ip (str): The IP address of this Misty robot.
        infos (Info()): The object of Info class that belongs to this Misty.
        actions (Action()): The object of Action class that belongs to this Misty.
        events (dict): A dictionary of active event subscriptions (keys being the event name, values the MistyEvent() object).
    """

    def __init__(self, ip: str, custom_info={}, custom_actions={}, custom_data={}):
        """Initialises an instance of a Misty robot.

        Args:
            ip (str): The IP address of this Misty robot.
            custom_info (dict, optional): Custom information keywords in the form of dictionary with key being the keyword and value being the API endpoint. Defaults to {}.
            custom_actions (dict, optional): Custom actions keywords in the form of dictionary with key being the keyword and value being the API endpoint. Defaults to {}.
            custom_data (dict, optional): Custom data shortcuts in the form of dictionary with key being the shortcut and value being the json data in the form of a dictionary. Defaults to {}.
        """
        self.ip = ip
        self.infos = Info(ip, custom_allowed_infos=custom_info)
        self.actions = Action(ip, custom_allowed_actions=custom_actions, custom_allowed_data=custom_data)
        self.event_handler = MistyEventHandler(ip)

    def __str__(self) -> str:
        """Transforms a Misty() object into a string.

        Returns:
            str: A string identifiyng this Misty robot
        """
        return "A Misty II robot with IP address %s" % self.ip

    def perform_action(self, action_name: str, data: dict = {}) -> dict:
        """Sends Misty a request to perform an action.

        Args:
            action_name (str): The keyword specifying the action to perform.
            data (dict, optional): The data to send in the request body in the form of a data shortcut or a json dictionary. Defaults to {}.

        Returns:
            dict: response from the API
        """

        return self.actions.action_handler(action_name, data)

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

    def event(self, action: str, **kwargs) -> dict:
        """Handles event-related actions.
        
        Supports following actions:
            - event subscripton: requires an action keyword "subscribe" and an argument "type" (a string representing the event type to subscribe to). Optional arguments are:
                - name (str) for a custom event name; must be unique.
                - return_property (str) for the property to return from Misty's websockets; all properties are returned if return_property is not supplied.
                - debounce (int) for the interval at which new information is sent in ms; defaults to 250.
                - len_data_entries (int) for the maximum number of data entries to keep (discards in fifo style); defaults to 10.
                - event_emitter (Callable) for an event emitter function which emits an event upon message recieval.
            - obtaining the data from an event: requires an action keyword "get_data" and an argument "name" (the event name).
            - obtaining the log from an event: requires an action keyword "get_log" and an argument "name" (the event name).
            - unsubscribing from an event: requires an action keyword "unsubscribe" and an argument "name" (the event name).

        Args:
            action (str): the action keyword.

        Returns:
            dict: the json dict response.
        """

        if action == "subscribe":
            return self.event_handler.subscribe_event(kwargs)

        if action == "get_data":
            return self.event_handler.get_event_data(kwargs)

        if action == "get_log":
            return self.event_handler.get_event_log(kwargs)

        if action == "unsubscribe":
            return self.event_handler.unsubscribe_event(kwargs)

        return {
            "status": "Failed",
            "message": "Unknown event action: `%s`." % action
        }
