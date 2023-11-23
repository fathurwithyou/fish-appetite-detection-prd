from time import sleep
from imu import MPU6050
from machine import Pin, I2C
from servoRotate import rotateServo

# Shows Pi is on by turning on LED when plugged in
LED = Pin("LED", Pin.OUT)

i2c = I2C(0, sda=Pin(0), scl=Pin(1), freq=400000)
imu = MPU6050(i2c)

displacement = []


def dataGyro():
    while True:
        rotateServo()
        abs_gx = abs_gy = abs_gz = 0
        for i in range(10):
            ax = round(imu.accel.x, 2)
            ay = round(imu.accel.y, 2)
            az = round(imu.accel.z, 2)
            gx = round(imu.gyro.x, 2)
            gy = round(imu.gyro.y, 2)
            gz = round(imu.gyro.z, 2)
            displacement.append([gx, gy, gz])
            abs_gx += abs(gx)
            abs_gy += abs(gy)
            abs_gz += abs(gz)
            sleep(0.5)
        
        print(f'\nAbsolute Displacement X: {abs_gx}')
        print(f'Absolute Displacement Y: {abs_gy}')
        print(f'Absolute Displacement Z: {abs_gz}')
        print(f'Euclidean Distance: {(abs_gx**2+abs_gy**2+abs_gz**2)**0.5}\n')


dataGyro()
