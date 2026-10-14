# SPDX-FileCopyrightText: 2026 Ariel Churi
# SPDX-License-Identifier: MIT

"""
Display a 1-bit monochrome BMP image on an SSD1306 OLED display using CircuitPython.

Requirements:
- adafruit_displayio_ssd1306.mpy in CIRCUITPY/lib/
- An indexed 1-bit monochrome .bmp file (e.g. test_pattern.bmp, 128x32 or 128x64) in the root of CIRCUITPY/
"""

import board
import busio
import displayio
from i2cdisplaybus import I2CDisplayBus
import adafruit_displayio_ssd1306

# Release any previous displays
displayio.release_displays()

# Initialize I2C communication (Pico GP1 = SCL, GP0 = SDA)
i2c = busio.I2C(board.GP1, board.GP0)
display_bus = I2CDisplayBus(i2c, device_address=0x3C)

# Configure the SSD1306 display (set height to 32 or 64 to match your hardware)
WIDTH = 128
HEIGHT = 32
display = adafruit_displayio_ssd1306.SSD1306(display_bus, width=WIDTH, height=HEIGHT)

# Load the 1-bit monochrome BMP image directly from the root of CIRCUITPY
# Ensure your BMP file is formatted as a 1-bit indexed monochrome bitmap matching your display dimensions.
bitmap = displayio.OnDiskBitmap("/test_pattern.bmp")

# Create a TileGrid and root Group to hold the image
tile_grid = displayio.TileGrid(bitmap, pixel_shader=bitmap.pixel_shader)
group = displayio.Group()
group.append(tile_grid)

# Show the image group on the display
display.root_group = group

while True:
    pass
