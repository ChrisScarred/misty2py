# Misty2py
Misty2py is a python wrapper around [Misty API](https://docs.mistyrobotics.com/misty-ii/rest-api/api-reference/ "Misty Robotics REST API").

## Features
Misty2py can be used to:
- **perform actions** via sending a POST or DELETE requests to Misty's API;
- **obtain information** via sending a GET request to Misty's API;
- **receive continuous streams of data** via subscribing to event types on Misty's websockets.

Misty2py uses following practical concepts:
- **action keywords** - Python-styled keywords for endpoints of Misty's API that correspond to performing actions;
- **information keywords** - Python-styled keywords for endpoints of Misty's API that correspond to retrieving information;
- **data shortcuts** - Python-styled keywords for commonly used data that is supplied to Misty's API as the body of a POST request.

## Usage
### Basics
- start by making **a new instance** of `Misty`:

```
from misty2py.robot import Misty
misty_robot = Misty("0.0.0.0")
```

- substitute `"0.0.0.0"` with the IP address of your Misty.

- use method `perform_action` to tell Misty to **perform an action:**
    - the first string argument is the action keyword corresponding to an endpoint in Misty's API, other optional arguments are:
        - `string` - the data to pass to the request as *a data shortcut*, defaults to `""`
        - `dct` - the data to pass to the request as *a dictionary*, defaults to `{}`
        - `data_method` - `"string"` if the data is passed as a data shrotcut, `"dict"` if the data is passed as a dictionary, defaults to `"dict"`

- use method `get_info` to tell Misty to **return information:**
    - the first string argument is the information keyword, other optional arguments are:
        - `params` - a dictionary of parameter name and parameter value, defaults to `{}`.



### List of supported information keywords

### List of supported action keywords

### List of supported data shortcuts


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

### Event types
To obtain event data in Misty's framework, it is required to **subscribe** to an event type. Misty's websocket server then streams data to the websocket client in a deamon thread. To access this data, it has to be accessed from another thread by the `get_event_data` method. When data is no longer required to be streamed to the client, an event type can be **unsubscribed**.

#### Subscription
Given `m` is an instance of Misty class, one can subscribe to an event type with following code:
```
m.subscribe_event_type(type_str_value, event_name = event_name_value, return_property = return_property_value, debounce = debounce_value, len_data_entries = len_data_entries_value)
```
where:
- `type_str_value` - required; event type string as denoted in [Event Types Docs](https://docs.mistyrobotics.com/misty-ii/robot/sensor-data/ "Misty Robotics Event Types").
- `event_name_value` - optional; a unique name for this subscription. Defaults to `event`.
- `return_property_value` - optional; the property to return or `None` if all properties should be returned. Defaults to `None`.
- `debounce_value` - optional; the interval at which new information is sent in ms. Defaults to `250`.
- `len_data_entries` - optional; the maximum number of data entries to keep. Discards in fifo style (first in, first out). Defaults to `10`.

`subscribe_event_type` returns a dictionary with keys `"result"` (value `"Success"` or `"Failed"`) and `"message"` with details.

#### Obtaining data
Given `m` is an instance of Misty class and `event_name_value` is a name of a subscribed event, its data can be obtained by: `m.get_event_data(event_name_value)`.

`get_event_data` returns a dictionary with keys `"result"` (value `"Success"` or `"Failed"`) and `"message"` with the data if successful or error details otherwise.

#### Obtaining logs
Given `m` is an instance of Misty class and `event_name_value` is a name of a subscribed event, its logs can be obtained by: `m.get_event_log(event_name_value)`.

`get_event_log` returns a dictionary with keys `"result"` (value `"Success"` or `"Failed"`) and `"message"` with the logs if successful or error details otherwise.

#### Unsubscribing
Given `m` is an instance of Misty class and `event_name_value` is a name of a subscribed event, `event_name_value` can be unsubscribed by: `m.unsubscribe_event_type(event_name_value)`.

`unsubscribe_event_type` returns a dictionary with keys `"result"` (value `"Success"` or `"Failed"`) and `"message"` with the logs if successful or error details otherwise.