# Character LCD 1602 (with PCF8574 I2C Backpack)

The LCD 1602 is a classic 16-character by 2-line alphanumeric liquid crystal display. Paired with a PCF8574 I²C backpack module, it only requires 4 wires (`GND`, `VCC`, `SDA`, `SCL`) instead of 16 parallel pins.

---

## 1. Technical Datasheet & 3D CAD Models

- **Technical Datasheet & Dimensional Guide:** [lcd1602-i2c-module.pdf](lcd1602-i2c-module.pdf) (High-precision 4-view mechanical drawing: front, back, side stackup, and top view comparing straight vs right-angle bent headers).
- **Display 3D STEP Model:** [lcd1602.step](lcd1602.step)
- **I²C Backpack 3D STEP Model:** [lcd1602_i2c_backpack.step](lcd1602_i2c_backpack.step)

---

## 2. Key Dimensions & Clearances

- **Module PCB Size:** $80.0 \times 36.0\text{ mm}$ ($3.150" \times 1.417"$)
- **Mounting Hole Centers:** $75.0 \times 31.0\text{ mm}$ ($2.5\text{ mm}$ inset from edges, $4\times \varnothing 3.0\text{ mm}$)
- **Viewing Window:** $64.5 \times 16.0\text{ mm}$ (Active Character Matrix: $56.2 \times 11.5\text{ mm}$)
- **Depth with Bent / Right-Angle Header:** $14.5\text{ mm} - 16.0\text{ mm}$ max (requires $\ge 16\text{ mm}$ enclosure depth, $\ge 15\text{ mm}$ lateral plug clearance)
- **Depth with Straight Header:** $24.0\text{ mm}$ max pin tips (requires $\ge 30\text{ mm}$ enclosure depth for DuPont cable housing)

---

## 3. Wiring to Raspberry Pi Pico

Connect the 4-pin I²C header to power and Pico I²C bus:
- **GND** $\rightarrow$ System Ground (`GND`)
- **VCC** $\rightarrow$ `VBUS` (+5V) or `3V3` (5V recommended for full contrast & backlight)
- **SDA** $\rightarrow$ `GP0` or `GP4` (I²C Data)
- **SCL** $\rightarrow$ `GP1` or `GP5` (I²C Clock)

> **Contrast Note:** If the display is blank or shows white boxes on power-up, turn the blue potentiometer on the rear backpack with a small screwdriver until characters appear sharply.

---

## 4. CircuitPython Example

Install `adafruit_character_lcd` library into your Pico's `lib` folder.

```python
import time
import board
import busio
import adafruit_character_lcd.character_lcd_i2c as character_lcd

# Modify columns and rows for 16x2 LCD
lcd_columns = 16
lcd_rows = 2

# Initialize I2C bus (RP2040 GP0/GP1 or board default)
i2c = busio.I2C(board.GP1, board.GP0)

# Default I2C address is typically 0x27 (or 0x3F for PCF8574AT chips)
lcd = character_lcd.Character_LCD_I2C(i2c, lcd_columns, lcd_rows, address=0x27)

# Turn on backlight and display a message
lcd.backlight = True
lcd.message = "Hello, Maker!\n1602 I2C Display"

while True:
    time.sleep(2)
    lcd.clear()
    lcd.message = "DCC Printer\nStatus: Ready"
    time.sleep(2)
```
