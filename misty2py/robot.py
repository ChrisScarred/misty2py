"""The main script for the misty2py package.
"""
from misty2py.information import *
from misty2py.action import *
from misty2py.utils import *
from misty2py.event_type import *


class Misty:
    """A class representing a Misty robot.

    Attributes:
        ip (str): The IP address of this Misty robot.
        infos (Info()): The object of Info class that belongs to this Misty.
        actions (Action()): The object of Action class that belongs to this Misty.
        event_types (dict): A dictionary of active event type subscriptions (keys being the event name, values the EventType() object).
    """

    def __init__(self, ip: str, custom_info={}, custom_actions={}, custom_data={}) -> None:
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
        self.event_types = {}

    def __str__(self) -> str:
        """Transforms a Misty() object into a string.

        Returns:
            str: A string identifiyng this Misty robot
        """
        return "A Misty II robot with IP address %s" % self.ip

    def perform_action(self, action_name: str, data = {}) -> dict:
        """Sends Misty a request to perform an action.

        Args:
            action_name (str): The keyword specifying the action to perform.
            data (dict, optional): The data to send in the request body in the form of a data shortcut or a json dictionary. Defaults to {}.

        Returns:
            dict: response from the API
        """
        if action_name == "led_trans" and isinstance(data, dict) and len(data)>=2 and len(data)<=4:
            try:
                data = construct_transition_dict(data, self.actions.allowed_data)
            except:
                return {"status" : "Failed", "message" : "Data not in correct format."}

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

    def subscribe_event_type(self, type_str : str, event_name : str = "event", return_property : str = None, debounce : int = 250, len_data_entries : int = 10) -> dict:
        """Subscribes to an event type.

        Args:
            type_str (str): The event type string as required by Misty's websockets.
            event_name (str, optional): A custom event name, must be unique. Defaults to "event".
            return_property (str, optional): The property to return as requeired by Misty's websockets. Defaults to None in which case return all properties.
            debounce (int, optional): The interval at which new information is sent in ms. Defaults to 250.
            len_data_entries (int, optional): The maximum number of data entries to keep (discards in fifo style). Defaults to 10.

        Returns:
            dict: success/fail message in the form of json dict.
        """

        assert debounce >= 0, "debounce interval cannot be negative"
        assert len_data_entries >= 1, "len_data_entries must be positive"

        try:
            s = EventType(self.ip, type_str, event_name, return_property, debounce, len_data_entries)
        except:
            return {"status" : "Failed", "message" : "Unknown error occurred."}

        self.event_types[event_name] = s
        return {"status" : "Success", "message" : "Subscribed to event type `%s`" % type_str}

    def get_event_data(self, event_name : str) -> dict:
        """Obtains data from a subscribed event type.

        Args:
            event_name (str): The name of the event type from which to obtain data.

        Returns:
            dict: the data or the fail message in the form of a json dict.
        """

        if event_name in self.event_types.keys():
            try:
                return {"status" : "Success", "message" : self.event_types[event_name].data}
            except:
                return {"status" : "Failed", "message" : "Unknown error occurred."}

        else:
            return {"status" : "Failed", "message" : "Event type `%s` is not subscribed to." % event_name}

    def get_event_log(self, event_name : str) -> dict:
        """Obtains the log from a subscribed event type.

        Args:
            event_name (str): The name of the event type from which to obtain the log.

        Returns:
            dict: the log or the fail message in the form of a json dict.
        """

        if event_name in self.event_types.keys():
            try:
                return {"status" : "Success", "message" : self.event_types[event_name].log}
            except:
                return {"status" : "Failed", "message" : "Unknown error occurred."}

        else:
            return {"status" : "Failed", "message" : "Event type `%s` is not subscribed to." % event_name}


    def unsubscribe_event_type(self, event_name : str) -> dict:
        """Unsubscribes from an event type.

        Args:
            event_name (str): The name of the event type to unsubscribe.

        Returns:
            dict: success/fail message in the form of json dict.
        """

        if event_name in self.event_types.keys():
            try:
                self.event_types[event_name].unsubscribe()
                mes = {"status" : "Success", "message" : "Event type `%s` unsubscribed. Log: %s" % (event_name, str(self.event_types[event_name].log))}
            except:
                mes = {"status" : "Failed", "message" : "Unknown error occurred."}
            self.event_types.pop(event_name)
            return mes
        else:
            return {"status" : "Failed", "message" : "Event type `%s` is not subscribed to." % event_name}