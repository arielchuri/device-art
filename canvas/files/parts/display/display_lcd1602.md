# Character LCD 1602 (I²C Backpack & Bare 16-Pin Configurations)

The LCD 1602 is a classic 16-character by 2-line alphanumeric liquid crystal display based on the HD44780 controller. It is one of the most common displays found in Arduino starter kits.

Depending on your kit, you may have:
1. **With I²C Backpack**: A small secondary daughterboard soldered to the back with **4 pins** (`GND`, `VCC`, `SDA`, `SCL`) and a blue contrast potentiometer.
2. **Bare LCD (No Backpack)**: A single row of **16 pins or holes** along the top edge, requiring parallel GPIO wiring and an external potentiometer.

---

## 1. Technical Datasheets & 3D CAD Models

- **Technical Datasheet & Dimensional Guide (I²C Backpack):** [lcd1602-i2c-module.pdf](lcd1602-i2c-module.pdf) (High-precision 4-view mechanical drawing: front, back, side stackup, and top view comparing straight vs. right-angle bent headers).
- **Display 3D STEP Model:** [lcd1602.step](lcd1602.step)
- **I²C Backpack 3D STEP Model:** [lcd1602_i2c_backpack.step](lcd1602_i2c_backpack.step)

---

## 2. Key Dimensions & Enclosure Clearances

- **Module PCB Size:** $80.0 \times 36.0\text{ mm}$ ($3.150" \times 1.417"$)
- **Mounting Hole Centers:** $75.0 \times 31.0\text{ mm}$ ($2.5\text{ mm}$ inset from edges, $4\times \varnothing 3.0\text{ mm}$)
- **Viewing Window:** $64.5 \times 16.0\text{ mm}$ (Active Character Matrix: $56.2 \times 11.5\text{ mm}$)
- **Depth (Bare Module):** $9.0\text{ mm} - 10.0\text{ mm}$ (bezel to PCB back)
- **Depth with I²C Backpack (Right-Angle Header):** $14.5\text{ mm} - 16.0\text{ mm}$ max (requires $\ge 16\text{ mm}$ enclosure depth, $\ge 15\text{ mm}$ lateral plug clearance)
- **Depth with I²C Backpack (Straight Header):** $24.0\text{ mm}$ max pin tips (requires $\ge 30\text{ mm}$ enclosure depth for DuPont cable housing)

---

## 3. Configuration A: Using the I²C Backpack (4 Wires)

Connect the 4-pin I²C header to power and Pico I²C bus:
- **GND** $\rightarrow$ System Ground (`GND`)
- **VCC** $\rightarrow$ `VBUS` (+5V) or `3V3` (5V recommended for full contrast & backlight)
- **SDA** $\rightarrow$ `GP0` or `GP4` (I²C Data)
- **SCL** $\rightarrow$ `GP1` or `GP5` (I²C Clock)

> **Contrast Note:** If the display is blank or shows solid white boxes on power-up, turn the blue potentiometer on the rear backpack with a small screwdriver until characters appear sharply.

### CircuitPython (I²C Mode)
Install `adafruit_character_lcd` library into your Pico's `lib/` folder.

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

lcd.backlight = True
lcd.message = "Hello, Maker!\n1602 I2C Display"

while True:
    time.sleep(2)
    lcd.clear()
    lcd.message = "Status: Ready\nMode: Active"
    time.sleep(2)
```

---

## 4. Configuration B: Using the Bare 16-Pin LCD (Parallel 4-Bit Mode)

If your LCD does not have a backpack, connect it using 4-bit parallel mode. This uses 6 GPIO pins, plus power, ground, and an external 10k potentiometer for contrast.

### 16-Pin Interconnect Table

| Pin | Symbol | Function | Connection on Breadboard / Pico |
| :---: | :--- | :--- | :--- |
| **1** | `VSS` | Power Ground | Connect to **GND** |
| **2** | `VDD` | Power Supply (+5V) | Connect to **VBUS (5V)** |
| **3** | `V0` | Contrast Adjustment | Connect to **Wiper (Center Pin) of 10k Potentiometer** |
| **4** | `RS` | Register Select | Connect to **Pico GP16** |
| **5** | `RW` | Read/Write Select | Connect to **GND** (Write mode only) |
| **6** | `E` | Enable Strobe | Connect to **Pico GP17** |
| **7–10**| `D0–D3`| Low Data Bits | **Leave Unconnected** (4-bit mode only uses high bits) |
| **11** | `D4` | Data Bit 4 | Connect to **Pico GP18** |
| **12** | `D5` | Data Bit 5 | Connect to **Pico GP19** |
| **13** | `D6` | Data Bit 6 | Connect to **Pico GP20** |
| **14** | `D7` | Data Bit 7 | Connect to **Pico GP21** |
| **15** | `A` | Backlight Anode (+) | Connect to **VBUS (5V)** through a **220Ω resistor** |
| **16** | `K` | Backlight Cathode (-)| Connect to **GND** |

*Potentiometer Wiring for Contrast:* Outer leg 1 $\rightarrow$ 5V, Outer leg 2 $\rightarrow$ GND, Center wiper $\rightarrow$ Pin 3 (`V0`).

### CircuitPython (Parallel 4-Bit Mode)

```python
import time
import board
import digitalio
import adafruit_character_lcd.character_lcd as character_lcd

# Modify columns and rows for 16x2 LCD
lcd_columns = 16
lcd_rows = 2

# Pin assignments on Raspberry Pi Pico
lcd_rs = digitalio.DigitalInOut(board.GP16)
lcd_en = digitalio.DigitalInOut(board.GP17)
lcd_d4 = digitalio.DigitalInOut(board.GP18)
lcd_d5 = digitalio.DigitalInOut(board.GP19)
lcd_d6 = digitalio.DigitalInOut(board.GP20)
lcd_d7 = digitalio.DigitalInOut(board.GP21)

# Initialize Character LCD in 4-bit parallel mode
lcd = character_lcd.Character_LCD_Mono(
    lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6, lcd_d7,
    lcd_columns, lcd_rows
)

lcd.message = "Bare 1602 LCD\nParallel 4-Bit!"

while True:
    time.sleep(2)
    lcd.clear()
    lcd.message = "Pico Connected\nContrast OK"
    time.sleep(2)
```
