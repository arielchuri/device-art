import digitalio
from digitalio import DigitalInOut, Direction, Pull
from analogio import AnalogOut
import pwmio
import time
import board
import random

# LEDs
led = digitalio.DigitalInOut(board.GP14)
led.direction = digitalio.Direction.OUTPUT
led2 =pwmio.PWMOut(board.GP15, frequency=1000)
led2.duty_cycle = 0

LAST_FADE_TIME = -1
FADE_SPEED = .005
FADE_DIR = 64

# Simulate LED blinking with a custom blink pattern
blink_pattern = [0.8,0.01, 0.1,0.01,0.1,0.01]  # Custom blink pattern intervals
last_change_time = time.monotonic()  # Initialize the last LED state change time
pattern_index = 0  # Initialize the index for cycling through the blink pattern
interval = blink_pattern[0]

# Function to check if it's time to change the LED state based on the blink pattern
def is_time_to_change_led(last_change_time, interval):
    return time.monotonic() - last_change_time >= interval

def run_led(last_change_time, interval, pattern_index):
    if is_time_to_change_led(last_change_time, interval):
        led.value = not led.value 
        # Update the last LED state change time
        last_change_time = time.monotonic()
        # Move to the next interval in the blink pattern
        pattern_index += 1
        interval = blink_pattern[pattern_index % len(blink_pattern)]
    return last_change_time, pattern_index, interval

def fade_led(led, fade_speed, fade_dir, last_fade_time):
    if time.monotonic() >= last_fade_time + fade_speed:
        led2.duty_cycle = max(min(led2.duty_cycle + fade_dir, 40000), 0)
        if led2.duty_cycle >= 40000 or led2.duty_cycle <= 0:
            fade_dir = -fade_dir  # Reverse the direction
        last_fade_time = time.monotonic()
    return last_fade_time, fade_dir

# Inside the while loop
while True:
    # Get the interval from the blink pattern based on the current index
    # Check if it's time to change the LED state
    last_change_time, pattern_index, interval = run_led(last_change_time, interval, pattern_index)
    
    LAST_FADE_TIME, FADE_DIR = fade_led(led, FADE_SPEED, FADE_DIR, LAST_FADE_TIME)
    # time.sleep(0.1)  # Simulate other operations