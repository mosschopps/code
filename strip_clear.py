# Imports
from time import sleep
from machine import Pin
from neopixel import NeoPixel

# Define the strip pin number (0) and number of LEDs (15)
strip = NeoPixel(Pin(16), 15)
strip.fill((0, 0, 0))
strip.write()
