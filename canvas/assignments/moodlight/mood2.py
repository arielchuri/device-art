import time
import board
import adafruit_lis3dh
import busio
import neopixel
import random

pixels = neopixel.NeoPixel(board.NEOPIXEL, 10, auto_write=False)

#code for accelerometer
i2c = busio.I2C(board.ACCELEROMETER_SCL, board.ACCELEROMETER_SDA)
lis3dh = adafruit_lis3dh.LIS3DH_I2C(i2c, address=0x19)
lis3dh.range = adafruit_lis3dh.RANGE_8_G

#variables for the Neopixels
xLed = 0
yLed = 0
zLed = 0

x, y, z = lis3dh.acceleration

#prints the x, y, and z coordinates of the accelerometer
def accelerom():
    while True:
        x, y, z = lis3dh.acceleration
        print((x, y, z))
        time.sleep(.5)
        break

def transaccel(n):
    return int((n*12)+128))
    break

#calls back to all the functions
while True:
    x, y, z = lis3dh.acceleration
    print(int((x*12)+128))
    transaccel(x)
    print(n)
    pixels.fill((0,0,int((x*12)+118)))

    # Gives a number from -1 to 18
    # print(int(x+16/2))
    pixels.show()
    # xx()
    # xxx()
    # yy()
    # yyy()
    # zz()
    # zzz()
    # light()
