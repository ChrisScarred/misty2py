# Misty2py
Misty2py is a python wrapper around [Misty API](https://docs.mistyrobotics.com/misty-ii/rest-api/api-reference/ "Misty Robotics REST API").

## Features
Misty2py can be used to:
- **perform actions** via sending a `POST` or `DELETE` requests to Misty's API;
- **obtain information** via sending a `GET` request to Misty's API;
- **receive continuous streams of data** via subscribing to event types on Misty's websockets.

Misty2py uses following concepts:
- **action keywords** - keywords for endpoints of Misty's API that correspond to performing actions;
- **information keywords** - keywords for endpoints of Misty's API that correspond to retrieving information;
- **data shortcuts** - keywords for commonly used data that is supplied to Misty's API as the body of a `POST` request.

## Usage
### Getting started
- Start by making **a new instance** of `Misty`:

```python
from misty2py.robot import Misty
misty_robot = Misty("0.0.0.0")
```

- Substitute `"0.0.0.0"` with the IP address of your Misty.
- Use method `Misty.perform_action()` to tell Misty to **perform an action**.
- Use the method `Misty.get_info()` to tell Misty to **return information**.
- Use methods `Misty.subscribe_event_type()`, `Misty.unsubscribe_event_type()` and `Misty.get_event_data()` to **obtain continuous streams of data** from Misty's event types.

### Obtaining information
Obtaining digital information is handled by `Misty.get_info()` method.

`Misty.get_info()` has following arguments:
- `info_name` - *required;* the string information keyword corresponding to an endpoint in Misty's API;
- `params` - *optional;* a dictionary of parameter name and parameter value, defaults to `{}`.

### Performing actions
Performing physical and digital actions including removal of non-system files is handled by `Misty.perform_action()` method.

`Misty.perform_action()` has following arguments:
- `action_name` - *required;* the string action keyword corresponding to an endpoint in Misty's API;
- `data` - *optional;* the data to pass to the request as a dictionary or a data shortcut (string), defaults to `{}`.

### Event types
To obtain event data in Misty's framework, it is required to **subscribe** to an event type on Misty's websocket server. Misty's websocket server then streams data to the websocket client, in this implementation via a separate deamon thread. To **access this data,** `Misty.get_event_data()` method must be called from another thread. When data is no longer required to be streamed to the client, an event type can be **unsubscribed** to kill the deamon thread.

#### Subscription
Subscribe to an event via `Misty.subscribe_event_type()` with following arguments:
- `type_str_value` - *required;* event type string as denoted in [Event Types Docs](https://docs.mistyrobotics.com/misty-ii/robot/sensor-data/ "Misty Robotics Event Types").
- `event_name_value` - *optional;* a unique name for this subscription. Defaults to `"event"`.
- `return_property_value` - *optional;* the property to return or `None` if all properties should be returned. Defaults to `None`.
- `debounce_value` - *optional;* the interval at which new information is sent in ms. Defaults to `250`.
- `len_data_entries` - *optional;* the maximum number of data entries to keep. Discards in fifo style (first in, first out). Defaults to `10`.

`Misty.subscribe_event_type()` returns a dictionary with keys `"status"` (value `"Success"` or `"Failed"`) and `"message"` with details.

#### Obtaining data
Given `event_name_value` is a name of a subscribed event, its data can be obtained by: `Misty.get_event_data(event_name_value)`.

`Misty.get_event_data()` returns a dictionary with keys `"status"` (value `"Success"` or `"Failed"`) and `"message"` with the data if successful or error details otherwise.

#### Obtaining logs
Given `event_name_value` is a name of a subscribed event, its logs can be obtained by: `Misty.get_event_log(event_name_value)`.

`Misty.get_event_log()` returns a dictionary with keys `"status"` (value `"Success"` or `"Failed"`) and `"message"` with the logs if successful or error details otherwise.

#### Unsubscribing
Given `event_name_value` is a name of a subscribed event, `event_name_value` can be unsubscribed by: `Misty.unsubscribe_event_type(event_name_value)`.

`Misty.unsubscribe_event_type()` returns a dictionary with keys `"status"` (value `"Success"` or `"Failed"`) and `"message"` with the logs if successful or error details otherwise.

### Keywords and shortcuts
#### List of supported action keywords
- `led` for **post** request to `api/led` endpoint
- `led_trans` for **post** request to `api/led/transition` endpoint
- `notification_settings` for **post** request to `api/notification/settings` endpoint
- `audio_upload` for **post** request `api/audio` to endpoint
- `audio_play` for **post** request to `api/audio/play` endpoint
- `audio_pause` for **post** request to `api/audio/pause` endpoint
- `audio_stop` for **post** request to `api/audio/stop` endpoint
- `audio_delete` for **delete** request to `api/audio` endpoint
- `audio_record_start` for **post** request to `api/audio/record/start` endpoint
- `audio_record_stop` for **post** request to `api/audio/record/stop` endpoint
- `audio_disable` for **post** request to `api/services/audio/disable` endpoint
- `audio_enable` for **post** request to `api/services/audio/enable` endpoint
- `image_upload` for **post** request to `api/images` endpoint
- `image_show` for **post** request to `api/images/display` endpoint
- `image_settings` for **post** request to `api/images/settings` endpoint
- `image_delete` for **delete** request to `api/images` endpoint
- `text_show` for **post** request to `api/text/display` endpoint
- `text_settings` for **post** request to `api/text/settings` endpoint
- `video_upload` for **post** request to `api/videos` endpoint
- `video_show` for **post** request to `api/videos/display` endpoint
- `video_settings` for **post** request to `api/videos/settings` endpoint
- `video_delete` for **delete** request to `api/videos` endpoint
- `blink_mapping_delete` for **delete** request to `api/blink/images` endpoint
- `slam_enable` for **post** request to `api/services/slam/enable` endpoint
- `slam_disable` for **post** request to `api/services/slam/disable` endpoint
- `slam_sensors_reset` for **post** request to `api/slam/reset` endpoint
- `slam_mapping_start` for **post** request to `api/slam/map/start` endpoint
- `slam_mapping_stop` for **post** request to `api/slam/map/stop` endpoint
- `slam_map_current` for **post** request to `api/slam/map/current` endpoint
- `slam_map_rename` for **post** request to `api/slam/map/rename` endpoint
- `slam_infrared_settings` for **post** request to `api/slam/settings/ir` endpoint
- `slam_visible_settings` for **post** request to `api/slam/settings/visible` endpoint
- `slam_map_delete` for **delete** request to `api/slam/map` endpoint
- `slam_docking_locate_start` for **post** request to `api/slam/docking/start` endpoint
- `slam_docking_locate_stop` for **post** request to `api/slam/docking/stop` endpoint
- `streaming_slam_start` for **post** request to `api/slam/streaming/start` endpoint
- `streaming_slam_stop` for **post** request to `api/slam/streaming/stop` endpoint
- `slam_track_start` for **post** request to `api/slam/track/start` endpoint
- `slam_track_stop` for **post** request to `api/slam/track/stop` endpoint
- `recording_start` for **post** request to `api/videos/recordings/start` endpoint
- `recording_stop` for **post** request to `api/videos/recordings/stop` endpoint
- `recording_rename` for **post** request to `api/videos/recordings/rename` endpoint
- `recording_delete` for **delete** request to `api/videos/recordings` endpoint
- `face_detection_start` for **post** request to `api/faces/detection/start` endpoint
- `face_detection_stop` for **post** request to `api/faces/detection/stop` endpoint
- `face_recognition_start` for **post** request to `api/faces/recognition/start` endpoint
- `face_recognition_stop` for **post** request to `api/faces/recognition/stop` endpoint
- `face_train_start` for **post** request to `api/faces/training/start` endpoint
- `face_train_cancel` for **post** request to `api/faces/training/cancel` endpoint
- `face_delete` for **delete** request to `api/faces` endpoint
- `skill_upload` for **post** request to `api/skills` endpoint
- `skill_start` for **post** request to `api/skills/start` endpoint
- `skills_reload` for **post** request to `api/skills/reload` endpoint
- `skill_load` for **post** request to `api/skills/load` endpoint
- `skill_cancel` for **post** request to `api/skills/cancel` endpoint
- `skill_delete` for **delete** request to `api/skills` endpoint
- `wifi_add` for **post** request to `api/networks/create` endpoint
- `wifi_connect` for **post** request to `api/networks` endpoint
- `wifi_delete` for **delete** request to `api/networks` endpoint
- `wifi_hotspot_start` for **post** request to `api/networks/hotspot/start` endpoint
- `wifi_hotspot_stop` for **post** request to `api/networks/hotspot/stop` endpoint
- `write_serial` for **post** request to `api/serial` endpoint
- `event_listener` for **post** request to `api/skills/event` endpoint
- `website_show` for **post** request to `api/webviews/display` endpoint
- `website_settings` for **post** request to `api/webviews/settings` endpoint
- `blink_on` for **post** request to `api/blink` endpoint
- `blink_settings` for **post** request to `api/blink/settings` endpoint
- `display_settings` for **post** request to `api/display/settings` endpoint
- `flashlight_on` for **post** request to `api/flashlight` endpoint
- `speak` for **post** request to `api/tts/speak` endpoint
- `speak_stop` for **post** request to `api/tts/stop` endpoint
- `speech_capture` for **post** request to `api/audio/speech/capture` endpoint
- `drive` for **post** request to `api/drive` endpoint
- `drive_arc` for **post** request to `api/drive/arc` endpoint
- `drive_heading` for **post** request to `api/drive/hdt` endpoint
- `drive_time` for **post** request to `api/drive/time` endpoint
- `drive_track` for **post** request to `api/drive/track` endpoint
- `drive_stop` for **post** request to `api/drive/stop` endpoint
- `drive_to_loc` for **post** request to `api/drive/coordinates` endpoint
- `drive_on_path` for **post** request to `api/drive/path` endpoint
- `halt` for **post** request to `api/halt` endpoint
- `arm_move` for **post** request to `api/arms` endpoint
- `arms_move` for **post** request to `api/arms/set` endpoint
- `head_move` for **post** request to `api/head` endpoint
- `hazard_settings` for **post** request to `api/hazard/updatebasesettings` endpoint
- `streaming_av_start` for **post** request to `api/avstreaming/start` endpoint
- `streaming_av_stop` for **post** request to `api/avstreaming/stop` endpoint
- `streaming_av_disable` for **post** request to `api/services/avstreaming/disable` endpoint
- `streaming_av_enable` for **post** request to `api/services/avstreaming/enable` endpoint
- `keyphrase_recognition_start` for **post** request to `api/audio/keyphrase/start` endpoint
- `keyphrase_recognition_stop` for **post** request to `api/audio/keyphrase/stop` endpoint
- `update_allow` for **post** request to `api/system/update/allow` endpoint
- `update_perform` for **post** request to `api/system/update` endpoint
- `update_perform_targeted` for **post** request to `api/system/update/component` endpoint
- `update_prevent` for **post** request to `api/system/update/prevent` endpoint
- `error_text_clear` for **post** request to `api/text/error/clear` endpoint
- `camera_disable` for **post** request to `api/services/camera/disable` endpoint
- `camera_enable` for **post** request to `api/services/camera/enable` endpoint
- `restart` for **post** request to `api/reboot` endpoint
- `volume_settings` for **post** request to `api/audio/volume` endpoint
- `logs_settings` for **post** request to `api/logs/level` endpoint
- `websocket_settings` for **post** request to `api/websocket/version` endpoint
- `external_request` for **post** request to `api/request` endpoint

#### List of supported information keywords
- `audio_file` for **get** request to `api/audio` endpoint
- `audio_list` for **get** request to `api/audio/list` endpoint
- `audio_status` for **get** request to `api/services/audio` endpoint
- `image_file` for **get** request to `api/images` endpoint
- `image_list` for **get** request to `api/images/list` endpoint
- `video_file` for **get** request to `api/videos` endpoint
- `video_list` for **get** request to `api/videos/list` endpoint
- `av_status` for **get** request to `api/services/avstreaming` endpoint
- `sensor_values` for **get** request to `api/serial` endpoint
- `map_file` for **get** request to `api/slam/map` endpoint
- `current_map_id` for **get** request to `api/slam/map/current` endpoint
- `map_id_list` for **get** request to `api/slam/map/ids` endpoint
- `slam_diagnostics` for **get** request to `api/slam/diagnostics` endpoint
- `slam_path` for **get** request to `api/slam/path` endpoint
- `slam_status` for **get** request to `api/slam/status` endpoint
- `slam_enabled` for **get** request to `api/services/slam` endpoint
- `picture_depth` for **get** request to `api/cameras/depth` endpoint
- `picture_fisheye` for **get** request to `api/cameras/fisheye` endpoint
- `picture_rgb` for **get** request to `api/cameras/rgb` endpoint
- `faces_known` for **get** request to `api/faces` endpoint
- `recording_file` for **get** request to `api/videos/recordings` endpoint
- `recording_list` for **get** request to `api/videos/recordings/list` endpoint
- `skills_running` for **get** request to `api/skills/running` endpoint
- `skills_known` for **get** request to `api/skills` endpoint
- `wifis_available` for **get** request to `api/networks/scan` endpoint
- `wifis_saved` for **get** request to `api/networks` endpoint
- `battery_status` for **get** request to `api/battery` endpoint
- `camera_status` for **get** request to `api/services/camera` endpoint
- `blink_settings` for **get** request to `api/blink/settings` endpoint
- `hazards_settings` for **get** request to `api/hazards/settings` endpoint
- `camera_settings` for **get** request to `api/camera` endpoint
- `slam_visible_settings` for **get** request to `api/slam/settings/visible` endpoint
- `slam_infrared_settings` for **get** request to `api/slam/settings/ir` endpoint
- `update_settings` for **get** request to `api/system/update/settings` endpoint
- `device` for **get** request to `api/device` endpoint
- `help` for **get** request to `api/help` endpoint
- `log` for **get** request to `api/logs` endpoint
- `log_level` for **get** request to `api/logs/level` endpoint
- `update_available` for **get** request to `api/system/updates` endpoint
- `websockets` for **get** request to `api/websockets` endpoint
- `websocket_version` for **get** request to `api/websocket/version`

#### List of supported data shortcuts
- `led_off` for `{ "red": "0", "green": "0", "blue": "0" }`
- `white_light` for `{ "red": "255", "green": "255", "blue": "255" }`
- `red_light` for `{ "red": "255", "green": "0", "blue": "0" }`
- `green_light` for `{ "red": "0", "green": "255", "blue": "0" }`
- `blue_light` for `{ "red": "0", "green": "0", "blue": "255" }`
- `yellow_light` for `{ "red": "255", "green": "255", "blue": "0" }`
- `cyan_light` for `{ "red": "0", "green": "255", "blue": "255" }`
- `magenta_light` for `{ "red": "255", "green": "0", "blue": "255" }`
- `orange_light` for `{ "red": "255", "green": "125", "blue": "0" }`
- `lime_light` for `{ "red": "125", "green": "255", "blue": "0" }`
- `aqua_light` for `{ "red": "0", "green": "255", "blue": "125" }`
- `azure_light` for `{ "red": "0", "green": "125", "blue": "255" }`
- `violet_light` for `{ "red": "125", "green": "0", "blue": "255" }`
- `pink_light` for `{ "red": "255", "green": "0", "blue": "125" }`
- `low_volume` for `{ "Volume": "5" }`
- `sound_acceptance` for `{ "FileName": "s_Acceptance.wav" }`
- `sound_amazement_1` for `{ "FileName": "s_Amazement.wav" }`
- `sound_amazement_2` for `{ "FileName": "s_Amazement2.wav" }`
- `sound_anger_1` for `{ "FileName": "s_Anger.wav" }`
- `sound_anger_2` for `{ "FileName": "s_Anger2.wav" }`
- `sound_anger_3` for `{ "FileName": "s_Anger3.wav" }`
- `sound_anger_4` for `{ "FileName": "s_Anger4.wav" }`
- `sound_annoyance_1` for `{ "FileName": "s_Annoyance.wav" }`
- `sound_annoyance_2` for `{ "FileName": "s_Annoyance2.wav" }`
- `sound_annoyance_3` for `{ "FileName": "s_Annoyance3.wav" }`
- `sound_annoyance_4` for `{ "FileName": "s_Annoyance4.wav" }`
- `sound_awe_1` for `{ "FileName": "s_Awe.wav" }`
- `sound_awe_2` for `{ "FileName": "s_Awe2.wav" }`
- `sound_awe_3` for `{ "FileName": "s_Awe3.wav" }`
- `sound_boredom` for `{ "FileName": "s_Boredom.wav" }`
- `sound_disapproval` for `{ "FileName": "s_Disapproval.wav" }`
- `sound_disgust_1` for `{ "FileName": "s_Disgust.wav" }`
- `sound_disgust_2` for `{ "FileName": "s_Disgust2.wav" }`
- `sound_disgust_3` for `{ "FileName": "s_Disgust3.wav" }`
- `sound_disoriented_1` for `{ "FileName": "s_DisorientedConfused.wav" }`
- `sound_disoriented_2` for `{ "FileName": "s_DisorientedConfused2.wav" }`
- `sound_disoriented_3` for `{ "FileName": "s_DisorientedConfused3.wav" }`
- `sound_disoriented_4` for `{ "FileName": "s_DisorientedConfused4.wav" }`
- `sound_disoriented_5` for `{ "FileName": "s_DisorientedConfused5.wav" }`
- `sound_disoriented_6` for `{ "FileName": "s_DisorientedConfused6.wav" }`
- `sound_distraction` for `{ "FileName": "s_Distraction.wav" }`
- `sound_ecstacy_1` for `{ "FileName": "s_Ecstacy.wav" }`
- `sound_ecstacy_2` for `{ "FileName": "s_Ecstacy2.wav" }`
- `sound_fear` for `{ "FileName": "s_Fear.wav" }`
- `sound_grief_1` for `{ "FileName": "s_Grief.wav" }`
- `sound_grief_2` for `{ "FileName": "s_Grief2.wav" }`
- `sound_grief_3` for `{ "FileName": "s_Grief3.wav" }`
- `sound_grief_4` for `{ "FileName": "s_Grief4.wav" }`
- `sound_joy_1` for `{ "FileName": "s_Joy.wav" }`
- `sound_joy_2` for `{ "FileName": "s_Joy2.wav" }`
- `sound_joy_3` for `{ "FileName": "s_Joy3.wav" }`
- `sound_joy_4` for `{ "FileName": "s_Joy4.wav" }`
- `sound_loathing` for `{ "FileName": "s_Loathing.wav" }`
- `sound_love` for `{ "FileName": "s_Love.wav" }`
- `sound_phrase_bye_bye` for `{ "FileName": "s_PhraseByeBye.wav" }`
- `sound_phrase_evil` for `{ "FileName": "s_PhraseEvilAhHa.wav" }`
- `sound_phrase_hello` for `{ "FileName": "s_PhraseHello.wav" }`
- `sound_phrase_no` for `{ "FileName": "s_PhraseNoNoNo.wav" }`
- `sound_phrase_oopsy` for `{ "FileName": "s_PhraseOopsy.wav" }`
- `sound_phrase_ow` for `{ "FileName": "s_PhraseOwOwOw.wav" }`
- `sound_phrase_oww` for `{ "FileName": "s_PhraseOwwww.wav" }`
- `sound_phrase_uh` for `{ "FileName": "s_PhraseUhOh.wav" }`
- `sound_rage` for `{ "FileName": "s_Rage.wav" }`
- `sound_sadness_1` for `{ "FileName": "s_Sadness.wav" }`
- `sound_sadness_2` for `{ "FileName": "s_Sadness2.wav" }`
- `sound_sadness_3` for `{ "FileName": "s_Sadness3.wav" }`
- `sound_sadness_4` for `{ "FileName": "s_Sadness4.wav" }`
- `sound_sadness_5` for `{ "FileName": "s_Sadness5.wav" }`
- `sound_sadness_6` for `{ "FileName": "s_Sadness6.wav" }`
- `sound_sadness_7` for `{ "FileName": "s_Sadness7.wav" }`
- `sound_sleepy_1` for `{ "FileName": "s_Sleepy.wav" }`
- `sound_sleepy_2` for `{ "FileName": "s_Sleepy2.wav" }`
- `sound_sleepy_3` for `{ "FileName": "s_Sleepy3.wav" }`
- `sound_sleepy_4` for `{ "FileName": "s_Sleepy4.wav" }`
- `sound_sleepy_snore` for `{ "FileName": "s_SleepySnore.wav" }`
- `sound_camera_shutter` for `{ "FileName": "s_SystemCameraShutter.wav" }`
- `sound_failure` for `{ "FileName": "s_SystemFailure.wav" }`
- `sound_success` for `{ "FileName": "s_SystemSuccess.wav" }`
- `sound_wake` for `{ "FileName": "s_SystemWakeWord.wav" }`

#### Adding custom keywords and shortcuts
Custom keywords and shortcuts can be passed to a Misty object while declaring a new instance by using the optional arguments:
- `custom_info` for custom information keywords (a dictionary with keys being the information keywords and values being the endpoints),
- `custom_actions` for custom action keywords (a dictionary with keys being the action keywords and values being a dictionary `{"endpoint" : "edpoint_value", "method" : "method_value"}` where `method_value` is either `post` or `delete`),
- `custom_data` for custom data shortcuts (a dictionary with keys being the data shortcuts and values being the dictionary of data values).

An example:

```python
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
