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

- use method `perform_action` to tell Misty to **perform an action:**
    - the first string argument is the action keyword, other optional arguments are:
        - `string` - the data to pass to the request as *a data shortcut*, defaults to `""`
        - `dct` - the data to pass to the request as *a dictionary*, defaults to `{}`
        - `data_method` - `"string"` if the data is passed as a data shrotcut, `"dict"` if the data is passed as a dictionary, defaults to `"dict"`

- use method `get_info` to tell Misty to **return information:**
    - the first string argument is the information keyword, other optional arguments are:
        - `params` - a dictionary of parameter name and parameter value, defaults to `{}`.

### Supported information keywords
| ***name***                 | ***endpoint***             | ***parameters***                               | ***purpose***                                                                                                                          |
|----------------------------|----------------------------|------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------|
| **audio_file**             | api/audio                  | `FileName` (string)                            | obtains the specified audio file                                                                                                       |
| **audio_list**             | api/audio/list             | -                                              | obtains the list of audio files                                                                                                        |
| **audio_status**           | api/services/audio         | -                                              | obtains the audio status                                                                                                               |
| **av_status**              | api/services/avstreaming   | -                                              | obtains the audiovideo status                                                                                                          |
| **battery_status**         | api/battery                | -                                              | obtains the battery status                                                                                                             |
| **blink_settings**         | api/blink/settings         | -                                              | obtains the blink settings                                                                                                             |
| **camera_settings**        | api/camera                 | -                                              | obtains the camera settings                                                                                                            |
| **camera_status**          | api/services/camera        | -                                              | obtains the camera status                                                                                                              |
| **current_map_id**         | api/slam/map/current       | -                                              | obtains the id of the current map                                                                                                      |
| **device**                 | api/device                 | -                                              | obtains information about the robot's OS, hardware, networking and   sensors                                                           |
| **faces_known**            | api/faces                  | -                                              | obtains the list of known faces                                                                                                        |
| **hazards_settings**       | api/hazards/settings       | -                                              | obtains the hazard settings                                                                                                            |
| **help**                   | api/help                   | `command` (string)                             | obtains the help guide for usable commands if parameter not supplied or   obtains the help guide for the specified command if supplied |
| **image_file**             | api/images                 | `FileName` (string)                            | obtains the specified image                                                                                                            |
| **image_list**             | api/images/list            | -                                              | obtains the list of images                                                                                                             |
| **log**                    | api/logs                   | -                                              | obtains the logs                                                                                                                       |
| **log_level**              | api/logs/level             | -                                              | obtains the log level                                                                                                                  |
| **map_file**               | api/slam/map               | `FileName` (string)                            | obtains the specified map file                                                                                                         |
| **map_id_list**            | api/slam/map/ids           | -                                              | obtains the list of map ids                                                                                                            |
| **picture_depth**          | api/cameras/depth          | -                                              | obtains a picture from the depth camera                                                                                                |
| **picture_fisheye**        | api/cameras/fisheye        | -                                              | obtains a picture from the fisheye camera                                                                                              |
| **picture_rgb**            | api/cameras/rgb            | -                                              | obtains a picture from the rgb camera                                                                                                  |
| **recording_file**         | api/videos/recordings      | `FileName` (string)                            | obtains the specified recording file                                                                                                   |
| **recording_list**         | api/videos/recordings/list | -                                              | obtains the list of recordings                                                                                                         |
| **sensor_values**          | api/serial                 | -                                              | obtains the current sensor values                                                                                                      |
| **skills_known**           | api/skills                 | -                                              | obtains the list of known skills                                                                                                       |
| **skills_running**         | api/skills/running         | -                                              | obtains the list of running skills                                                                                                     |
| **slam_diagnostics**       | api/slam/diagnostics       | -                                              | obtains the diagnostic information about the navigation system                                                                         |
| **slam_enabled**           | api/services/slam          | -                                              | checks whether the navigation system is enabled                                                                                        |
| **slam_infrared_settings** | api/slam/settings/ir       | -                                              | obtains the navigation settings for the infrared camera                                                                                |
| **slam_path**              | api/slam/path              | `x` (non-negative int), `y` (non-negative int) | obtains the path to specified coordinates                                                                                              |
| **slam_status**            | api/slam/status            | -                                              | obtains the value representing the current status and activity of the   navigation system                                              |
| **slam_visible_settings**  | api/slam/settings/visible  | -                                              | obtains the navigation settings for the fisheye camera                                                                                 |
| **update_available**       | api/system/updates         | -                                              | checks whether a system update is available                                                                                            |
| **update_settings**        | api/system/update/settings | -                                              | obtains the update settings                                                                                                            |
| **video_file**             | api/videos                 | `FileName` (string)                            | obtains the specified video file                                                                                                       |
| **video_list**             | api/videos/list            | -                                              | obtains the list of videos uploaded to Misty                                                                                           |
| **websocket_version**      | api/websocket/version      | -                                              | obtains the version of websocket                                                                                                       |
| **websockets**             | api/websockets             | optional: websocketClass (str)                 | obtains the list of websockets                                                                                                         |
| **wifis_available**        | api/networks/scan          | -                                              | obtains the list of available wifis                                                                                                    |
| **wifis_saved**            | api/networks               | -                                              | obtains the list of saved wifis                                                                                                        |


