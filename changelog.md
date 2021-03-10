# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## 1.0.0 - 10-03-2021
### Added
- Support for custom defined action and information keywords.
- Support for custom defined data shortcuts.
- Unit tests to test the added features.
- Support for all currently available Misty API endpoints for GET, POST and DELETE methods.
- Event types support.
### Changed
- `Misty.perform_action()` now takes one optional argument `data` instead of three optional arguments `dict`, `string` and `data_method`.
- Several functions now return keyword `"status"` instead of `"result"`.
- README to reflect support for custom definitions and event types.
- README to include documentation of supported keywords and shortcuts.
- Renamed `tests\test_unit.py` to `tests\test_base.py` to reflect on purposes of the tests.
### Note
This release was wrongly tagged as it is not downstream compatible and was published without documentation by mistake.

## 0.0.1 - 21-02-2021
### Added
- This CHANGELOG to track changes.
- README with basic information.
- The package misty2py itself supporting:
    - `api/led` endpoint under the keyword `led`,
    - `api/blink/settings` endpoint under the keyword `blink_settings`,
    - the keyword `led_off` for a json dictionary with values 0 for red, green and blue.

---

## Yanked 0.0.2 - 10-03-2021
### Added
- Support for custom defined action and information keywords.
- Support for custom defined data shortcuts.
- Unit tests to test the added features.
- Support for all currently available Misty API endpoints for GET, POST and DELETE methods.
- Event types support.
### Changed
- `Misty.perform_action()` now takes one optional argument `data` instead of three optional arguments `dict`, `string` and `data_method`.
- Several functions now return keyword `"status"` instead of `"result"`.
- README to reflect support for custom definitions and event types.
- README to include documentation of supported supported keywords and shortcuts.
- Renamed `tests\test_unit.py` to `tests\test_base.py` to reflect on purposes of the tests.
### Note
This release was wrongly tagged as it is not downstream compatible and was published without documentation by mistake.