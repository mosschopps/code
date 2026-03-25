# Imports
import time
from machine import Pin
from neopixel import NeoPixel

# Define the strip pin number (0) and number of LEDs (15)
strip = NeoPixel(Pin(0), 15)

# Colour variables
red = 64,0,0
green = 0,64,0
blue= 0,0,64
yellow= 64,64,0
cyan= 0,64,64
magenta= 64,0,64
white= 64,64,64
black= 0,0,0

# Define colour list
colours = [red, green, blue, yellow, cyan, magenta, white, black]
try:
    while True: # Run forever

        # Iterate over the colours
        for j in colours:
        
            # Then iterate over 15 leds
            for i in range(15):
            
                # Set each LED in the range to red
                strip[i] = (j)
            
                # Delay - the speed of the chaser
                time.sleep(0.05)
            
                # Send the data to the strip
                strip.write()
except:
    strip.fill((0, 0, 0))
    strip.write()
