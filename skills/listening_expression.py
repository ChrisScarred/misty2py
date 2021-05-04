from typing import Callable, Union
import time

from misty2py.robot import Misty
from misty2py.utils import *
from utils.env_loader import *


def listening_expression(
    misty: Callable,
    colour: str = "azure_light",
    sound: str = "sound_wake",
    duration: Union[float, int] = 1.5,
):
    """Misty plays a sound and lights up to appear interested / listening. Lights last for 'duration' seconds. The sound is played in the begining right after the lights are lit.

    Args:
        misty (Callable): an instance of Misty class.
        colour (str, optional): The led colour. Defaults to "azure_light".
        sound (str, optional): The sound. Defaults to "sound_wake".
        duration (Union[float, int], optional): The duration of lights in seconds. Defaults to 1.5.
    """
    misty.perform_action("led", data=colour)
    misty.perform_action("audio_play", data=sound)
    time.sleep(duration)
    misty.perform_action("led", data="led_off")


def main():
    """Creates an instance of Misty class and calls the listening_expression function with the instance as an argument."""
    m = Misty(MISTY_IP)
    listening_expression(m)


if __name__ == "__main__":
    main()
