# apt sources
sudo cp flirc.list /etc/apt/sources.list.d 

# apt dependencies
sudo apt update
sudo apt upgrade
sudo apt install sense-hat
sudo apt install flirc

# install pip
wget https://bootstrap.pypa.io/get-pip.py
python3 get-pip.py
rm get-pip.py

# python dependencies
pip3 install paho-mqtt
pip3 install pyusb

# install flirc rules
sudo cp 99-flirc.rules /etc/udev/rules.d/
#sudo udevadm control --reload-rules && sudo udevadm trigger
