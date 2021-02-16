
import time
import pigpio

pi = pigpio.pi()

servo_pins = {1: 23, 2:24, 3:25, 4:8}
servo_pin = servo_pins[1]

try:
    while 1:
        time.sleep(1)
        pi.set_servo_pulsewidth(servo_pin, 1000)
        time.sleep(1)
        pi.set_servo_pulsewidth(servo_pin, 2000)
finally:
        pi.set_servo_pulsewidth(servo_pin, 0) # turns servo off
