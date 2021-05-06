from typing import Callable

from misty2py.robot import Misty
from misty2py.utils import *
from utils.env_loader import *


def do_something(misty: Callable):
    """Do something with Misty here.

    Args:
        misty (Callable): an instance of Misty class.
    """
    misty.perform_action("led", data="led_off")


def main():
    """Creates an instance of Misty class and calls the skill function."""
    m = Misty(MISTY_IP)
    do_something(m)


if __name__ == "__main__":
    main()
