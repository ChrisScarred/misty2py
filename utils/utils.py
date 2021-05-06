from typing import Dict


def message_parser(data: Dict, message_if_success: str = "Operation successful.", message_if_fail: str = "Operation failed.") -> str:
    """Parses a message from misty2py json Dict reply to a string. 

    Args:
        data (Dict): json Dict to parse.
        message_if_success (str, optional): Brief success-indicating message / keyword. Defaults to "Operation successful.".
        message_if_fail (str, optional): Brief failure-indicating message / keyword. Defaults to "Operation failed.".

    Returns:
        str: Brief success-or-failure-indicating sentence / keyword and detailed information in the next sentence if available.
    """
    message = ""
    potential_message = data.get("message")
    if data.get("status") == "Success":
        message = message_if_success
        if isinstance(potential_message, str):
            message += " %s" % potential_message
    else:
        message = message_if_fail
        if isinstance(potential_message, str):
            message += " %s" % potential_message
    return message