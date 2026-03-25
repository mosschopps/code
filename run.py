# Imports
from utime import sleep
from machine import Pin
from neopixel import NeoPixel

# Define the strip pin number (0) and number of LEDs (15)
strip = NeoPixel(Pin(0), 15)
delay = (0.05)
red = (60, 0, 0)
green = (0, 60, 0)
blue = (0, 0, 60)
black = (0, 0, 0)
# Select the first pixel (pixel 0)
# Set the RGB colour (red)
def fill(colour):
    for j in range(15):
    
        strip[j] = (colour)
        sleep(delay)
        # Send the data to the strip
        strip.write()
    
def empty():    
    for j in reversed(range(15)):
        strip[j] = (black)
        sleep(delay)
        # Send the data to the strip
        strip.write()
fill(red)
sleep(0.5)
empty()
fill(green)
sleep(0.5)
empty()
fill(blue)
sleep(0.5)
empty()