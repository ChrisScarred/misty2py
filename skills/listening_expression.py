from typing import Callable
import time

from misty2py.robot import Misty
from misty2py.utils import *
from utils.env_loader import *


def listening_expression(misty: Callable, colour: str = "azure_light", sound: str = "sound_wake"):
    misty.perform_action("led", data=colour)
    misty.perform_action("audio_play", data=sound)
    time.sleep(1.5)
    misty.perform_action("led", data="led_off")

def main():
    m = Misty(MISTY_IP)
    listening_expression(m)

if __name__=="__main__":
    main()
