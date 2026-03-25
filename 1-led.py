# Imports
import time
from machine import Pin
from neopixel import NeoPixel

# Define the strip pin number (0) and number of LEDs (15)
strip = NeoPixel(Pin(0), 15)
        
# Select the first pixel (pixel 0)
# Set the RGB colour (red)
strip[0] = (255,0,0)

# Send the data to the strip
strip.write()
