# Index of Raspberry Pi Pico Resources & Canvas Curriculum Assets

This index documents all Raspberry Pi Pico microcontroller setup guides, CircuitPython cheatsheets, code modules, hardware component recipes, and lab assignments migrated into the `canvas/` directory structure.

All file paths are relative to the root `device-art/` repository folder.

---

## 1. Student-Facing Pages & Cheatsheets

| Relative Path | Primary Purpose |
| :--- | :--- |
| `canvas/pages/python_led_blink_simulation.md` | Pure software terminal emulation of the LED state machine, blocking delays vs non-blocking `time.monotonic()` clock checks prior to physical wiring. |
| `canvas/pages/vscode_circuitpython_setup.md` | Complete setup guide for Visual Studio Code, CircuitPython extension, "Run on Save" mechanics, USB mounting, and live Serial Monitor / REPL interaction. |
| `canvas/pages/pico_microcontroller_intro.md` | Core student guide for flashing CircuitPython UF2, USB drive mounting, pinout orientation, and foundational digital/analog/PWM I/O tutorials. |
| `canvas/pages/lecture_code_meets_electricity.md` | Classroom lecture notes bridging electrical principles and Python computation; covers RP2040 chip specs, pin mappings, and first hardware "Hello World". |
| `canvas/files/cheatsheets/pico_circuitpython_cheatsheet.md` | Quick reference card containing concise CircuitPython snippets for digital I/O, pushbuttons with internal pull-downs, analog ADC reading, PWM LED fading, NeoPixel addressing, and I2C OLED display initialization. |


---

## 2. Pico Code Examples, Starter Files & Libraries

| Relative Path | Primary Purpose |
| :--- | :--- |
| `canvas/files/raspberryPiPico/microcontroller_intro.md` | Master pedagogical source markdown for Pico CircuitPython setup and hardware exercises. |
| `canvas/files/raspberryPiPico/micro_programming_quiz.md` | Self-assessment diagnostic quiz covering CircuitPython variables, pin initialization, conditional logic, and range mapping. |
| `canvas/files/raspberryPiPico/raspberry_pi_Pico-R3-Pinout-narrow.png` | Visual reference diagram of the RP2040 40-pin DIP layout and pin functions. |
| `canvas/files/raspberryPiPico/adafruit-circuitpython-bundle-9.x-mpy-20250319.zip` | Offline driver archive containing compiled `.mpy` libraries for CircuitPython 9.x. |
| `canvas/files/raspberryPiPico/01_hello_world/code.py` | Minimal starter script verifying USB serial connection and terminal output. |
| `canvas/files/raspberryPiPico/02_digital_inout/code.py` | Basic digital output and input loop demonstrating LED toggle on button press. |
| `canvas/files/raspberryPiPico/02_digital_inout/code_buttons_switch.py` | Code demonstrating state switching and momentary button handling. |
| `canvas/files/raspberryPiPico/02_digital_inout/code_simpler.py` | Streamlined digital I/O example for introductory teaching. |
| `canvas/files/raspberryPiPico/02_digital_inout/code_simpleryet.py` | Bare-minimum direct assignment of button value to LED state. |
| `canvas/files/raspberryPiPico/02_digital_inout/digital_inout.md` | Explanatory notes on digital logic states, high/low voltage thresholds, and pull-up/pull-down resistors. |
| `canvas/files/raspberryPiPico/03_libraries/adafruit_simplemath.mpy` | Pre-compiled CircuitPython helper library for `map_range` scaling operations. |
| `canvas/files/raspberryPiPico/03_libraries/boardLedBlink.py` | Demonstration of controlling the onboard indicator LED on GP25. |
| `canvas/files/raspberryPiPico/03_libraries/buttonKeypadFade.py` | Advanced demo combining input debounce, matrix keypad scanning, and PWM brightness fading. |
| `canvas/files/raspberryPiPico/03_libraries/fadePotButtonBlink.py` | Integrated multi-component script reading potentiometer voltage to control LED pulse frequency. |
| `canvas/files/raspberryPiPico/03_libraries/gp14Blink.py` | Standalone external GPIO blink test script on pin GP14. |
| `canvas/files/raspberryPiPico/03_libraries/jled.py` | Non-blocking LED animation and breathing pattern utility class. |
| `canvas/files/raspberryPiPico/04_time/code.py` | Demonstrates timing loops, `time.monotonic()` delta calculations, and non-blocking multitasking. |

---

## 3. Hardware Component Guides & Drivers

