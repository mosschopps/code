'''HTML Colour Codes for Rainbow Colours

The colours of the rainbow can be represented in HTML using specific colour codes.
Below is a table that lists each color along with its corresponding HTML color code.
Colour-HTML Color Code
Red-#FF0000 255, 0, 0
Orange-#FFA500 255, 165, 0
Yellow-#FFFF00 255, 255, 0
Green-#008000 0, 128, 0
Blue-#0000FF 0, 0, 255
Indigo-#4B0082 76, 0, 130
Violet-#EE82EE 238, 30, 238

These codes are commonly used in web design to accurately display the colours of the rainbow.'''
# Imports
from time import sleep
import random
from machine import Pin
from neopixel import NeoPixel
delay = 0.05
pixel = 0
#define colours
red = (255, 0, 0)
orange = (255, 165, 0)
yellow = (255, 255, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
indigo = (76, 0, 130)
violet = (238, 30, 238)


#define colour list
colours = [red, orange, yellow, green, blue, indigo, violet]
# Define the strip pin number (0) and number of LEDs (15)
strip = NeoPixel(Pin(0), 15)

def fillStrip():
    pixel = random.randrange(0, 15)
    col = random.choice(colours)
    strip[pixel] = (col)
    strip.write()

try:
    
    while True:
        #main loop
        fillStrip()
        sleep(delay)
        
except KeyboardInterrupt:
    strip.fill((0, 0, 0))
    strip.write()
finally:
    strip.fill((0, 0, 0))
    strip.write()
    