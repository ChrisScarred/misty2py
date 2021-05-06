from typing import Callable

from misty2py.robot import Misty
from misty2py.utils import *
from utils.env_loader import *


def delete_non_system_files(misty: Callable):
    """TODO: Implement function that deletes all audio, video and image files that are not system assets.

    Args:
        misty (Callable): an instance of Misty class.
    """
    pass


def main():
    """Creates an instance of Misty class and calls the delete function."""
    m = Misty(MISTY_IP)
    delete_non_system_files(m)


if __name__ == "__main__":
    main()
