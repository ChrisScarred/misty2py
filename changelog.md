# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## Unreleased
### Added
- Support for custom defined action and information keywords.
- Support for custom defined data shortcuts.
- Unit tests to test the added features.
### Changed
- README to reflect support for custom definitions.
- Renamed `tests\test_unit.py` to `tests\test_base.py` to reflect on purposes of the tests.

## 0.0.1 - 21-02-2021
### Added
- This CHANGELOG to track changes.
- README with basic information.
- The package misty2py itself supporting:
    - `api/led` endpoint under the keyword `led`,
    - `api/blink/settings` endpoint under the keyword `blink_settings`,
    - the keyword `led_off` for a json dictionary with values 0 for red, green and blue.

