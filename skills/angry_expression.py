import time
from typing import Callable, Union, Dict

from misty2py.robot import Misty
from utils.env_loader import *


def angry_expression(
    misty: Callable,
    expression: str = "image_anger",
    sound: str = "sound_anger_1",
    led_offset: Union[float, int] = 0.5,
    duration: Union[float, int] = 1.5,
    colours: Dict = {"col1": "red_light", "col2": "orange_light", "time": 200},
):
    """Misty appears angry. Her displayed image changes to 'expression' and 'led_offset' seconds after, led changes to 'colours' and 'sound' is played. Lights last for 'duration' seconds and 'expression' image lasts for 'led_offset'+'duration' seconds.

    Args:
        misty (Callable): an instance of Misty class.
        expression (str, optional): The name of the expression image. Defaults to "image_anger".
        sound (str, optional): The name of the sound. Defaults to "sound_anger_1".
        led_offset (Union[float, int], optional): Time till lights and sound are initiated after the image changed in seconds. Defaults to 0.5.
        duration (Union[float, int], optional): Time of duration for the lights in seconds. Defaults to 1.5.
        colours (Dict, optional): The colours of the light in transition format. Defaults to { "col1": "red_light", "col2": "orange_light", "time": 200 }.
    """
    misty.perform_action("image_show", data=expression)
    time.sleep(led_offset)
    misty.perform_action("led_trans", data=colours)
    misty.perform_action("audio_play", data=sound)
    time.sleep(duration)
    misty.perform_action("led", data="led_off")
    misty.perform_action("image_show", data="image_content_default")


def main():
    """Creates a Misty object and calls angry expression with it as a parameter."""
    m = Misty(MISTY_IP)
    angry_expression(m)


if __name__ == "__main__":
    main()
