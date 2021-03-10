"""This script enables the websocket information recieval from Misty.
"""
import websocket
import json
import threading


class EventType():
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
    """

    def __init__(self, ip: str, type_str: str, event_name: str, return_property: str, debounce: int, len_data_entries: int):
        """Initialises an event type object.

        Args:
            ip (str): Misty's IP address.
            type_str (str): The event type string as required by Misty's websockets.
            event_name (str): A custom, unique event name. 
            return_property (str): The property to return as requeired by Misty's websockets.
            debounce (int): The interval at which new information is sent in ms.
            len_data_entries (int): The maximum number of data entries to keep.
        """

        self.server = "ws://%s/pubsub" % ip
        self.data = []
        self.type_str = type_str
        self.event_name = event_name
        self.return_property = return_property
        self.debounce = debounce
        self.log = []
        self.len_data_entries = len_data_entries
        thread_daemon = threading.Thread(target=self.run, daemon=True)
        thread_daemon.start()

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
        """Saves received data.

        Args:
            ws (websocket.WebSocketApp): the event type's websocket.
            message (str): the data.
        """

        message = json.loads(message)
        mes = message["message"]
        if len(self.data) > self.len_data_entries:
            self.data = self.data[1:-1]
        self.data.append(mes)

    def on_error(self, ws, error):
        """Logs an error.

        Args:
            ws (websocket.WebSocketApp): the event type's websocket.
            error (str): the error message.
        """

        if len(self.log) > self.len_data_entries:
            self.log = self.log[1:-1]
        self.log.append(error)

    def on_close(self, ws):
        """Appends the closing message to the log.

        Args:
            ws (websocket.WebSocketApp): the event type's websocket.
        """

        mes = "Closed"
        if len(self.log) > self.len_data_entries:
            self.log = self.log[1:-1]
        self.log.append(mes)

    def on_open(self, ws):
        """Appends the opening message to the log and starts the subscription.

        Args:
            ws (websocket.WebSocketApp): the event type's websocket.
        """

        self.log.append("Opened")
        self.subscribe()
        ws.send("")

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
            "EventName" : self.event_name
        }
        msg_str = json.dumps(msg, separators=(',', ':'))
        self.ws.send(msg_str)
        self.ws.close()
