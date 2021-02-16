#!/usr/bin/env sh

FOLDER=$(dirname $(realpath "$0"))
cd $FOLDER

yes | sudo pip3 install adafruit-circuitpython-ads1x15
yes | sudo pip3 install adafruit-circuitpython-mpu6050

sudo apt-get install -y pigpio python-pigpio python3-pigpio

for file in *.service; do
    [ -f "$file" ] || break
    sudo ln -s $FOLDER/$file /lib/systemd/system/
done

sudo systemctl daemon-reload
sudo systemctl enable monitor_battery # starts program on boot
sudo systemctl enable pigpiod
