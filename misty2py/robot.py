"""The main script for the misty2py package.
"""
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

    def __init__(
        self,
        ip: str,
        custom_info: Dict = {},
        custom_actions: Dict = {},
        custom_data: Dict = {},
    ):
        """Initialises an instance of a Misty robot.

        Args:
            ip (str): The IP address of this Misty robot.
            custom_info (Dict, optional): Custom information keywords in the form of dictionary with key being the keyword and value being the API endpoint. Defaults to {}.
            custom_actions (Dict, optional): Custom actions keywords in the form of dictionary with key being the keyword and value being the API endpoint. Defaults to {}.
            custom_data (Dict, optional): Custom data shortcuts in the form of dictionary with key being the shortcut and value being the json data in the form of a dictionary. Defaults to {}.
        """

        self.ip = ip
        self.infos = Info(ip, custom_allowed_infos=custom_info)
        self.actions = Action(
            ip, custom_allowed_actions=custom_actions, custom_allowed_data=custom_data
        )
        self.event_handler = MistyEventHandler(ip)

    def __str__(self) -> str:
        """Transforms a Misty() object into a string.

        Returns:
            str: A string identifiyng this Misty robot
        """

        return "A Misty II robot with IP address %s" % self.ip

    def perform_action(self, action_name: str, data: Dict = {}) -> Dict:
        """Sends Misty a request to perform an action.

        Args:
            action_name (str): The keyword specifying the action to perform.
            data (Dict, optional): The data to send in the request body in the form of a data shortcut or a json dictionary. Defaults to {}.

        Returns:
            Dict: response from the API
        """

        return self.actions.action_handler(action_name, data)

    def get_info(self, info_name: str, params: Dict = {}) -> Dict:
        """Obtains information from Misty.

        Args:
            info_name (str): The information keyword specifying which kind of information to retrieve.
            params (Dict): dict of parameter name and parameter value. Defaults to {}.

        Returns:
            Dict: The requested information in the form of a json dictionary.
        """

        return self.infos.get_info(info_name, params)

    def event(self, action: str, **kwargs) -> Dict:
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
            Dict: the json dict response.
        """

        if action == "subscribe":
            return self.event_handler.subscribe_event(kwargs)

        if action == "get_data":
            return self.event_handler.get_event_data(kwargs)

        if action == "get_log":
            return self.event_handler.get_event_log(kwargs)

        if action == "unsubscribe":
            return self.event_handler.unsubscribe_event(kwargs)

        return {"status": "Failed", "message": "Unknown event action: `%s`." % action}
