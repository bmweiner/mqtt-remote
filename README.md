## Hardware
* Buy the usb dongle
* Raspberry PI Model 3B+ (2022-04-04-raspios-bullseye-arm64-lite)

## Install dependencies

    sh setup.sh

## Program remote

1. Follow prompt: `flirc_util record`
2. Confirm: `flirc_util settings`

## Verify Scripts

1. mqtt-remote.service: verify installation directory and user
2. main.py: update actions dictionary and device address
3. main.py: verify local path to mqtt certs and creds

## Reload Service

    sudo systemctl restart mqtt-remote
