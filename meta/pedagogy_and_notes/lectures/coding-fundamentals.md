# Lecture: Coding Fundamentals

**Week:** 6
**Date:** Mar 9
**Duration:** ~45 minutes

## Learning Outcomes

This lecture supports the following learning outcomes:

- **LO 2 - Tools, Materials, Methods:** Write and debug basic Python code and create electronic circuits using microprocessors.

## Overview

This lecture deepens students' programming knowledge, introducing more advanced coding concepts needed for creating sophisticated interactive objects. Topics include loops, functions, lists, and state management for microcontroller applications.

## Key Topics

### Review: Programming Basics

#### What We Know
- Variables and data types
- Conditionals (if/else)
- While loops
- Digital input/output
- Basic program structure

#### Building Forward
- How these concepts enable complex behaviors
- Moving from simple to sophisticated interactions
- Writing maintainable code
- Debugging strategies

### Functions

#### Why Functions?
- Organize code into reusable chunks
- Make code readable and maintainable
- Reduce repetition (DRY principle)
- Enable abstraction
- Easier testing and debugging

#### Defining Functions
```python
def blink_led(pin, times, duration):
    """Blink an LED a specified number of times"""
    for i in range(times):
        pin.value = True
        time.sleep(duration)
        pin.value = False
        time.sleep(duration)

# Using the function
blink_led(led_pin, 5, 0.2)
```

#### Parameters and Return Values
- Passing information to functions
- Getting results back
- Default parameter values
- Scope and variable lifetime

### Lists and Iteration

#### Lists Basics
```python
led_pins = [board.GP15, board.GP16, board.GP17]
colors = ["red", "green", "blue"]
sensor_readings = [0, 0, 0, 0, 0]
```

#### For Loops
```python
# Iterate over list
for pin in led_pins:
    pin.value = True
    time.sleep(0.1)

# Iterate with index
for i in range(len(colors)):
    print(f"LED {i} is {colors[i]}")

# Enumerate for both
for index, color in enumerate(colors):
    print(f"{index}: {color}")
```

#### List Operations
- Append, insert, remove
- Indexing and slicing
- List comprehensions
- Length and membership

### State Management

#### What is State?
- Remembering information between loop iterations
- Tracking modes and behaviors
- Managing complex interactions
- Creating object "memory"

#### State Variables
```python
button_pressed = False
current_mode = 0
last_button_time = 0
counter = 0
is_active = True
```

#### State Machines
```python
mode = "idle"

while True:
    if mode == "idle":
        # Waiting for activation
        if button.value:
            mode = "active"
    elif mode == "active":
        # Do active behavior
        if not sensor.value:
            mode = "alert"
    elif mode == "alert":
        # Alert state
        if timeout_reached:
            mode = "idle"
```

### Timing Without Blocking

#### The Problem with time.sleep()
- Blocks all other code
- Can't respond to inputs during sleep
- Limits interactivity
- Poor user experience

#### Using time.monotonic()
```python
last_blink_time = 0
blink_interval = 0.5

while True:
    current_time = time.monotonic()

    # Check button without blocking
    if button.value:
        print("Button pressed!")

    # Blink LED without blocking
    if current_time - last_blink_time >= blink_interval:
        led.value = not led.value
        last_blink_time = current_time
```

### Analog Input and Sensors

#### Reading Analog Values
```python
import analogio

sensor = analogio.AnalogIn(board.A0)

while True:
    # Raw value (0-65535)
    raw_value = sensor.value

    # Convert to voltage
    voltage = (raw_value * 3.3) / 65535

    # Map to range (0-100)
    percentage = (raw_value / 65535) * 100
```

#### Sensor Applications
- Light sensors (photoresistors)
- Distance sensors
- Potentiometers for user input
- Temperature sensors
- Mapping sensor values to behaviors

### Debugging Techniques

#### Print Statements
```python
print(f"Sensor value: {sensor.value}")
print(f"Mode: {mode}, Counter: {counter}")
print(f"Button state: {button.value}")
```

#### Serial Monitor
- Viewing output in real-time
- Tracking program flow
- Inspecting variable values
- Understanding timing issues

#### Systematic Debugging
1. Reproduce the problem
2. Isolate the issue
3. Form a hypothesis
4. Test systematically
5. Fix and verify
6. Document the solution

