# Digital In Out

The file [code.py](microcontroller_intro/03_digital_inout/code.py) contains a simple program that lights an LED when a button is pressed. [code_simpler.py](code_simpler.py) and [code_simpleryet.py](code_simpleryet.py) are simplified versions of this program that achieve the same result.

The code in [code_button_switch.py](code_button_switch.py) lights the LED if both buttons are pressed and outputs text for the position of the switch.

Can you edit the code so that the position of the switch determines which button lights the LED?

Here is one way to do it. Can you find another?:

```
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
	if switch.value:
		led.value = buttonA.value
	else:
		led.value = buttonB.value

	time.sleep(0.01)
```
