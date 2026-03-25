# SPDX-FileCopyrightText: 2021 Kattni Rembor for Adafruit Industries
#
# SPDX-License-Identifier: MIT

"""
Button and LED example for Pico. Turns on LED when button is pressed.

REQUIRED HARDWARE:
* Button switch on pin GP13.
* LED on pin GP14.
"""
import time
import board
import digitalio
import usb_hid
from adafruit_hid.mouse import Mouse

mouse = Mouse(usb_hid.devices)

ledr = digitalio.DigitalInOut(board.GP14)
ledr.direction = digitalio.Direction.OUTPUT
ledg = digitalio.DigitalInOut(board.GP15)
ledg.direction = digitalio.Direction.OUTPUT
button = digitalio.DigitalInOut(board.GP13)
button.switch_to_input(pull=digitalio.Pull.DOWN)

while True:
    if button.value:
        ledr.value = True
        ledg.value = False
        mouse.click(Mouse.LEFT_BUTTON)
        time.sleep(0.05)  # Debounce delay
    ledr.value = False
    ledg.value = True