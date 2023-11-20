from time import sleep
from imu import MPU6050
from machine import Pin, I2C

# Shows Pi is on by turning on LED when plugged in
LED = Pin("LED", Pin.OUT)

i2c = I2C(0, sda=Pin(0), scl=Pin(1), freq=400000)
imu = MPU6050(i2c)


def dataGyro():
    while True:
        LED.toggle()
        ax = round(imu.accel.x, 2)
        ay = round(imu.accel.y, 2)
        az = round(imu.accel.z, 2)
        gx = round(imu.gyro.x, 2)
        gy = round(imu.gyro.y, 2)
        gz = round(imu.gyro.z, 2)
        tem = round(imu.temperature, 2)
        print(f"Gyro X: {gx}")
        print(f"Gyro Y: {gy}")
        print(f"Gyro Z: {gz}")
        print(f'Temp: {tem} C')
        print()
        sleep(1)


dataGyro()
