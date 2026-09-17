# My First Object

## Asignment objectives

- [ ] Set up your development environment. Can you program your microcontroller?
- [ ] See data in the _Serial Port Monitor_.
- [ ] Be able to multitask with _Circuit Python_. Blink an **LED** without using _time.sleep_ and toggle a button.
- [ ] Understand the code.

## Breadboard

The following steps assume you have a breadboard set up with your _Raspberry PI PICO_. PI should be powering the breadboard with PIN 36 for power and one of the ground pins (3 and or 38).

Compare the (breadboard)[breadboard.png] illustration and (schematic)[schematic.png] diagram below. Can you see how they are the same?

Set up your breadboard to have the same connections. 
The parts do not need to be in the same place.

Notice the LED that is not connected to the _PICO_. This **LED** will always be on as long as the board is powered correctly.

![](raspberry-pi-pico-pinout.png)

![](breadboard.png)

![](schematic.png)

## Hello World

Upload the following code to your PICO. Do you see the output in the _Serial Port Monitor_.

```python
# Lines that start like this are comments. The PICO ignores them.
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

# Inside the while loop
while True:
    print('Hello, world!')
```

## Blinky

Can you understand what it should do before you try it?

```python
# < pin setup from above remains the same >

while True:
    if button.value: # check if the button is pressed
        print('Button Pressed')
        led.value = True
        led2.duty_cycle = 30000
        time.sleep(.25)
        led.value = False
        led2.duty_cycle = 60000
        time.sleep(.25)
        print(sensor.value)
```

## Toggle State

Lets toggle a state. 

```python
# < LED, Sensor, and Button Set up go here. >

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
    print(machine_state)
```

## Blink Without Sleep

If we want to blink an LED without using the _time.sleep_ command, we must keep track of the time.

```python
# < LED, Sensor, and Button Set up go here. >

# How long we want the LED to stay on
BLINK_ON_DURATION = 0.1

# How long we want the LED to stay off
BLINK_OFF_DURATION = 0.5

# When we last changed the LED state
LAST_BLINK_TIME = -1

# Inside the while loop
while True:
    # Store the current time to refer to later.
    now = time.monotonic()
    if not led.value: # if the LED is off
        # Is it time to turn on?
        if now >= LAST_BLINK_TIME + BLINK_OFF_DURATION:
            led.value = True
            LAST_BLINK_TIME = now
    if led.value: # If the LED is on
        # Is it time to turn off?
        if now >= LAST_BLINK_TIME + BLINK_ON_DURATION:
            led.value = False
            LAST_BLINK_TIME = now
```

## Blink Only When the Machine is On.

```python
# < LED, Sensor, and Button Set up go here. >

machine_state = False # Keeps track of if the machine is on or off.
button_pressed = False # To take action only once when the button is pressed

# How long we want the LED to stay on
BLINK_ON_DURATION = 0.1

# How long we want the LED to stay off
BLINK_OFF_DURATION = 0.5

# When we last changed the LED state
LAST_BLINK_TIME = -1

# Inside the while loop
while True:
    # Store the current time to refer to later.
    now = time.monotonic()

    if button.value: # check if the button is pressed
        if button_pressed == False: # only take action once when the button is pressed
            machine_state = not machine_state
            button_pressed = True
    else:
        button_pressed = False # reset the button_pressed variable

    if machine_state:
        if not led.value: # if the LED is off
            # Is it time to turn on?
            if now >= LAST_BLINK_TIME + BLINK_OFF_DURATION:
                led.value = True
                LAST_BLINK_TIME = now
        if led.value: # If the LED is on
            # Is it time to turn off?
            if now >= LAST_BLINK_TIME + BLINK_ON_DURATION:
                led.value = False
                LAST_BLINK_TIME = now
        led2.duty_cycle = sensor.value
    else:
        led.value = False
        led2.duty_cycle = 0
```

## Using Sensor Data

Can you add this code in to change the blink speed based on the sensor?
The sensor values may need to be changed for your lighting situation.

```python
        if sensor.value >= 55000:
            BLINK_ON_DURATION = .05
            BLINK_OFF_DURATION = .05
        elif sensor.value < 55000:
            BLINK_ON_DURATION = .5
            BLINK_OFF_DURATION = .5
```
