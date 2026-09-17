# Micro Programming Quiz

Each problem includes psuedo code to get you started. Psuedo code is the idea of how the code should work, not actual code.

## Starter Code

```python
import board
import digitalio
import analogio
import pwmio
import time


# Setup the pins for the pot, leds and buttons.
led1 = digitalio.DigitalInOut(board.GP14)
led1.direction = digitalio.Direction.OUTPUT
led2 = pwmio.PWMOut(board.GP15, frequency=1000)

button1 = digitalio.DigitalInOut(board.GP13)
button1.switch_to_input(pull=digitalio.Pull.DOWN)

potentiometer = analogio.AnalogIn(board.GP26)
ldr = analogio.AnalogIn(board.GP27)

# Create the variables

previousButton1State = button1.value

# This is the variable that will change when we press the button.
myMode1 = False

while True:
    currentButton1State = button1.value
    if currentButton1State != previousButton1State:
        # print statements like these can be seen in the serial terminal
        # print('yes')
        if not currentButton1State:
            myMode1 = not myMode1
            print('myMode1 =', myMode1)
            print("ldr.value")
        else:
            print("down")
    previousButton1State = currentButton1State
    led1.value = myMode1
    # print("led1 = ", led1.value)
    # This line sets the PWM (pulse width modulation) to the potentiometer value.
    led2.duty_cycle = potentiometer.value
```

## Links

- [Python 1](../programming_intro/python_lesson.md)
- [Python 2](../programming_2/programming_02.md)
- [Microcontroller 1](../microcontroller_intro/microcontroller_intro.md)
- [Microcontroller 2](../microcontroller_two/)

## Problem One

An LED gets brighter as the room gets darker.

```python

pwm.dutycycle = lightsensor.value

```

## Problem Two

Make an LED slowly fade in and out.

```python

ledBrightness = 0
ledDirection = 1
maxBrightness = 6000

while True:
    led.dutycycle = ledBrightness
    ledBrightness = ledBrightness + ledDirection
    time.sleep(.05)

    # Can you tell what this does:
    if ledBrightness >= maxBrightness OR ledBrightness <= 0:
        ledDirection = ledDirection x -1
    time.sleep(.02)

```

## Problem Three

An LED turns on when the room get dark. The level of darkness required to turn on the LED may be adjusted with a potentiometer.

You will need the _simplemath_ library on your pico. Instructions are in this file [microcontroller_intro](./microcontroller_intro.md) and the library is here [libraries folder](03_libraries).

```python

import adafruit_simplemath
from adafruit_simplemath import map_unconstrained_range

potValue = 0
lightValue = 0

while True:
    potValue = potentiometer.value
    lightValue = lightsensor.value

    # this takes the potentiometers value range and makes it 1-100
    potValue  = map_unconstraned_range(potValue, 0, 65535, 1, 100)

    # you will need change the first two numbers to the high and low of your light sensor
    lightValue = map_unconstraned_range(lightValue, 330, 9056, 1, 100)

    if lightValue > potValue:
        led.value = True
    else
        led.value = False

```

## Problem four

On button press, an off LED becomes brighter in 6 steps. Each step being 3/4 of a second long.
The button will turn off the LED at any time.

```python

lightMode = False
brightnessValues = [200, 1000, 2000, 3000, 4000, 6000]
brightnessStep = 0
previousTime = 0

while True:
    check button to see if we need to change the lightMode

    if lightMode == True:

        # send the current brightness to the led. on the first run, brightnessValues[brightnessStep] = 200
        led.dutycycle = brightnessValues[brightnessStep]

        # change the current brightness if enough time has passed
        if enough time has passed: # See below for a reminder of how to do this
            brightnessStep += 1 # Move to the next brightess in the list
            if brightnessStep > 5:
                brightnessStep = 0

    else: # If the button has changed the lightMode to off
        led.dutycycle = 0
        brightnessStep = 0

```

### Keeping track of time

```python

previousTime = 0
interval = 1000

while True:
    currentTime = time.monotonic()

    if currentTime > previousTime + interval: # Syntax could be way off but you get the idea
        print(currentTime) # Prints every one second
        previousTime = currentTime
```

## Problem five

Two buttons. Pressing button1 changes the effect of Button2. Button2 will either, make an LED blink, or make the same LED 60% bright, or make the LED turn off.
(use touch sensor or two wires for the second button)

```

```