| Relative Path | Primary Purpose |
| :--- | :--- |
| `canvas/files/parts/display/display.md` | Step-by-step wiring and code guide for monochrome 128x64 SSD1306 I2C OLED displays. |
| `canvas/files/parts/display/adafruit_displayio_ssd1306i.mpy` | Pre-compiled I2C display driver required in the Pico `/lib` folder. |
| `canvas/files/parts/display/code.py` | Graphical shape, line, and bounding box drawing demo on SSD1306 OLED. |
| `canvas/files/parts/display/text.py` | Dynamic text rendering, string formatting, and display group layout script. |
| `canvas/files/parts/neopixel/neopixel.md` | Guide for wiring and driving WS2812B addressable RGB NeoPixels via single-wire timing protocol. |
| `canvas/files/parts/neopixel/neopixel.py` | CircuitPython library module for controlling individual pixels and arrays. |
| `canvas/files/parts/neopixel/rotate.py` | Rotating color chase and rainbow wheel animation demo. |
| `canvas/files/parts/neopixel/strandtest.py` | Color wipe, theater chase, and full RGB diagnostic test routine. |
| `canvas/files/parts/RGB_LED/rgb_led.md` | Guide to wiring 4-pin RGB LEDs (common cathode/anode) using 3 PWM channels. |
| `canvas/files/parts/RGB_LED/code.py` | Basic RGB color mixing cycling through primary and secondary hues. |
| `canvas/files/parts/RGB_LED/code_pot.py` | Controlling RGB LED brightness and single-channel intensity via analog potentiometer. |
| `canvas/files/parts/RGB_LED/code_pot_color.py` | Full analog color-wheel mixer using potentiometer position to calculate RGB ratios. |
| `canvas/files/parts/captouch_sensor/captouch_sensor.md` | Integration guide for TTP223 capacitive touch sensing modules. |
| `canvas/files/parts/captouch_sensor/code.py` | Digital touch trigger script treating capacitive pads as momentary or toggle inputs. |

---

## 4. Visual Schematics & Breadboard Vector Graphics

| Relative Path | Primary Purpose |
| :--- | :--- |
| `canvas/files/images/graphics/pico_pinout.svg` | Clean vector pinout diagram highlighting 3V3, GND, GPIO, ADC, and I2C buses. |
| `canvas/files/images/graphics/pico_breadboard.svg` | Vector representation of the Pico mounted across the central breadboard divider. |
| `canvas/files/images/graphics/first_micro_circuit.svg` | Breadboard pictorial wiring diagram for the first LED output circuit on GP14. |
| `canvas/files/images/graphics/first_micro_circuit_schem.svg` | Standard schematic diagram showing Pico GP14 connected through a 220-ohm resistor to LED. |
| `canvas/files/images/graphics/button_circuit.svg` | Pictorial breadboard wiring for a tactile pushbutton with external/internal pull-down. |
| `canvas/files/images/graphics/button_circuit_schem.svg` | Electrical schematic for momentary pushbutton input connected to GP13. |
| `canvas/files/images/graphics/pot_circuit_schem.svg` | Schematic showing 10k potentiometer wired as a voltage divider into ADC0 (GP26). |
| `canvas/files/images/graphics/pwm_circuit_schem.svg` | Schematic diagram for PWM-driven LED brightness control on GP15. |
| `canvas/files/images/graphics/ldr_circuit_schem.svg` | Schematic diagram for light-dependent resistor (photoresistor) voltage divider circuit. |
| `canvas/files/images/graphics/without_delay_circuit.svg` | Pictorial diagram illustrating concurrent input/output without blocking delays. |
| `canvas/files/images/graphics/neopixel_5mm_diagram.svg` | Pinout and wiring schematic for individual 5mm NeoPixel elements. |
| `canvas/files/images/graphics/breadboard01.svg` | Base vector template of standard 830 tie-point breadboard power and terminal rails. |

---

## 5. Lab Assignments & Studio Challenges

| Relative Path | Primary Purpose |
| :--- | :--- |
| `canvas/assignments/my_first_object/my_first_object.md` | First physical computing assignment: breadboard power rail wiring, serial debugging, non-blocking LED blinking, and button event capture. |
| `canvas/assignments/my_first_object/breadboard.png` | High-resolution visual layout of the completed starter breadboard build. |
| `canvas/assignments/my_first_object/schematic.png` | Electrical schematic for the combined LED and button circuit in Assignment 1. |
| `canvas/assignments/my_first_object/power_on_led.py` | Reference solution code demonstrating power verification and non-blocking multitasking. |
| `canvas/assignments/hardware-software-challenge/hardware-software.md` | Studio challenge testing student debugging skills across physical wiring faults and Python runtime exceptions. |
| `canvas/assignments/hardware-software-challenge/hardware-software_schematic.odg` | Source vector schematic file for the hardware/software troubleshooting exercise. |
| `canvas/assignments/moodlight/moodlight.md` | Project brief for fabricating a desktop mood lamp using laser-cut enclosures, NeoPixels, and touch/sensor inputs. |
| `canvas/assignments/moodlight/mood.py` | Firmware script implementing smooth color transitions and ambient light feedback. |
| `canvas/assignments/moodlight/mood2.py` | Alternate state-machine firmware featuring multi-mode capacitive touch controls. |
| `canvas/assignments/moodlight/moodlight_drawing.svg` | Mechanical 2D layout drawing for enclosure assembly. |
| `canvas/assignments/moodlight/moodlight_laserpattern.svg` | Laser-cutter vector cutting template for the lamp enclosure panels. |
