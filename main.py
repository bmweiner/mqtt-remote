from evdev import InputDevice, categorize, ecodes

# FLIR = "/dev/input/by-id/usb-flirc.tv_flirc-if01-event-kbd"
FLIR = "/dev/input/by-id/usb-flirc.tv_flirc-event-if01"

device = InputDevice(FLIR)
for event in device.read_loop():
    if event.type == ecodes.EV_KEY:
        print(categorize(event))
