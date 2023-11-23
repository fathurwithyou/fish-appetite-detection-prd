from servo import Servo
import utime

pwmPin = 15  # change for your pin
motor = Servo(pwmPin)


def rotateServo():
    print('Servo is working...')
    motor.move(45)
    utime.sleep(1)
    motor.move(180)
    print('Servo is not working...')

rotateServo()
