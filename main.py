from time import sleep
from evdev import InputDevice, categorize, ecodes
from sense_hat import SenseHat
import paho.mqtt.client as mqtt

class Remote():
    def __init__(self, dev, actions):
        self.actions = actions

        # setup keyboard
        self.keyboard = InputDevice(dev)

        # setup mqtt
        client = mqtt.Client()
        client.on_connect = self._on_connect
        client.on_message = self._on_message
        certs = {
            "ca_certs": "local/certs/ca.crt",
            "certfile": "local/certs/client.crt",
            "keyfile": "local/certs/client.key"
        }
        client.tls_set(**certs)
        client.tls_insecure_set(True)
        with open("local/creds") as f:
            username, password = f.readlines()[0].split(":")
        client.username_pw_set(username, password)
        self.client = client

        # setup sense hat
        sense = SenseHat()
        sense.set_rotation(90)
        self.sense = sense

    def _on_connect(self, client, userdata, flags, rc):
        print("Connected with result code "+str(rc))
        client.subscribe("$SYS/#")

    def _on_message(self, client, userdata, msg):
        print(msg.topic+" "+str(msg.payload))

    def read_loop(self):
        for event in self.keyboard.read_loop():
            # keyboard button pressed
            if event.type == ecodes.EV_KEY & event.value == 1:
                code = event.code
                key = categorize(event).keycode

                # process action for code
                if key in self.actions:
                    action = actions[key]
                    print(key, action)
                    self.sense.clear(action['RGB'])
                    self.client.connect("ha", 8883)
                    self.client.publish(action['topic'], action['msg'])
                    sleep(1)
                    self.sense.clear()

if __name__ == '__main__':
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    YELLOW = (255, 255, 0)
    BLUE = (0, 0, 255)

    dev = "/dev/input/by-id/usb-flirc.tv_flirc-if01-event-kbd"
    actions = {
        "KEY_0" : {
            "RGB": RED,
            "topic": "remote/living_room_light",
            "msg": "toggle"
        },
        "KEY_1" : {
            "RGB": GREEN,
            "topic": "remote/living_room_light",
            "msg": "dim"
        },
        "KEY_2" : {
            "RGB": YELLOW,
            "topic": "remote/tts",
            "msg": "wiki_today"
        },
        "KEY_3" : {
            "RGB": BLUE,
            "topic": "remote/living_room_light",
            "msg": "toggle"
        }
    }
    remote = Remote(dev, actions)
    remote.read_loop()
