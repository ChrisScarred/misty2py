# Misty2py
Misty2py is a python wrapper around [Misty API](https://docs.mistyrobotics.com/misty-ii/rest-api/api-reference/ "Misty Robotics REST API").

## Features
Misty2py can be used to:
- **perform actions** as an equivalent to sending a POST or DELETE request to Misty's API;
- **obtain information** as an equivalent to sending a GET request to Misty's API.

This can be done comfortably from Python by employing following concepts:
- **action keywords** - Python-styled keywords for endpoints of Misty's API that correspond to performing actions;
- **information keywords** - Python-styled keywords for endpoints of Misty's API that correspond to retrieving information;
- **data shortcuts** - Python-styled keywords for commonly used data that is supplied to Misty's API as the body of a POST request.

## Usage
- start by making **a new instance** of `Misty`:

```
from misty2py.robot import Misty
misty_robot = Misty("0.0.0.0")
```

- substitute `"0.0.0.0"` with the IP address of your Misty.

- use method `perform_action` to tell Misty to **perform an action**
    - the first string argument is the action keyword, other arguments are:
        - `string` - the data to pass to the request as *a data shortcut*, defaults to `""`
        - `dct` - the data to pass to the request as *a dictionary*, defaults to `{}`
        - `data_method` - `"string"` if the data is passed as a data shrotcut, `"dict"` if the data is passed as a dictionary, defaults to `"dict"`

- use method `get_info` to tell Misty to **return information**
    - the one string argument is the information keyword
    
### Supported action keywords
| keyword | endpoint  | data format                                                                                                                  | explanation                 |
|---------|-----------|------------------------------------------------------------------------------------------------------------------------------|-----------------------------|
| `led`   | `api/led` | `{"red" : "red_int_val", "green" : "green_int_val", "blue" : "blue_int_val"}` with values being in range 0-255 (including)   | changes the chest LED light |

### Supported information keywords
| keyword          | endpoint             | explanation            |
|------------------|----------------------|------------------------|
| `blink_settings` | `api/blink/settings` | returns blink settings |

### Supported data shortcuts
| shortcut  | dictionary                             | explanation   |
|-----------|----------------------------------------|---------------|
| `led_off` | `{"red" : 0, "green" : 0, "blue" : 0}` | led light off |

### Adding custom keywords and shortcuts
- Custom keywords and shortcuts can be passed to a Misty object while declaring a new instance by using the optional arguments:
    - `custom_info` for custom information keywords (a dictionary with keys being the information keywords and values being the endpoints),
    - `custom_actions` for custom action keywords (a dictionary with keys being the action keywords and values being a dictionary `{"endpoint" : "edpoint_value", "method" : "method_value"}` where `method_value` is either `post` or `delete`),
    - `custom_data` for custom data shortcuts (a dictionary with keys being the data shortcuts and values being the dictionary of data values).
- An example:

```
custom_allowed_infos = {
    "hazards_settings": "api/hazards/settings"
}

custom_allowed_data = {
    "amazement": {
        "FileName": "s_Amazement.wav"
    },
    "red": {
        "red": "255",
        "green": "0",
        "blue": "0"
    }
}

custom_allowed_actions = {
    "audio_play" : {
        "endpoint" : "api/audio/play",
        "method" : "post"
    },
    "delete_audio" : {
        "endpoint" : "api/audio",
        "method" : "delete"
    }
}

misty_robot = Misty("0.0.0.0", 
    custom_info=custom_allowed_infos, 
    custom_actions=custom_allowed_actions, 
    custom_data=custom_allowed_data)
```