### Code Organization

#### Structure for Clarity
```python
# Imports at top
import board
import digitalio

# Configuration and setup
LED_PIN = board.GP15
BLINK_RATE = 0.5

# Hardware initialization
led = digitalio.DigitalInOut(LED_PIN)
led.direction = digitalio.Direction.OUTPUT

# Helper functions
def blink_pattern():
    # Function code

# Main program
while True:
    # Main loop code
```

#### Comments and Documentation
- Explain why, not what
- Document complex logic
- Note assumptions and limitations
- Include usage examples
- Keep comments updated

## Practical Examples

### Multi-LED Sequencer
```python
leds = [led1, led2, led3, led4]
current_led = 0

while True:
    # Turn off all LEDs
    for led in leds:
        led.value = False

    # Turn on current LED
    leds[current_led].value = True

    # Move to next LED
    current_led = (current_led + 1) % len(leds)

    time.sleep(0.2)
```

### Button-Controlled Modes
```python
modes = ["off", "steady", "blink", "fade"]
current_mode = 0

while True:
    if button_pressed():
        current_mode = (current_mode + 1) % len(modes)

    if modes[current_mode] == "off":
        led.value = False
    elif modes[current_mode] == "steady":
        led.value = True
    # etc.
```

### Sensor-Responsive Behavior
```python
def map_range(value, in_min, in_max, out_min, out_max):
    return (value - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

while True:
    sensor_value = sensor.value
    brightness = map_range(sensor_value, 0, 65535, 0, 65535)
    led.duty_cycle = int(brightness)
```

## Key Questions

- When should you create a function?
- How do you maintain state across loop iterations?
- Why is blocking code (time.sleep) problematic?
- How do you structure code for readability?
- What debugging strategies work best?
- How do you map sensor values to meaningful ranges?

## Demonstrations

### Live Coding Session
1. **Refactor simple code** - Show before/after with functions
2. **Multi-LED pattern** - Using lists and loops
3. **State machine** - Mode switching example
4. **Non-blocking blink** - Compare to time.sleep()
5. **Sensor input** - Reading and mapping analog values
6. **Debugging walkthrough** - Fix a buggy program

## Activities

### Following Workshop: Soldering Intro
- Learn soldering techniques
- Permanent circuit connections
- Safety and best practices
- Preparing components for projects

### Following Demo: Sensors & Input
- Hands-on with various sensors
- Reading analog inputs
- Mapping sensor values
- Creating sensor-responsive behaviors

## Common Challenges

### Conceptual
- Understanding scope
- State management complexity
- Non-blocking timing
- List indexing
- Function design

### Technical
- Syntax errors
- Logic errors
- Timing issues
- Sensor noise and variability
- Memory limitations on microcontroller

### Problem-Solving Approaches
- Break problems into smaller steps
- Test each piece independently
- Use serial output to understand flow
- Consult documentation and examples
- Ask specific questions
- Iterate and refine

## Connections to Course

- Builds on Python App and basic programming
- Essential for complex Final Project interactions
- Enables sophisticated object behaviors
- Supports sensor integration
- Foundation for responsive design
- Prepares for Advanced Code Loops (Week 9)

## Resources

### Documentation
- CircuitPython core modules
- Python language reference
- Sensor library documentation
- Code examples collection

### Course Materials
- programming_2 directory
- analogin directory
- State machine examples
- Sensor code examples

### Learning Resources
- Python tutorials
- CircuitPython guides
- Debugging checklists
- Code pattern library

## Assessment

Students demonstrate understanding through:
- More sophisticated Final Project code
- Use of functions and organization
- State management in objects
- Sensor integration
- Code quality and documentation
- Problem-solving in workshops

## Tips for Teaching

- Live code whenever possible - show the process
- Make mistakes intentionally and debug them
- Start simple, add complexity incrementally
- Use analogies for abstract concepts
- Show multiple ways to solve problems
- Emphasize that coding is a craft skill
- Encourage experimentation
- Provide code templates and examples
- Make debugging strategies explicit
- Connect to student project needs
- Balance theory with practical application
- Celebrate working code, even if imperfect
- Remind students that Googling and consulting docs is normal
- Build confidence through small successes
