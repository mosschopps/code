# Imports
from time import sleep
import random
from machine import Pin
from neopixel import NeoPixel
delay = 0.005
pixel = 0
#define colours
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
yellow = (255, 255, 0)
cyan = (0, 255, 255)
magenta = (255, 0, 255)
silver = (192, 192, 192)
grey = (128, 128, 128)
crimson = (220, 20, 60)
orange = (255, 165, 0)
midnightblue = (25, 25, 112)
hotpink = (255, 105, 180)
brown = (139, 69, 19)
#define colour list
colours = [red, green, blue, yellow, cyan, magenta, silver, grey, crimson, orange, midnightblue, hotpink, brown]
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
    
