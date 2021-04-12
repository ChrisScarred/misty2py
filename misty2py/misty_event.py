"""This script enables the websocket information recieval from Misty.
"""
import websocket
import json
import threading
from typing import Callable, Dict, Union

from misty2py.utils import get_random_string


class MistyEvent():
    """A class that represents an event type subscribed to.

    Attributes:
        server (str): Misty's websocket server address.
        data (list): The data entries obtained.
        type_str (str): The event type string as required by Misty's websockets.
        event_name (str): A custom, unique event name. 
        return_property (str): The property to return as requeired by Misty's websockets.
        debounce (int): The interval at which new information is sent in ms.
        log (list): The logs.
        len_data_entries (int): The maximum number of data entries to keep.
        ee (Union[bool, Callable]): The event emitter function if one is desired, False otherwise.
    """

    def __init__(self, ip: str, type_str: str, event_name: str, return_property: str, debounce: int, len_data_entries: int, event_emitter: Union[Callable, None]):
        """Initialises an event object.

        Args:
            ip (str): Misty's IP address.
            type_str (str): The event type string as required by Misty's websockets.
            event_name (str): A custom, unique event name. 
            return_property (str): The property to return as required by Misty's websockets.
            debounce (int): The interval at which new information is sent in ms.
            len_data_entries (int): The maximum number of data entries to keep.
            event_emitter (Union[Callable, None]): The event emitter function if one is desired, False otherwise.
        """

        self.server = "ws://%s/pubsub" % ip
        self.data = []
        self.type_str = type_str
        self.event_name = event_name
        self.return_property = return_property
        self.debounce = debounce
        self.log = []
        self.len_data_entries = len_data_entries
        event_thread = threading.Thread(target=self.run, daemon=True)
        event_thread.start()
        if event_emitter:
            self.ee = event_emitter
        else:
            self.ee = False

    def run(self):
        """Initialises the subscription and data collection.
        """

        self.ws = websocket.WebSocketApp(self.server,
                                on_open = self.on_open,
                                on_message = self.on_message,
                                on_error = self.on_error,
                                on_close = self.on_close)
        self.ws.run_forever()

    def on_message(self, ws, message):
        """Saves received data and if ee is set, emits an event.

        Args:
            ws (websocket.WebSocketApp): the event's websocket.
            message (str): the data.
        """

        message = json.loads(message)
        mes = message["message"]
        if len(self.data) > self.len_data_entries:
            self.data = self.data[1:-1]
        self.data.append(mes)

        if self.ee:
            self.ee.emit(self.event_name, mes)

    def on_error(self, ws, error):
        """Logs an error and if ee is set, emits an 'error' event.

        Args:
            ws (websocket.WebSocketApp): the event type's websocket.
            error (str): the error message.
        """

        if len(self.log) > self.len_data_entries:
            self.log = self.log[1:-1]
        self.log.append(error)

        if self.ee:
            self.ee.emit("error_%s" % self.event_name, error)

    def on_close(self, ws):
        """Appends the closing message to the log and if ee is set, emits a 'close' event.

        Args:
            ws (websocket.WebSocketApp): the event type's websocket.
        """

        mes = "Closed"
        if len(self.log) > self.len_data_entries:
            self.log = self.log[1:-1]
        self.log.append(mes)

        if self.ee:
            self.ee.emit("close_%s" % self.event_name, mes)

    def on_open(self, ws):
        """Appends the opening message to the log and starts the subscription and if ee is set, emits an 'open' event.

        Args:
            ws (websocket.WebSocketApp): the event type's websocket.
        """

        self.log.append("Opened")
        self.subscribe()
        ws.send("")

        if self.ee:
            self.ee.emit("open_%s" % self.event_name)

    def subscribe(self):
        """Constructs the subscription message.
        """

        msg = {
            "Operation" : "subscribe",
            "Type" : self.type_str,
            "DebounceMs" : self.debounce,
            "EventName" : self.event_name,
            "ReturnProperty": self.return_property
        }
        msg_str = json.dumps(msg, separators=(',', ':'))
        self.ws.send(msg_str)

    def unsubscribe(self):
        """Constructs the unsubscription message.
        """
        
        msg = {
            "Operation" : "unsubscribe",
            "EventName" : self.event_name,
            "Message": ""
        }
        msg_str = json.dumps(msg, separators=(',', ':'))
        self.ws.send(msg_str)
        self.ws.close()

