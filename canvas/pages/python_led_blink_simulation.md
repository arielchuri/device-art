# Emulating the LED Blink in Pure Python (Before Hardware)

Before wiring a single electronic component or touching the Raspberry Pi Pico, we can write and run the core control logic in pure Python on your laptop. 

Hardware computing is simply software logic translated into electrical voltage. By understanding the loop, timing, and state mechanics in the terminal first, troubleshooting physical circuits later becomes significantly faster.

---

## 1. The Core Computational Model of an LED

An LED is a binary output device. It exists in one of two states:
- **`True` / `1` / `HIGH`**: Pin delivers **3.3V** $\to$ LED illuminates.
- **`False` / `0` / `LOW`**: Pin connects to **0V (GND)** $\to$ LED turns off.

To make an LED blink repeatedly, the program requires four fundamental computational elements:
1. A **state variable** to track whether the light is currently on or off.
2. An **inversion operation** (`not`) to flip the state.
3. A **timing delay** (`time.sleep`) to hold each state long enough for human perception.
4. An **infinite loop** (`while True`) to keep the sequence repeating continuously.

---

## 2. Level 1: Basic Terminal Blink (Sequential Output)

Create a new file on your computer named `blink_sim.py` and run it in your terminal (`python3 blink_sim.py`):

```python
# blink_sim.py - Terminal LED Simulation
import time

# 1. State variable
led_state = False

print("Starting Terminal LED Blink Simulation (Press Ctrl+C to stop)...\n")

# 2. Infinite execution loop
while True:
    # 3. Toggle the boolean state (False becomes True, True becomes False)
    led_state = not led_state
    
    if led_state:
        print("[ ON  ] 3.3V HIGH - Current flowing through diode")
    else:
        print("[ OFF ] 0.0V LOW  - No current")
    
    # 4. Hold state for half a second
    time.sleep(0.5)
```

### Try This in the Terminal:
- Change `time.sleep(0.5)` to `time.sleep(0.1)` for a rapid strobe.
- Change the sleep duration to create asymmetric timing (e.g., short pulse `0.1s`, long dark `0.9s`).

---

## 3. Level 2: Animated In-Place Terminal Indicator

Instead of printing thousands of lines downward, we can use the carriage return character `\r` to update the terminal line in place, mimicking a physical blinking indicator on your screen:

```python
# blink_animated.py - In-place terminal animation
import time
import sys

led_state = False

print("Simulating Hardware Indicator (Press Ctrl+C to exit):")

while True:
    led_state = not led_state
    
    if led_state:
        sys.stdout.write("\r[ ● ON  ] 3.3V (GP14) ")
    else:
        sys.stdout.write("\r[ ○ OFF ] 0.0V (GP14) ")
    
    sys.stdout.flush()
    time.sleep(0.5)
```

---

## 4. Level 3: Non-Blocking Multitasking Blink (`time.monotonic`)

### The Problem with `time.sleep()`
`time.sleep()` is **blocking**. While the computer is sleeping, it cannot listen for button clicks, read sensor voltages, or respond to network requests.

### The Non-Blocking Solution (Time Arithmetic)
Instead of putting Python to sleep, we keep the loop spinning at maximum speed and check the elapsed clock time using `time.monotonic()`:

```python
# blink_nonblocking.py - Non-blocking timer arithmetic
import time

led_state = False
interval = 0.5  # Toggle every 0.5 seconds
previous_time = time.monotonic()

print("Non-blocking loop running at full speed (checking clock continuously)...")

while True:
    current_time = time.monotonic()
    
    # Has half a second elapsed since our last toggle?
    if current_time - previous_time >= interval:
        previous_time = current_time
        led_state = not led_state
        print(f"Timestamp: {current_time:.2f}s | LED: {'● ON' if led_state else '○ OFF'}")
    
    # The CPU is free to run other instructions here instantly!
    # (e.g. checking if a button was pressed)
```

---

## 5. From Terminal Code to Physical Microcontroller

Notice how minimal the change is when we move this exact Python logic to the **Raspberry Pi Pico**:

| Pure Python (Terminal) | CircuitPython (Raspberry Pi Pico) |
| :--- | :--- |
| `led_state = True` | `led.value = True` |
| `led_state = False` | `led.value = False` |
| `led_state = not led_state` | `led.value = not led.value` |
| `time.sleep(0.5)` | `time.sleep(0.5)` |
| `time.monotonic()` | `time.monotonic()` |

Next step: Follow the [VS Code & CircuitPython Setup Guide](vscode_circuitpython_setup.md) to connect your Pico and run this logic on physical hardware.