### Supported action keywords
| ***name***                | ***method*** | ***endpoint***            | ***parameters***                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | ***purpose***                                                             |
|---------------------------|--------------|---------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------|
| **led**                   | POST         | api/led                   | `red` (int in range 0-255),   `green` (int in range 0-255), `blue` (int in range 0-255)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | changes the chest LED light colour                                        |
| **led_trans**             | POST         | api/led/transition        | *either:* `Red` (int in range   0-255), `Green` (int in range 0-255), `Blue` (int in range 0-255), `Red2`   (int in range 0-255), `Green2` (int in range 0-255), `Blue2` (int in range   0-255), `TransitionType` (`"Breathe"`, `"Blink"` or `"TransitOnce"`),   `TimeMS` (positive int) *or:* `col1` (a data shortcut or a dict of `red`,   `green` and `blue`), `col2` (a data shortcut or a dict of `red`, `green` and   `blue`), optionally `time` (positive integer, defaults to 500) and optionally   `transition` (`"Breathe"`, `"Blink"` or   `"TransitOnce"`, defaults to `"Breathe"`) | changes the chest LED light colour to transitioning between   two colours |
| **notification_settings** | POST         | api/notification/settings | optionally `RevertToDefault`   (bool), optionally `LedEnabled` (bool), optionally `KeyPhraseEnabled` (bool),   optionally `KeyPhraseFile` (str)                                                                                                                                                                                                                                                                                                                                                                                                                                                 | changes the default hardware notifications                                |
| **audio_upload**          | POST         | api/audio                 | `FileName` (str), `Data` (base64   str of a .mp3, .wav, .wma or .aac file), optionally `ImmediatelyApply`   (bool), optionally `OverwriteExisting` (bool)                                                                                                                                                                                                                                                                                                                                                                                                                                       | uploads an audio file                                                     |
| **audio_play**            | POST         | api/audio/play            | `FileName` (str), optionally `Volume` (int in range 0-100)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | plays an audio file                                                       |
| **volume_settings**       | POST         | api/audio/volume          | `Volume` (int in range 0-100)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | sets the default volume                                                   |

