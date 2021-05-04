"""Utility functions for misty2py.
"""
import base64
import string
import random
from typing import Dict


def get_random_string(n: int) -> str:
    """Constructs an n characters long random string containing ASCII letters and digits.

    Args:
        n (int): the required length of the string.

    Returns:
        str: the random string.
    """

    assert n > 0, "Required string length must be a positive integer."

    return "".join(
        random.SystemRandom().choice(string.ascii_letters + string.digits)
        for _ in range(n)
    )


def rgb(red: int, green: int, blue: int) -> Dict:
    """Returns rgb dictionary from rgb values.

    Args:
        red (int): red value (0-255 including)
        green (int): green value (0-255 including)
        blue (int): blue value (0-255 including)

    Returns:
        dict: a dictionary in the form led requires.
    """

    assert (
        red >= 0 and red <= 255
    ), "red value must be between 0 and 255 (bounds included)"
    assert (
        green >= 0 and green <= 255
    ), "green value must be between 0 and 255 (bounds included)"
    assert (
        blue >= 0 and blue <= 255
    ), "blue value must be between 0 and 255 (bounds included)"

    return {"red": red, "green": green, "blue": blue}


def construct_transition_dict(data: Dict, allowed_data: Dict) -> Dict:
    """Constructs input to led_trans action from a dict of two colours data dictionaries or shortcuts (under keys col1, col2) and optionally transition time (key time) and transition style (key transition).

    Args:
        data (dict): a dictionary with keys col1 and col2 containing either a data shortcut for a colour or a dictionary with keys red, green and blue and values 0-255. data may contain keys time with a positive integer value and transition with one of following values: "Breathe", "Blink" or "TransitOnce".

        allowed_data (dict): a dictionary of allowed data shortcuts.

    Returns:
        dict: a dictionary in the form that led_trans requires.
    """

    col1 = data.get("col1")
    if col1:
        if isinstance(col1, str):
            col1 = allowed_data[col1]
    else:
        raise ValueError("The `col1` value is missing.")

    col2 = data.get("col2")
    if col2:
        if isinstance(col2, str):
            col2 = allowed_data[col2]
    else:
        raise ValueError("The `col2` value is missing.")

    time = 500
    if "time" in data.keys():
        time = data["time"]

    transition = "Breathe"
    if "transition" in data.keys():
        transition = data["transition"]

    for subcolour in ["red", "green", "blue"]:
        val1 = int(col1.get(subcolour))

        if val1:
            if val1 < 0 or val1 > 255:
                raise ValueError("Invalid value: `%s` of `col1`" % subcolour)
        else:
            raise ValueError("Missing value: `%s` of `col1`" % subcolour)

        val2 = int(col2.get(subcolour))

        if val2:
            if val2 < 0 or val2 > 255:
                raise ValueError("Invalid value: `%s` of `col2`" % subcolour)
        else:
            raise ValueError("Missing value: `%s` of `col2`" % subcolour)

    return {
        "Red": col1["red"],
        "Green": col1["green"],
        "Blue": col1["blue"],
        "Red2": col2["red"],
        "Green2": col2["green"],
        "Blue2": col2["blue"],
        "TransitionType": transition,
        "TimeMS": time,
    }


def file_to_base64_string(fname: str) -> str:
    """Encodes a file into base64 encoding and into utf-8 string from the encoding.

    Useful for uploading files to Misty.

    Args:
        fname (str): file path

    Returns:
        str: file as base64 string
    """
    try:
        data = open(fname, "rb").read()
        encoded = base64.b64encode(data)
        return encoded.decode("utf-8")
    except:
        return "Unknown error while encoding the file `%s`" % fname
