import requests

from misty.robot import Misty


misty_robot = Misty("192.168.0.103")

def test_misty_print():
    assert str(misty_robot) == "A Misty II robot with IP address 192.168.0.103"

def test_light_off():
    cols = {
        "red": "0",
        "green": "0",
        "blue": "0"
    }
    r = misty_robot.action('api/led', cols)
    assert r