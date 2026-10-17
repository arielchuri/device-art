# Parts & Hardware Master Reference

This document indexes all electronic components, breakout boards, and mechanical datasheets for the **Device Art Hardware Kit** and auxiliary maker parts.

---

## 1. Kit Breakout Modules & Displays

| Component | Hardware Guide | Technical Datasheets & Mechanical Drawings | CAD Models |
| :--- | :--- | :--- | :---: |
| **SSD1306 OLED (0.96" I²C)** | [Display (SSD1306 OLED)](display/display.md) | • [ssd1306-oled-module.pdf](display/ssd1306-oled-module.pdf) (Dimensional Drawing)<br>• [SSD1306.pdf](display/SSD1306.pdf) (IC Datasheet) | — |
| **Character LCD 1602 (I²C / Bare)** | [Display (Character LCD 1602)](display/display_lcd1602.md) | • [lcd1602-i2c-module.pdf](display/lcd1602-i2c-module.pdf) (4-View Drawing & Header Options) | [lcd1602.step](display/lcd1602.step)<br>[backpack.step](display/lcd1602_i2c_backpack.step) |
| **Real Time Clock (DS3231 / ZS-042)** | [Real Time Clock DS3231](realTimeClock/realTimeClock_ds3231.md) | • [ds3231-rtc-module.pdf](realTimeClock/ds3231-rtc-module.pdf) (Dimensions & CR2032 Safety Mod) | [ds3231_rtc.step](realTimeClock/ds3231_rtc.step) |
| **Ultrasonic Sensor (HC-SR04)** | [Ultrasonic Sensor HC-SR04](ultrasonic_sensor/ultrasonic_sensor.md) | • [hcsr04-ultrasonic-module.pdf](ultrasonic_sensor/hcsr04-ultrasonic-module.pdf) (Dimensional Guide)<br>• [HCSR04.pdf](ultrasonic_sensor/HCSR04.pdf) (Electrical Specs) | — |
| **Touch Sensor (TTP223 / TTP223B)** | [Capacitive Touch Sensor](captouch_sensor/captouch_sensor.md) | • [ttp223-touch-sensor.pdf](captouch_sensor/ttp223-touch-sensor.pdf) (Dimensions & Jumper Matrix)<br>• [TTP223.pdf](captouch_sensor/TTP223.pdf) (Tontek IC Datasheet) | — |
| **NeoPixel (WS2812B / 5mm Diffused)** | [NeoPixel WS2812B](neopixel/neopixel.md) | • [WS2812B.pdf](neopixel/WS2812B.pdf) (Official Worldsemi Datasheet) | — |
| **Audio & Speaker** | [Audio and Speaker](audio.md) / [Piano](piano.md) | Tone generation, PWM audio, and 8Ω speaker guides | — |
| **RGB LED** | [RGB LED](RGB_LED/rgb_led.md) | Common anode/cathode wiring & PWM color cycling | — |
| **Digital Multimeter** | — | • [multitester_basic_color.pdf](multitester_basic_color.pdf) (Operation Guide) | — |

---

## 2. Microcontroller Hardware & Setup

- **Raspberry Pi Pico (RP2040)**:
  - [Official Pico Hardware Datasheet](raspberryPiPico/pico-datasheet.pdf) (Pinout diagrams, electrical specifications, RP2040 peripherals)
  - [Raspberry Pi Pico Pinout Diagram](raspberryPiPico/raspberry_pi_Pico-R3-Pinout-narrow.png)
  - [Microcontroller Intro Guide](../raspberryPiPico/microcontroller_intro.md)

---

## 3. Additional Component Sourcing & Project References

### Actuators & Outputs
- [Standard Servo Motor](https://www.adafruit.com/product/155)
- [Micro Servo Motor](https://www.adafruit.com/product/4411) 
- [Piezo Buzzer](https://www.adafruit.com/product/160)
- [NeoPixel Driver Board](https://www.adafruit.com/product/5650)
- [Sewable Flora NeoPixel](https://www.adafruit.com/product/1260) 
- [5mm Through-Hole NeoPixel](https://www.adafruit.com/product/1938) 
- [Mini Air Pump (3V-6V)](https://www.adafruit.com/product/4700) 
- [Mini Water Pump (3V-6V)](https://www.adafruit.com/product/4547) 

### Inputs & Controls
- [Rotary Potentiometer (10k linear)](https://www.adafruit.com/product/562) 
- [Panel Mount Toggle Switch](https://www.adafruit.com/product/3221)
- [Tactile Pushbutton](https://www.adafruit.com/product/1503)

### Sensors
- [MPL3115A2 I²C Barometric Pressure / Altitude / Temperature](https://www.adafruit.com/product/1893)
- [Light Dependent Resistor (CdS Photoresistor)](https://www.adafruit.com/product/161)

### Hardware & Power
- [Stacking Female Headers for Pico](https://www.adafruit.com/product/5582)
- [Perma-Proto Half-Size Breadboard PCB](https://www.adafruit.com/product/5905) 
- [Lithium Ion Polymer Battery (3.7V 1200mAh)](https://www.adafruit.com/product/258)
