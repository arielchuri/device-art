# Bring in libraries
# import time
import board
import touchio
import digitalio
import neopixel

# Set up touch sensors and a variable to track if they have been touched.
touch_A4 = touchio.TouchIn(board.A4)
A4touched = False
touch_A3 = touchio.TouchIn(board.A3)
A3touched = False

# Set up neopixels
pixels = neopixel.NeoPixel(board.NEOPIXEL, 10, brightness=0.9, auto_write=False)
my_bright = 1 # A variable to track the brightness of the LEDs.

# An array of brightness values for each color.
AQUA = [(0,0,0),(0,32,64),(0,64,128),(0,96,192),(0,128,255)]
PUCE = [(0,0,0),(32,0,64),(64,0,128),(96,0,192),(128,0,255)]
WHITE = [(0,0,0),(32,32,32),(96,96,96),(128,128,128),(255,255,255)]

colors = [AQUA, PUCE, WHITE] # A list of colors.
colornum = 0 # A variable to keep track of where we are in the list of colors.
my_color = AQUA # A variable for the current color of the lights.

while True:
    if touch_A4.value and A4touched == False:
        A4touched = True # This and the line above cause this section to run only once
        colornum = colornum + 1
        if colornum == 3:
            colornum = 0
        my_color = colors[colornum]
        print(colornum)
    elif touch_A4.value == False and A4touched == True:
        A4touched = False
    if touch_A3.value and A3touched == False:
        A3touched = True
        my_bright = my_bright + 1
        if my_bright == 5:
            my_bright = 0
    elif touch_A3.value == False and A3touched == True:
        A3touched = False
    print(my_bright)
    pixels.fill(my_color[my_bright])
    pixels.show()
