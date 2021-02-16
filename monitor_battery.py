
import time

import board
import busio
import adafruit_ads1x15.ads1015 as ADS
from adafruit_ads1x15.analog_in import AnalogIn

i2c = busio.I2C(board.SCL, board.SDA)
ads = ADS.ADS1015(i2c, gain=2/3)
chan = AnalogIn(ads, ADS.P1)

with open('/sys/class/leds/led0/trigger', 'wb', buffering=0) as trigger:
    trigger.write(b'none') # turn off default behaviour (SD card activity)

led = open('/sys/class/leds/led0/brightness', 'wb', buffering=0)

while True:
    if chan.voltage > 4.1:
        # fully charged - solid
        led.write(b'1')
        time.sleep(5)
    elif chan.voltage > 3.3:
        # normal opperation - slow blink
        for _ in range(3):
            led.write(b'0')
            time.sleep(1)
            led.write(b'1')
            time.sleep(1)
    else:
        # needs charging - fast blink
        for _ in range(25):
            led.write(b'0')
            time.sleep(0.1)
            led.write(b'1')
            time.sleep(0.1)
