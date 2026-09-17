# Raspberry Pi Pico & CircuitPython Cheat Sheet

---

## 1. Hardware Architecture & Pin Overview

The Raspberry Pi Pico operates at **3.3V logic** powered by the RP2040 microcontroller.

- **Power Pins**:
  - `VBUS` (Pin 40): 5V direct from USB.
  - `VSYS` (Pin 39): Main system power input (1.8V to 5.5V).
  - `3V3(OUT)` (Pin 36): Regulated 3.3V power output to breadboard power rail.
  - `GND` (Pins 3, 8, 13, 18, 23, 28, 33, 38): Ground connections.
- **GPIO Pins**: `GP0` through `GP22`, `GP26` through `GP28` (3.3V logic level).
- **Analog Pins (ADC)**: `GP26` (ADC0), `GP27` (ADC1), `GP28` (ADC2). 16-bit range in CircuitPython (`0` to `65535`).

---

## 2. Setting Up the Pico with CircuitPython

1. Hold down the white **BOOTSEL** button on the Pico.
2. Plug the USB cable into your computer, then release BOOTSEL.
3. The Pico mounts as a storage drive named `RPI-RP2`.
4. Drag and drop the CircuitPython `.uf2` file onto `RPI-RP2`.
5. The board reboots automatically and mounts as a USB drive named `CIRCUITPY`.
6. Edit `code.py` on the `CIRCUITPY` drive using VS Code or Mu Editor. The code executes automatically on save.

---

## 3. Core CircuitPython Code Snippets

### A. Digital Output (LED Control)

```python
import board
import digitalio
import time

# Configure GP14 as an output pin
led = digitalio.DigitalInOut(board.GP14)
led.direction = digitalio.Direction.OUTPUT

while True:
    led.value = True   # Turn ON (3.3V)
    time.sleep(0.5)
    led.value = False  # Turn OFF (0V)
    time.sleep(0.5)
```

---

### B. Digital Input (Pushbutton with Internal Pull-Down Resistor)

```python
import board
import digitalio
import time

# Configure GP13 as input with internal pull-down
button = digitalio.DigitalInOut(board.GP13)
button.direction = digitalio.Direction.INPUT
button.pull = digitalio.Pull.DOWN

led = digitalio.DigitalInOut(board.GP14)
led.direction = digitalio.Direction.OUTPUT

while True:
    if button.value:
        led.value = True
    else:
        led.value = False
    time.sleep(0.01)
```

---

### C. Analog Input (Potentiometer / Light Sensor)

```python
import board
import analogio
import time

# Configure ADC0 (GP26)
pot = analogio.AnalogIn(board.GP26)

while True:
    # pot.value returns 0 to 65535
    voltage = (pot.value * 3.3) / 65535
    print(f"Raw: {pot.value} | Voltage: {voltage:.2f}V")
    time.sleep(0.1)
```

---

### D. PWM Output (LED Dimming / Brightness Control)

```python
import board
import pwmio
import time

# Configure GP15 for PWM output at 1kHz
pwm_led = pwmio.PWMOut(board.GP15, frequency=1000)

while True:
    # Duty cycle ranges from 0 (0%) to 65535 (100%)
    for duty in range(0, 65536, 1000):
        pwm_led.duty_cycle = duty
        time.sleep(0.01)
    for duty in range(65535, -1, -1000):
        pwm_led.duty_cycle = duty
        time.sleep(0.01)
```

---

### E. Addressable LEDs (NeoPixel RGB)

```python
import board
import neopixel
import time

# Requires neopixel.py in /lib on CIRCUITPY
num_pixels = 8
pixels = neopixel.NeoPixel(board.GP16, num_pixels, brightness=0.2, auto_write=True)

# Color tuples: (Red, Green, Blue) from 0 to 255
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

while True:
    pixels.fill(RED)
    time.sleep(1)
    pixels.fill(GREEN)
    time.sleep(1)
    pixels.fill(BLUE)
    time.sleep(1)
```

---

### F. I2C Display (SSD1306 128x64 OLED)

```python
import board
import busio
import displayio
import terminalio
from adafruit_display_text import label
import adafruit_displayio_ssd1306

displayio.release_displays()

# I2C configuration: SCL = GP15, SDA = GP14
i2c = busio.I2C(board.GP15, board.GP14)
display_bus = displayio.I2CDisplay(i2c, device_address=0x3C)
display = adafruit_displayio_ssd1306.SSD1306(display_bus, width=128, height=64)

# Render text
splash = displayio.Group()
text_area = label.Label(terminalio.FONT, text="Device Art", color=0xFFFF00, x=10, y=28)
splash.append(text_area)
display.root_group = splash

while True:
    pass
```

---

## 4. Installing Libraries on `CIRCUITPY`

1. Open the `CIRCUITPY` drive on your computer.
2. Ensure there is a folder named `lib`.
3. Copy the required `.py` or `.mpy` files (e.g. `neopixel.py`, `adafruit_simplemath.mpy`) directly into the `lib` folder.
4. Reference the library in `code.py` using `import <library_name>`.
