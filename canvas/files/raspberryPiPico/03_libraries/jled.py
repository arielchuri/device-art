import board
import digitalio
from digitalio import DigitalInOut, Direction, Pull
import analogio
import pwmio
import time
import keypad
from jled import JLed

led1 = digitalio.DigitalInOut(board.GP14)
led1.direction = digitalio.Direction.OUTPUT

led3 = JLed(board.GP16).breathe(2000).min_brightness(20).forever()

keys = keypad.Keys((board.GP13,), value_when_pressed=False, pull=True)

potentiometer = analogio.AnalogIn(board.GP26)
led2 = pwmio.PWMOut(board.GP15, frequency=1000)

led1.value = False

while True:
    #print(potentiometer.value)
    led2.duty_cycle = potentiometer.value

    event = keys.events.get()
    # event will be None if nothing has happened.
    if event:
        print(event.key_number)
        if event.key_number == 0 and event.released == True:
            led1.value = not led1.value
            #print(led.value)


    led3.update()
