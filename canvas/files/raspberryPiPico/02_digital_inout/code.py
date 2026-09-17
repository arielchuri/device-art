# Emergent Objects
# Digital input/output

import time
import board
import digitalio

# Make a variable for pin 13.
led = digitalio.DigitalInOut(board.D13)
# Set it to be in output.
led.switch_to_output()

# Create a variable for the button.
button = digitalio.DigitalInOut(board.BUTTON_A)
# Set it to be an input.
button.switch_to_input(pull=digitalio.Pull.DOWN)

while True:
    if button.value == True:  # button is pushed
        led.value = True
    else:
        led.value = False

    time.sleep(0.01)
