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