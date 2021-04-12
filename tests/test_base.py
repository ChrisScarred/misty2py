from misty2py.robot import Misty
import json
from os import path
import time

this_directory = path.abspath(path.dirname(__file__))
action_file = str(path.join(this_directory, "custom_allowed_actions.json"))
data_file = str(path.join(this_directory, "custom_allowed_data.json"))
info_file = str(path.join(this_directory, "custom_allowed_infos.json"))

f = open(info_file)
custom_allowed_infos = json.loads(f.read())
f.close()
f = open(data_file)
custom_allowed_data = json.loads(f.read())
f.close()
f = open(action_file)
custom_allowed_actions = json.loads(f.read())
f.close()

misty_robot = Misty(
    "192.168.0.103",
    custom_info=custom_allowed_infos,
    custom_actions=custom_allowed_actions,
    custom_data=custom_allowed_data,
)


def test_misty_print():
    assert str(misty_robot) == "A Misty II robot with IP address 192.168.0.103"


def test_basic_action_dict_method():
    colours = {"red": "200", "green": "20", "blue": "40"}
    r = misty_robot.perform_action("led", data=colours)
    assert r["status"] == "Success"


def test_basic_action_string_method():
    r = misty_robot.perform_action("led", data="led_off")
    assert r["status"] == "Success"


def test_basic_info():
    r = misty_robot.get_info("blink_settings")
    assert r["status"] == "Success"


def test_custom_action_dict_method():
    colours = {"FileName": "s_Amazement.wav"}
    r = misty_robot.perform_action("audio_play", data=colours)
    assert r["status"] == "Success"


def test_custom_action_string_method():
    r = misty_robot.perform_action("audio_play", data="amazement")
    assert r["status"] == "Success"


def test_custom_info():
    r = misty_robot.get_info("hazards_settings")
    assert r["status"] == "Success"


def test_query_params():
    r = misty_robot.get_info(
        "audio_file", {"FileName": "s_Amazement.wav", "base64": "false"}
    )
    assert r["content"][0:10] == b"RIFF$\x07\x06\x00WA"


def test_event_type_data():
    misty_robot.subscribe_event("BatteryCharge", event_name="Battery Event")
    time.sleep(1)
    data = misty_robot.get_event_data("Battery Event")
    misty_robot.unsubscribe_event("Battery Event")
    assert data["status"] == "Success"


def test_event_type_log():
    misty_robot.subscribe_event("BatteryCharge", event_name="Battery Event")
    time.sleep(1)
    data = misty_robot.get_event_log("Battery Event")
    misty_robot.unsubscribe_event("Battery Event")
    assert data["status"] == "Success"


def test_event_type_unsubscription():
    misty_robot.subscribe_event("BatteryCharge", event_name="Battery Event")
    time.sleep(1)
    data = misty_robot.get_event_data("Battery Event")
    misty_robot.unsubscribe_event("Battery Event")
    nodata = misty_robot.get_event_data("Battery Event")
    assert data["status"] == "Success" and nodata["status"] == "Failed"