### Supported data shortcuts
| ***name***               | ***shortcut for***                                | ***purpose***                                         |
|--------------------------|---------------------------------------------------|-------------------------------------------------------|
| **led_off**              | `{"red": "0", "green": "0",   "blue": "0"}`       | turns off the chest colour when supplied to `led`     |
| **white_light**          | `{"red": "255", "green": "255",   "blue": "255"}` | a colour that can be supplied to `led` or `led_trans` |
| **red_light**            | `{"red": "255", "green": "0",   "blue": "0"}`     | a colour that can be supplied to `led` or `led_trans` |
| **green_light**          | `{"red": "0", "green": "255",   "blue": "0"}`     | a colour that can be supplied to `led` or `led_trans` |
| **blue_light**           | `{"red": "0", "green": "0",   "blue": "255"}`     | a colour that can be supplied to `led` or `led_trans` |
| **yellow_light**         | `{"red": "255", "green": "255",   "blue": "0"}`   | a colour that can be supplied to `led` or `led_trans` |
| **cyan_light**           | `{"red": "0", "green": "255",   "blue": "255"}`   | a colour that can be supplied to `led` or `led_trans` |
| **magenta_light**        | `{"red": "255", "green": "0",   "blue": "255"}`   | a colour that can be supplied to `led` or `led_trans` |
| **orange_light**         | `{"red": "255", "green": "125",   "blue": "0"}`   | a colour that can be supplied to `led` or `led_trans` |
| **lime_light**           | `{"red": "125", "green": "255",   "blue": "0"}`   | a colour that can be supplied to `led` or `led_trans` |
| **aqua_light**           | `{"red": "0", "green": "255",   "blue": "125"}`   | a colour that can be supplied to `led` or `led_trans` |
| **azure_light**          | `{"red": "0", "green": "125",   "blue": "255"}`   | a colour that can be supplied to `led` or `led_trans` |
| **violet_light**         | `{"red": "125", "green": "0",   "blue": "255"}`   | a colour that can be supplied to `led` or `led_trans` |
| **pink_light**           | `{"red": "255", "green": "0",   "blue": "125"}`   | a colour that can be supplied to `led` or `led_trans` |
| **sound_acceptance**     | {"FileName": "s_Acceptance.wav"}                  | an audio file that can be used in `audio_play`        |
| **sound_amazement_1**    | {"FileName": "s_Amazement.wav"}                   | an audio file that can be used in `audio_play`        |
| **sound_amazement_2**    | {"FileName": "s_Amazement2.wav"}                  | an audio file that can be used in `audio_play`        |
| **sound_anger_1**        | {"FileName": "s_Anger.wav"}                       | an audio file that can be used in `audio_play`        |
| **sound_anger_2**        | {"FileName": "s_Anger2.wav"}                      | an audio file that can be used in `audio_play`        |
| **sound_anger_3**        | {"FileName": "s_Anger3.wav"}                      | an audio file that can be used in `audio_play`        |
| **sound_anger_4**        | {"FileName": "s_Anger4.wav"}                      | an audio file that can be used in `audio_play`        |
| **sound_annoyance_1**    | {"FileName": "s_Annoyance.wav"}                   | an audio file that can be used in `audio_play`        |
| **sound_annoyance_2**    | {"FileName": "s_Annoyance2.wav"}                  | an audio file that can be used in `audio_play`        |
| **sound_annoyance_3**    | {"FileName": "s_Annoyance3.wav"}                  | an audio file that can be used in `audio_play`        |
| **sound_annoyance_4**    | {"FileName": "s_Annoyance4.wav"}                  | an audio file that can be used in `audio_play`        |
| **sound_awe_1**          | {"FileName": "s_Awe.wav"}                         | an audio file that can be used in `audio_play`        |
| **sound_awe_2**          | {"FileName": "s_Awe2.wav"}                        | an audio file that can be used in `audio_play`        |
| **sound_awe_3**          | {"FileName": "s_Awe3.wav"}                        | an audio file that can be used in `audio_play`        |
| **sound_boredom**        | {"FileName": "s_Boredom.wav"}                     | an audio file that can be used in `audio_play`        |
| **sound_disapproval**    | {"FileName": "s_Disapproval.wav"}                 | an audio file that can be used in `audio_play`        |
| **sound_disgust_1**      | {"FileName": "s_Disgust.wav"}                     | an audio file that can be used in `audio_play`        |
| **sound_disgust_2**      | {"FileName": "s_Disgust2.wav"}                    | an audio file that can be used in `audio_play`        |
| **sound_disgust_3**      | {"FileName": "s_Disgust3.wav"}                    | an audio file that can be used in `audio_play`        |
| **sound_disoriented_1**  | {"FileName": "s_DisorientedConfused.wav"}         | an audio file that can be used in `audio_play`        |
| **sound_disoriented_2**  | {"FileName": "s_DisorientedConfused2.wav"}        | an audio file that can be used in `audio_play`        |
| **sound_disoriented_3**  | {"FileName": "s_DisorientedConfused3.wav"}        | an audio file that can be used in `audio_play`        |
| **sound_disoriented_4**  | {"FileName": "s_DisorientedConfused4.wav"}        | an audio file that can be used in `audio_play`        |
| **sound_disoriented_5**  | {"FileName": "s_DisorientedConfused5.wav"}        | an audio file that can be used in `audio_play`        |
| **sound_disoriented_6**  | {"FileName": "s_DisorientedConfused6.wav"}        | an audio file that can be used in `audio_play`        |
| **sound_distraction**    | {"FileName": "s_Distraction.wav"}                 | an audio file that can be used in `audio_play`        |
| **sound_ecstacy_1**      | {"FileName": "s_Ecstacy.wav"}                     | an audio file that can be used in `audio_play`        |
| **sound_ecstacy_2**      | {"FileName": "s_Ecstacy2.wav"}                    | an audio file that can be used in `audio_play`        |
| **sound_fear**           | {"FileName": "s_Fear.wav"}                        | an audio file that can be used in `audio_play`        |
| **sound_grief_1**        | {"FileName": "s_Grief.wav"}                       | an audio file that can be used in `audio_play`        |
| **sound_grief_2**        | {"FileName": "s_Grief2.wav"}                      | an audio file that can be used in `audio_play`        |
| **sound_grief_3**        | {"FileName": "s_Grief3.wav"}                      | an audio file that can be used in `audio_play`        |
| **sound_grief_4**        | {"FileName": "s_Grief4.wav"}                      | an audio file that can be used in `audio_play`        |
| **sound_joy_1**          | {"FileName": "s_Joy.wav"}                         | an audio file that can be used in `audio_play`        |
| **sound_joy_2**          | {"FileName": "s_Joy2.wav"}                        | an audio file that can be used in `audio_play`        |
| **sound_joy_3**          | {"FileName": "s_Joy3.wav"}                        | an audio file that can be used in `audio_play`        |
| **sound_joy_4**          | {"FileName": "s_Joy4.wav"}                        | an audio file that can be used in `audio_play`        |
| **sound_loathing**       | {"FileName": "s_Loathing.wav"}                    | an audio file that can be used in `audio_play`        |
| **sound_love**           | {"FileName": "s_Love.wav"}                        | an audio file that can be used in `audio_play`        |
| **sound_phrase_bye_bye** | {"FileName": "s_PhraseByeBye.wav"}                | an audio file that can be used in `audio_play`        |
| **sound_phrase_evil**    | {"FileName": "s_PhraseEvilAhHa.wav"}              | an audio file that can be used in `audio_play`        |
| **sound_phrase_hello**   | {"FileName": "s_PhraseHello.wav"}                 | an audio file that can be used in `audio_play`        |
| **sound_phrase_no**      | {"FileName": "s_PhraseNoNoNo.wav"}                | an audio file that can be used in `audio_play`        |
| **sound_phrase_oopsy**   | {"FileName": "s_PhraseOopsy.wav"}                 | an audio file that can be used in `audio_play`        |
| **sound_phrase_ow**      | {"FileName": "s_PhraseOwOwOw.wav"}                | an audio file that can be used in `audio_play`        |
| **sound_phrase_oww**     | {"FileName": "s_PhraseOwwww.wav"}                 | an audio file that can be used in `audio_play`        |
| **sound_phrase_uh**      | {"FileName": "s_PhraseUhOh.wav"}                  | an audio file that can be used in `audio_play`        |
| **sound_rage**           | {"FileName": "s_Rage.wav"}                        | an audio file that can be used in `audio_play`        |
| **sound_sadness_1**      | {"FileName": "s_Sadness.wav"}                     | an audio file that can be used in `audio_play`        |
| **sound_sadness_2**      | {"FileName": "s_Sadness2.wav"}                    | an audio file that can be used in `audio_play`        |
| **sound_sadness_3**      | {"FileName": "s_Sadness3.wav"}                    | an audio file that can be used in `audio_play`        |
| **sound_sadness_4**      | {"FileName": "s_Sadness4.wav"}                    | an audio file that can be used in `audio_play`        |
| **sound_sadness_5**      | {"FileName": "s_Sadness5.wav"}                    | an audio file that can be used in `audio_play`        |
| **sound_sadness_6**      | {"FileName": "s_Sadness6.wav"}                    | an audio file that can be used in `audio_play`        |
| **sound_sadness_7**      | {"FileName": "s_Sadness7.wav"}                    | an audio file that can be used in `audio_play`        |
| **sound_sleepy_1**       | {"FileName": "s_Sleepy.wav"}                      | an audio file that can be used in `audio_play`        |
| **sound_sleepy_2**       | {"FileName": "s_Sleepy2.wav"}                     | an audio file that can be used in `audio_play`        |
| **sound_sleepy_3**       | {"FileName": "s_Sleepy3.wav"}                     | an audio file that can be used in `audio_play`        |
| **sound_sleepy_4**       | {"FileName": "s_Sleepy4.wav"}                     | an audio file that can be used in `audio_play`        |
| **sound_sleepy_snore**   | {"FileName": "s_SleepySnore.wav"}                 | an audio file that can be used in `audio_play`        |
| **sound_camera_shutter** | {"FileName": "s_SystemCameraShutter.wav"}         | an audio file that can be used in `audio_play`        |
| **sound_failure**        | {"FileName": "s_SystemFailure.wav"}               | an audio file that can be used in `audio_play`        |
| **sound_success**        | {"FileName": "s_SystemSuccess.wav"}               | an audio file that can be used in `audio_play`        |
| **sound_wake**           | {"FileName": "s_SystemWakeWord.wav"}              | an audio file that can be used in `audio_play`        |

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