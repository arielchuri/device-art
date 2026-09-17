
import digitalio
import analogio
import pwmio
import time
import board
import random

# LEDs
# on off led
led = digitalio.DigitalInOut(board.GP14)
led.direction = digitalio.Direction.OUTPUT
led.value = True
# PWM LED
led2 =pwmio.PWMOut(board.GP15, frequency=1000)
led2.duty_cycle = 0

# Inputs
# a button
button = digitalio.DigitalInOut(board.GP13)
button.direction = digitalio.Direction.INPUT
button.pull = digitalio.Pull.DOWN

# an analog input
sensor = analogio.AnalogIn(board.GP26)

# keep track of the states of the object
machine_state = False # Keeps track of if the machine is on or off.
button_pressed = False # To take action only once when the button is pressed

# Inside the while loop
while True:
    if button.value: # check if the button is pressed
        print('if')
        if button_pressed == False: # only take action once when the button is pressed
            machine_state = not machine_state
            button_pressed = True
    else:
        print('else')
        button_pressed = False # reset the button_pressed variable
    led.value = machine_state # update the LED
    print(button.value)
    # print(sensor.value)
    time.sleep(0.1)