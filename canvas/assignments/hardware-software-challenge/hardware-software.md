# Hardware Software Challenge

A series of circuit building/programming challenges that build on each other.

1. Blink an LED.

```
LED on
sleep
LED off
sleep
```

2. Blink the LED without using _sleep_

```
check if CURRENT_TIME - LAST_TIME is greater than BLINK_TIME
  toggle LED
  LAST_TIME = CURRENT_TIME
```

3. Turn on the LED when a button is held down.

```
if BUTTON_TRUE
  LED_TRUE
else
  LED_FALSE
```

4. Toggle the LED when the button is pressed (or released). You may need to _debounce_ the button.
   On a microscopic level, the metal contacts of a button will _bounce_ of off each other when pressed together. The code is running so quickly that, it may register this bounce as multiple presses.
   For a simple project it maybe ok to introduce a tiny sleep

5. Blink a second LED while being able to toggle the first LED. Use a pin capable of PWM (Pulse Width Modulation).
6. Change the blink speed based on the value returned from a resistive sensor (eg. pot or light sensor).
7. Change the brightness of the blinking based on the value of a second resistive sensor.
