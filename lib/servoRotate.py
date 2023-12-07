from servo import Servo
import utime

pwmPin = 15  # change for your pin
motor = Servo(pwmPin)


def rotateServo():
    while True:
        print('Servo is working...')
        utime.sleep(1)
        motor.move(45)
        utime.sleep(1)
        motor.move(180)
        print('Servo is not working...')