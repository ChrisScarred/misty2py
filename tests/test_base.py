from misty2py.robot import Misty
import json
from os import path


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

misty_robot = Misty("192.168.0.103", custom_info=custom_allowed_infos, custom_actions=custom_allowed_actions, custom_data=custom_allowed_data)

def test_misty_print():
    assert str(misty_robot) == "A Misty II robot with IP address 192.168.0.103"

def test_basic_action_dict_method():
    colours = {
        "red": "200",
        "green": "20",
        "blue": "40"
    }
    r = misty_robot.perform_action('led', dct=colours, data_method="dict")
    assert r

def test_basic_action_string_method():
    r = misty_robot.perform_action('led', string="led_off", data_method="string")
    assert r

def test_basic_info():
    r = misty_robot.get_info('blink_settings')
    assert r['status'] == 'Success'

def test_custom_action_dict_method():
    colours = {
        "FileName": "s_Amazement.wav"
    }
    r = misty_robot.perform_action('audio_play', dct=colours, data_method="dict")
    assert r

def test_custom_action_string_method():
    r = misty_robot.perform_action('audio_play', string="song", data_method="string")
    assert r

def test_custom_info():
    r = misty_robot.get_info('hazards_settings')
    assert r['status'] == 'Success'