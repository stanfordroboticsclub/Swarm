#!/usr/bin/env sh

FOLDER=$(dirname $(realpath "$0"))
cd $FOLDER

sudo apt update
sudo apt install -y git vim screen python3-pip
yes | sudo pip3 install --upgrade pip

# turns on i2c and installs some utilities
sudo raspi-config nonint do_i2c 0
sudo apt-get install -y i2c-tools

# libraries to interface with the ADC and IMU respectivly
yes | sudo pip3 install adafruit-circuitpython-ads1x15
yes | sudo pip3 install adafruit-circuitpython-mpu6050

# library to generate nice pwm for the servos and motors
sudo apt-get install -y pigpio python-pigpio python3-pigpio

# the communication library we use
yes | sudo pip3 install UDPComms

# VPN which will hopefully allow us access across the internet
curl -s https://install.zerotier.com | sudo bash

# installs the .service scripts
for file in *.service; do
    [ -f "$file" ] || break
    sudo ln -s $FOLDER/$file /lib/systemd/system/
done

sudo systemctl daemon-reload
sudo systemctl enable monitor_battery # starts program on boot
sudo systemctl enable pigpiod # starts program on boot
sudo systemctl enable zerotier-one
