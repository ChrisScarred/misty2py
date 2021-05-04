import time
import sys
from typing import Callable, Dict, Iterable, List, Union
from pymitter import EventEmitter

from misty2py.robot import Misty


ee = EventEmitter()
event_name = "myevent_001"
DEFAULT_DURATION = 2


@ee.on(event_name)
def listener(data: Dict):
    """Prints received data every time 'event_name' emits data.

    Args:
        data (Dict): the json data received by the event subscription handler.
    """
    print(data)


def battery_printer(misty: Callable, duration: Union[int, float]):
    """Prints Misty's battery status every 250ms for 'duration' seconds.

    Args:
        misty (Callable): an instance of a Misty class.
        duration (Union[int,float]): the requested duration of the printing behaviour in seconds.
    """
    event_type = "BatteryCharge"
    d = misty.event("subscribe", type=event_type, name=event_name, event_emitter=ee)
    print(d)
    time.sleep(duration)
    d = misty.event("unsubscribe", name=event_name)
    print(d)


def main(args: Iterable):
    """Obtains the requested duration (is seconds) of subscription to an event and calls the event handling method.

    Args:
        args (Iterable): CLI arguments

    Raises:
        TypeError: if the second CLI argument is not an integer, a float or non-existant.
    """
    if len(args) > 1:
        arg_1 = args[1]
        try:
            arg_1 = float(arg_1)
        except:
            raise TypeError("This script expects a single integer or float argument")
        duration = arg_1
    else:
        duration = DEFAULT_DURATION

    m = Misty("192.168.0.103")
    battery_printer(m, duration)


if __name__ == "__main__":
    main(sys.argv)
