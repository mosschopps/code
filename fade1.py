# Imports
import time
from machine import Pin
from neopixel import NeoPixel

# Define the strip pin number (16) and number of LEDs (15)
strip = NeoPixel(Pin(0), 15)

# Variable for the fade speed
delay = 0.005

while True: # Run forever
    
    # Iterate from 1 to 255 in steps of 1
    for i in range(1,255,1):
        
        # Fill the strip using the iterated R value
        strip.fill((i,0,0))
        
        # Write the data to the LED strip
        strip.write()
        
        # Delay
        time.sleep(delay)
        
    # iterate from 255 to 1 in steps of -1
    for i in range(255,1,-1):
        
        # Fill the strip using the iterated R value
        strip.fill((i,0,0))
        
        # Write the data to the LED strip
        strip.write()
        
        # Delay
        time.sleep(delay)
