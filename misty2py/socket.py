import websocket
import json
import threading


class Socket():
    def __init__(self, ip, type_str, event_name, return_property, debounce, len):
        self.server = "ws://%s/pubsub" % ip
        self.data = []
        self.type_str = type_str
        self.event_name = event_name
        self.return_property = return_property
        self.debounce = debounce
        self.log = []
        self.len = len
        thread_daemon = threading.Thread(target=self.run, daemon=True)
        thread_daemon.start()

    def run(self):
        self.ws = websocket.WebSocketApp(self.server,
                                on_open = self.on_open,
                                on_message = self.on_message,
                                on_error = self.on_error,
                                on_close = self.on_close)
        self.ws.run_forever()

    def on_message(self, ws, message):
        message = json.loads(message)
        mes = message["message"]
        if len(self.data) > self.len:
            self.data = [mes]
        else:
            self.data.append(mes)

    def on_error(self, ws, error):
        if len(self.log) > self.len:
            self.log = [error]
        else:
            self.log.append(error)

    def on_close(self, ws):
        mes = "Closed"
        if len(self.log) > self.len:
            self.log = [mes]
        else:
            self.log.append(mes)

    def on_open(self, ws):
        self.log.append("Opened")
        self.subscribe()
        ws.send("")

    def subscribe(self):
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
        msg = {
            "Operation" : "unsubscribe",
            "EventName" : self.event_name
        }
        msg_str = json.dumps(msg, separators=(',', ':'))
        self.ws.send(msg_str)
        self.ws.close()
