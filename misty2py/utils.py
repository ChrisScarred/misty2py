"""Utility functions for misty2py.
"""
import base64
import string
import random


def get_random_string(n: int) -> str:
    return ''.join(random.SystemRandom().choice(string.ascii_letters + string.digits) for _ in range(n))

def rgb(red: int, green: int, blue: int) -> dict:
    """Returns rgb dictionary from rgb values.

    Args:
        red (int): red value (0-255 including)
        green (int): green value (0-255 including)
        blue (int): blue value (0-255 including)

    Returns:
        dict: a dictionary in the form led requires.
    """

    assert red >= 0 and red <=255, "red value must be between 0 and 255 (bounds included)"
    assert green >= 0 and green <=255, "green value must be between 0 and 255 (bounds included)"
    assert blue >= 0 and blue <=255, "blue value must be between 0 and 255 (bounds included)"

    return {
        "red": red,
        "green": green,
        "blue": blue
    }

def construct_transition_dict(data: dict, allowed_data: dict) -> dict:
    """Constructs input to led_trans action from a dict of two colours data dictionaries or shortcuts (under keys col1, col2) and optionally transition time (key time) and transition style (key transition).

    Args:
        data (dict): a dictionary with keys col1 and col2 containing either a data shortcut for a colour or a dictionary with keys red, green and blue and values 0-255. data may contain keys time with a positive integer value and transition with one of following values: "Breathe", "Blink" or "TransitOnce".

        allowed_data (dict): a dictionary of allowed data shortcuts.

    Returns:
        dict: a dictionary in the form that led_trans requires.
    """
    
    col1 = data['col1']
    if isinstance(col1, str):
        col1 = allowed_data[col1]
    col2 = data['col2']
    if isinstance(col2, str):
        col2 = allowed_data[col2]
    time = 500
    transition = "Breathe"
    if 'time' in data.keys():
        time = data['time']
    if 'transition' in data.keys():
        transition = data['transition']
    dct = {
        "Red": col1["red"],
        "Green": col1["green"],
        "Blue": col1["blue"],
        "Red2": col2["red"],
        "Green2": col2["green"],
        "Blue2": col2["blue"],
        "TransitionType": transition,
        "TimeMS": time
    }
    return dct

def file_to_base64_string(fname: str) -> str:
    """Encodes a file into base64 encoding and into utf-8 string from the encoding.

    Useful for uploading files to Misty.

    Args:
        fname (str): file path

    Returns:
        str: file as base64 string
    """
    data = open(fname, "rb").read()
    encoded = base64.b64encode(data)
    return encoded.decode("utf-8")