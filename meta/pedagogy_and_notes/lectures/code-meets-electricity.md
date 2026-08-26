# Lecture: Code Meets Electricity

**Week:** 4
**Date:** Feb 23
**Duration:** ~45 minutes

## Learning Outcomes

This lecture supports the following learning outcomes:

- **LO 2 - Tools, Materials, Methods:** Write and debug basic Python code and create electronic circuits using microprocessors.
- **LO 3 - Experimentation:** Play with the concept of a "fantastic object" and experiment with non-traditional human-object interactions through play and discovery.

## Overview

This lecture bridges the gap between software and hardware, introducing microcontrollers and showing students how to use Python code to control physical electronic components. This is where their programming skills meet their circuit knowledge to create interactive objects.

## Key Topics

### What is a Microcontroller?

#### Definition and Purpose
- Small computer on a single chip
- Designed for embedded applications
- Combines processor, memory, and I/O
- Different from general-purpose computers
- Real-world applications and examples

#### The Raspberry Pi Pico
- Overview of the board and specifications
- RP2040 chip architecture
- GPIO pins (General Purpose Input/Output)
- Power requirements (USB or external)
- CircuitPython and MicroPython support
- Why we chose this platform

### GPIO Pins

#### Understanding Pins
- Digital pins (on/off, high/low, 1/0)
- Analog input pins (reading variable voltages)
- PWM (Pulse Width Modulation) output
- Power pins (3.3V, GND)
- Special function pins (I2C, SPI, UART)

#### Pin Numbering
- Physical pin numbers vs GPIO numbers
- Pico pinout diagram
- How to reference pins in code
- Finding information in documentation

### Digital Output: Blinking an LED

#### The Classic "Hello World" of Hardware
- Connecting LED to GPIO pin
- Current-limiting resistor calculation
- Writing code to turn LED on/off
- Using time.sleep() for timing
- The blink pattern as communication

#### Code Structure
```python
import board
import digitalio
import time

led = digitalio.DigitalInOut(board.GP15)
led.direction = digitalio.Direction.OUTPUT

while True:
    led.value = True   # LED on
    time.sleep(0.5)
    led.value = False  # LED off
    time.sleep(0.5)
```

### Digital Input: Reading Buttons

#### Button Basics
- How buttons work (making/breaking connections)
- Pull-up and pull-down resistors (why we need them)
- Reading button state in code
- Debouncing (dealing with switch bounce)
- Button press vs button hold

#### Code Example
```python
import board
import digitalio

button = digitalio.DigitalInOut(board.GP14)
button.direction = digitalio.Direction.INPUT
button.pull = digitalio.Pull.UP  # Use internal pull-up

while True:
    if not button.value:  # Button pressed (pulls to ground)
        print("Button pressed!")
```

### Combining Input and Output

#### Interactive Circuits
- Button controls LED
- Multiple buttons, multiple LEDs
- State machines and logic
- Event-driven programming patterns
- Creating responsive behaviors

#### Code Logic
- If/else statements for control
- While loops for continuous operation
- Variables to track state
- Functions for organization

### PWM for LED Brightness

#### What is PWM?
- Rapidly turning pin on/off
- Duty cycle determines "brightness"
- Frequency considerations
- Limitations and applications

#### Fading LED Example
```python
import board
import pwmio
import time

led = pwmio.PWMOut(board.GP15, frequency=5000, duty_cycle=0)

while True:
    # Fade up
    for i in range(0, 65535, 256):
        led.duty_cycle = i
        time.sleep(0.01)
    # Fade down
    for i in range(65535, 0, -256):
        led.duty_cycle = i
        time.sleep(0.01)
```

### From Circuits to Objects

#### Making Things Interactive
- Input → Processing → Output
- Creating object behaviors
- Responsive vs autonomous objects
- Feedback loops
- Emergent behaviors from simple rules

#### Design Considerations
- What inputs make sense for your object?
- What outputs communicate effectively?
- How should the object respond?
- What personality does the object have?
- How does interaction serve your concept?

## Key Questions

- How does code control electricity?
- What's the difference between digital and analog?
- Why do we need resistors with LEDs controlled by microcontrollers?
- How do you map physical interactions to code logic?
- What kinds of object behaviors can you create?
- How do you troubleshoot when code and circuits interact?

## Demonstrations

### Live Coding
1. **Basic LED blink** - Show complete setup
2. **Button reading** - Demonstrate serial monitor
3. **Button-controlled LED** - Interactive system
4. **PWM fading** - Analog output effect
5. **Multiple LEDs pattern** - Sequencing
6. **Troubleshooting** - Common errors and fixes

### Hardware Setup
- Proper breadboard layout
- Wire management
- Power connections
- USB programming connection
- Serial debugging

## Activities

### Following Workshop: Blinking LEDs with Code
- Students write and upload their first program
- Connect LED circuits to Pico
- Experiment with timing and patterns
- Add button control
- Create simple interactive behaviors

### Wiring Workshop
- Best practices for breadboard circuits
- Wire color conventions
- Organizing complex circuits
- Strain relief and stability
- Planning for enclosures

## Common Challenges

### Technical Issues
- Wrong pin numbers
- Reversed polarity
- Forgot resistors
- Code syntax errors
- Import errors
- Board not recognized

### Conceptual Challenges
- Understanding pull-up/down resistors
- Inverting logic (active low)
- Timing and delays
- State management
- Mapping ideas to code

### Troubleshooting Process
1. Check physical connections
2. Verify code syntax
3. Test components individually
4. Use serial print statements
5. Simplify to smallest working example
6. Check documentation and examples

## Connections to Course

- Builds on Python App (Week 3)
- Builds on Circuit Plan (Week 4)
- Foundation for all interactive projects
- Critical for Final Project
- Enables object behaviors and personality
- Bridges concept and implementation

## Resources

### Documentation
- CircuitPython documentation
- Raspberry Pi Pico pinout
- Component datasheets
- Code examples library

### Course Materials
- microcontroller_intro directory
- Example code repository
- Pin reference charts
- Troubleshooting guides

### Online Resources
- Adafruit Learning System
- CircuitPython libraries
- Community forums
- Video tutorials

## Assessment

Students demonstrate understanding through:
- Successful LED blink program
- Interactive button-LED circuit
- Wiring workshop participation
- Object Sketches assignment (integrating interactivity)
- Progress toward Final Project functionality

## Tips for Teaching

- Start with the absolute simplest example
- Show the code AND the physical result together
- Use serial output liberally for debugging
- Build complexity gradually
- Expect technical difficulties - build in troubleshooting time
- Have working backup hardware
- Show your own debugging process
- Celebrate when LEDs first light up
- Connect physical computing to larger design goals
- Emphasize that this is a tool for making objects, not just circuits
- Relate pin control to everyday objects (doorbells, thermostats, etc.)
- Encourage experimentation and play
- Remind students this is a learned skill - persistence matters
