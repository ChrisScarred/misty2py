import requests

from misty.robot import Misty


misty_robot = Misty("192.168.0.103")

def test_misty_print():
    assert str(misty_robot) == "A Misty II robot with IP address 192.168.0.103"

def test_led_off():
    r = misty_robot.perform_action('led', string="led_off", method="string")
    assert r

def test_led_value():
    colours = {
        "red": "200",
        "green": "20",
        "blue": "40"
    }
    r = misty_robot.perform_action('led', dct=colours, method="dict")