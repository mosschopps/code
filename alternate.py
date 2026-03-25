from machine import Pin
from utime import sleep
ledg = Pin(13, Pin.OUT)
ledr = Pin(12, Pin.OUT)
ledr.value(1)
ledg.value(0)

while True:
    ledg.toggle()
    ledr.toggle()
    sleep(1)