# Emergent Objects
# Digital input/output

import time
import board
import digitalio

led = digitalio.DigitalInOut(board.D13)
led.switch_to_output()

buttonA = digitalio.DigitalInOut(board.BUTTON_A)
buttonA.switch_to_input(pull=digitalio.Pull.DOWN)

buttonB = digitalio.DigitalInOut(board.BUTTON_B)
buttonB.switch_to_input(pull=digitalio.Pull.DOWN)

switch = digitalio.DigitalInOut(board.SLIDE_SWITCH)
switch.direction = digitalio.Direction.INPUT
switch.pull = digitalio.Pull.UP

while True:
	if buttonA.value and buttonB.value:
	    led.value = True
	else:
		led.value = False

	if switch.value is True: # switch is to the left
		print("Switch is on.")
	else:
		print("Switch is off.")

	time.sleep(0.01)
