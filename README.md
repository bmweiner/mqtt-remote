## FLIRC
* Buy the usb dongle

## Install flirc_util

1. Add source to `/etc/apt/sources.list`:
    `deb [trusted=yes] https://apt.fury.io/flirc/ /`
2. Update: `sudo apt update`
3. Install: `sudo apt install flirc`

## Setup MQTT client

1. Add source to `/etc/apt/sources.list`:
    `deb https://repo.mosquitto.org/debian bullseye main`
2. Update: `sudo apt update`
3. Install: `sudo apt install mosquitto-clients`

## Program remote

1. Follow prompt: `flirc_util record`
2. Confirm: `flirc_util settings`

## Python Venv
source infrared/bin/activate
pip freeze -l > requirements.txt
