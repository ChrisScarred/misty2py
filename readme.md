# Misty2py
Misty2py is a python wrapper around [Misty API](https://docs.mistyrobotics.com/misty-ii/rest-api/api-reference/ "Misty Robotics REST API").

## Features
Misty2py can be used to:
- **perform actions** as an equivalent to sending a POST request to Misty's API;
- **obtain information** as an equivalent to sending a GET request to Misty's API.

This can be done comfortably from Python by employing following concepts:
- **action keywords** - Python-styled keywords for endpoints of Misty's API that correspond to performing actions;
- **information keywords** - Python-styled keywords for endpoints of Misty's API that correspond to retrieving information;
- **data shortcuts** - Python-styled keywords for commonly used data that is supplied to Misty's API as the body of a POST request.

## Usage
- start by making a new instance of `Misty`:
```
from misty2py.robot import Misty
misty_robot = Misty("0.0.0.0")
```
- substitute `"0.0.0.0"` with the IP address of your Misty.
- optional parameters can be used to pass custom keywords and shortcuts:
    - `custom_info` takes custom information keywords in the form of a dictionary with keys being the keywords and values being the API endpoints.
    - `custom_actions` takes custom actions keywords in the form of a dictionary with keys being the keywords and values being the API endpoints.
    - `custom_data` takes custom data shortcuts in the form of a dictionary with keys being the shortcuts and values being the json data in the form of a dictionary.
- use method `perform_action` to tell Misty to perform an action
    - currently you can only use `misty_robot.perform_action('led', dct=colours, method="dict")` to change the LED light on Misty's chest to a supplied json value or `misty_robot.perform_action('led', string="led_off", method="string")` to turn the LED light on Misty's chest off
    - the action `led` corresponds to the `/api/led` endpoint
- use method `get_info` to tell Misty to return information
    - currently only `misty_robot.get_info(blink_settings)` to obtain blink settings is supported (corresponds to the `api/blink/settings` endpoint)
    
### More action and information keywords and data shortcuts will be added soon
