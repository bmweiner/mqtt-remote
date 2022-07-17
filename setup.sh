# apt sources
sudo apt install curl gnupg
curl https://apt.fury.io/flirc/gpg.key | sudo apt-key add -
echo "deb [arch=armhf] https://apt.fury.io/flirc/ * *" | sudo tee /etc/apt/sources.list.d/fury.list

# apt dependencies
sudo apt update
sudo apt install git
sudo apt install python3-pip
sudo apt install sense-hat
sudo apt install flirc

# python dependencies
python -m pip install paho-mqtt
python -m pip install evdev

sudo dpkg --add-architecture armhf
sudo apt install libreadline8:armhf
cd /lib/arm-linux-gnueabihf/; sudo ln -s libreadline.so.8 libreadline.so.6

# install service
cd /etc/systemd/system; sudo ln -s /home/pi/mqtt-remote/mqtt-remote.service .
sudo systemctl daemon-reload
sudo systemctl enable mqtt-remote.service
sudo systemctl start mqtt-remote.service
