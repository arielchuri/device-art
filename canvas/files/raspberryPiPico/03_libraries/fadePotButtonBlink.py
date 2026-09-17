# SPDX-FileCopyrightText: 2021 Kattni Rembor for Adafruit Industries
#
# SPDX-License-Identifier: MIT

"""
Button and LED example for Pico. Turns on LED when button is pressed.

REQUIRED HARDWARE:
* Button switch on pin GP13.
* LED on pin GP14.
"""
import board
import digitalio
import analogio
import pwmio
import time

led = digitalio.DigitalInOut(board.GP14)
led.direction = digitalio.Direction.OUTPUT
button = digitalio.DigitalInOut(board.GP13)
button.switch_to_input(pull=digitalio.Pull.DOWN)

potentiometer = analogio.AnalogIn(board.GP26)
led2 = pwmio.PWMOut(board.GP15, frequency=1000)

while True:
    print(potentiometer.value)
    time.sleep(0.05)
    led.value = button.value
    led2.duty_cycle = potentiometer.value
