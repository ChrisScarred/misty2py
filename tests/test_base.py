import json
from os import path
import time

from misty2py.robot import Misty


DIR_NAME = path.abspath(path.dirname(__file__))

with open(path.join(DIR_NAME, "custom_allowed_actions.json")) as f:
    custom_allowed_infos = json.loads(f.read())
with open(path.join(DIR_NAME, "custom_allowed_data.json")) as f:
    custom_allowed_data = json.loads(f.read())
with open(path.join(DIR_NAME, "custom_allowed_infos.json")) as f:
    custom_allowed_actions = json.loads(f.read())

MISTY = Misty(
    "192.168.0.103",
    custom_info=custom_allowed_infos,
    custom_actions=custom_allowed_actions,
    custom_data=custom_allowed_data,
)


def test_misty_print():
    assert str(MISTY) == "A Misty II robot with IP address 192.168.0.103"

def test_basic_action_dict_method():
    colours = {"red": "200", "green": "20", "blue": "40"}
    r = MISTY.perform_action("led", data=colours)
    assert r["status"] == "Success"

def test_basic_action_string_method():
    r = MISTY.perform_action("led", data="led_off")
    assert r["status"] == "Success"

def test_basic_info():
    r = MISTY.get_info("blink_settings")
    assert r["status"] == "Success"

def test_custom_action_dict_method():
    colours = {"FileName": "s_Amazement.wav"}
    r = MISTY.perform_action("audio_play", data=colours)
    assert r["status"] == "Success"

def test_custom_action_string_method():
    r = MISTY.perform_action("audio_play", data="amazement")
    assert r["status"] == "Success"

def test_custom_info():
    r = MISTY.get_info("hazards_settings")
    assert r["status"] == "Success"

def test_query_params():
    r = MISTY.get_info(
        "audio_file", {"FileName": "s_Amazement.wav", "base64": "false"}
    )
    assert r["content"][0:10] == b"RIFF$\x07\x06\x00WA"

def test_event_type_data():
    MISTY.event("subscribe", type="BatteryCharge", name="Battery Event")
    time.sleep(0.5)
    data = MISTY.event("get_data", name="Battery Event")
    MISTY.event("unsubscribe", name="Battery Event")
    assert data["status"] == "Success"

def test_event_type_log():
    MISTY.event("subscribe", type="BatteryCharge", name="Battery Event")
    time.sleep(0.5)
    data = MISTY.event("get_log", name="Battery Event")
    MISTY.event("unsubscribe", name="Battery Event")
    assert data["status"] == "Success"

def test_event_type_unsubscription():
    MISTY.event("subscribe", type="BatteryCharge", name="Battery Event")
    time.sleep(0.5)
    data = MISTY.event("get_data", name="Battery Event")
    MISTY.event("unsubscribe", name="Battery Event")
    nodata = MISTY.event("get_data", name="Battery Event")
    assert data["status"] == "Success" and nodata["status"] == "Failed"
