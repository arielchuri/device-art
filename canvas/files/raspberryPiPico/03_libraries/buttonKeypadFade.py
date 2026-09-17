import board
import digitalio
from digitalio import DigitalInOut, Direction, Pull
import analogio
import pwmio
import time
import keypad

led = digitalio.DigitalInOut(board.GP14)
led.direction = digitalio.Direction.OUTPUT
keys = keypad.Keys((board.GP13,), value_when_pressed=False, pull=True)

potentiometer = analogio.AnalogIn(board.GP26)
led2 = pwmio.PWMOut(board.GP15, frequency=1000)

led.value = False

while True:
    #print(potentiometer.value)
    led2.duty_cycle = potentiometer.value

    event = keys.events.get()
    # event will be None if nothing has happened.
    if event:
        print(event.key_number)
        if event.key_number == 0 and event.released == True:
            led.value = not led.value
            print(led.value)
