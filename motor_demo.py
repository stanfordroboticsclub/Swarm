
import time
import pigpio

pi = pigpio.pi()

motor_pins = {"left": (17,27), "right": (9, 10)}
motor = motor_pins['left']


try:
    while 1:
        pi.set_PWM_dutycycle( motor[0], 0 )
        pi.set_PWM_dutycycle( motor[1], 200 ) # 255 is max value
        time.sleep(3)

        pi.set_PWM_dutycycle( motor[0], 200 ) # 255 is max value
        pi.set_PWM_dutycycle( motor[1], 0 )
        time.sleep(3)
finally:
        pi.set_PWM_dutycycle( motor[0], 0 ) # stop motor on program exit
        pi.set_PWM_dutycycle( motor[1], 0 )