class MistyEventHandler:
    """A class that handles all events its related Misty object subscribed to during this runtime.

    Attributes:
        events (Dict): a dictionary of all Event objects its related Misty object subscribed to during this runtime.
        ip (str): the IP address of the Misty belonging to this object's related Misty object.
    """

    def __init__(self, ip: str):
        """Initialises an object of class MistyEventHandler.

        Args:
            ip (str): the IP address of the Misty belonging to this object's related Misty object.
        """

        self.events = {}
        self.ip = ip

    def subscribe_event(self, kwargs: Dict) -> Dict:
        """Subscribes to an event type.

        Args:
            kwargs (Dict):  requires a key "type" (a string representing the event type to subscribe to). Optional keys are:
                - name (str) for a custom event name; must be unique.
                - return_property (str) for the property to return from Misty's websockets; all properties are returned if return_property is not supplied.
                - debounce (int) for the interval at which new information is sent in ms; defaults to 250.
                - len_data_entries (int) for the maximum number of data entries to keep (discards in fifo style); defaults to 10.
                - event_emitter (Callable) for an event emitter function which emits an event upon message recieval.

        Returns:
            Dict: success/fail message in the form of json dict.
        """

        event_type = kwargs.get("type")
        if not event_type:
            return {
                "status" : "Failed", 
                "message" : "No event type specified."
            }

        event_name = kwargs.get("name")
        if not event_name:
            event_name = "event_%s" % get_random_string(8)

        return_property = kwargs.get("return_property")

        debounce = kwargs.get("debounce")
        if not debounce:
            debounce = 250

        len_data_entries = kwargs.get("len_data_entries")
        if not len_data_entries:
            len_data_entries = 10

        event_emitter = kwargs.get("event_emitter")

        try:
            new_event = MistyEvent(
                self.ip, 
                event_type, 
                event_name, 
                return_property, 
                debounce, 
                len_data_entries,
                event_emitter
            )

        except:
            return {
                "status" : "Failed", 
                "message" : "Unknown error occurred while attempting to subscribe to an event of type `%s`." % event_type
            }

        self.events[event_name] = new_event

        return {
            "status" : "Success", 
            "message" : "Subscribed to event type `%s` with name `%s`" % (
                event_type, 
                event_name
            ), 
            "event_name" : event_name
        }

    def get_event_data(self, kwargs: Dict) -> Dict:
        """Obtains data from a subscribed event type.

        Args:
            kwargs (Dict): Requires a key "name" (the event name).

        Returns:
            Dict: the data or the fail message in the form of a json dict.
        """

        event_name = kwargs.get("name")
        if not event_name:
            return {
                "status" : "Failed", 
                "message" : "No event name specified."
            }

        if event_name in self.events.keys():
            try:
                return {
                    "status" : "Success", 
                    "message" : self.events[event_name].data
                }
            except:
                return {
                    "status" : "Failed", 
                    "message" : "Unknown error occurred."
                }

        else:
            return {
                "status" : "Failed", 
                "message" : "Event type `%s` is not subscribed to." % event_name
            }

    def get_event_log(self, kwargs: Dict) -> Dict:
        """Obtains the log from a subscribed event type.

        Args:
            kwargs (Dict): Requires a key "name" (the event name).

        Returns:
            Dict: the log or the fail message in the form of a json dict.
        """

        event_name = kwargs.get("name")
        if not event_name:
            return {
                "status" : "Failed", 
                "message" : "No event name specified."
            }

        if event_name in self.events.keys():
            try:
                return {
                    "status" : "Success", 
                    "message" : self.events[event_name].log
                }
            except:
                return {
                    "status" : "Failed",
                    "message" : "Unknown error occurred while attempting to access the log of event `%s`." % event_name
                }

        else:
            return {
                "status" : "Failed", 
                "message" : "Event `%s` is not subscribed to." % event_name
            }


    def unsubscribe_event(self, kwargs: Dict) -> Dict:
        """Unsubscribes from an event type.

        Args:
            kwargs (Dict): Requires a key "name" (the event name).

        Returns:
            Dict: success/fail message in the form of json dict.
        """

        event_name = kwargs.get("name")
        if not event_name:
            return {
                "status" : "Failed", 
                "message" : "No event name specified."
            }

        if event_name in self.events.keys():
            try:
                self.events[event_name].unsubscribe()
                mes = {
                    "status" : "Success", 
                    "message" : "Event `%s` of type `%s` unsubscribed" % (
                        event_name, 
                        self.events[event_name].type_str
                    ), 
                    "log": self.events[event_name].log
                }
            except:
                mes = {
                    "status" : "Failed", 
                    "message" : "Unknown error occurred while attempting to unsubscribe from event `%s`." % event_name
                }
            self.events.pop(event_name)
            return mes
        else:
            return {
                "status" : "Failed", 
                "message" : "Event type `%s` is not subscribed to." % event_name
            }
