from build.lib.misty2py import action
from typing import Callable
from pymitter import EventEmitter
import time

from misty2py.robot import Misty
from misty2py.utils import *
from utils.env_loader import *
from utils.utils import *
from skills.listening_expression import listening_expression


ee = EventEmitter()
event_name = "listening_greeting_%s" % get_random_string(6)

misty = Misty(MISTY_IP)


@ee.on(event_name)
def listener(data: Dict):
    """Prints received data every time 'event_name' emits data.

    Args:
        data (Dict): the json data received by the event subscription handler.
    """
    conf = data.get("confidence")
    if isinstance(conf, int):
        if conf >= 60:
            listening_expression(misty)
    print(data)


def greet():
    """TODO: Document"""
    result = misty.perform_action(
        "keyphrase_recognition_start", data={"CaptureSpeech": "false"}
    )
    print(message_parser(result))
    event_type = "KeyPhraseRecognized"
    d = misty.event("subscribe", type=event_type, name=event_name, event_emitter=ee)
    print(message_parser(d))
    time.sleep(15)
    input(">>> Press any key to terminate <<<")
    d = misty.event("unsubscribe", name=event_name)
    print(message_parser(d))
    result = misty.perform_action("keyphrase_recognition_stop")
    print(message_parser(result))


def main():
    """Calls the greeting function."""
    greet()


if __name__ == "__main__":
    main()
