#!/usr/bin/python3
from gpiozero import MCP3008
from time import sleep
voltage = [0,0,0,0,0,0,0,0]
vref = 3.3

while True:
    for x in range(5, 8):
        with MCP3008(channel=x) as reading:
            voltage[x] = reading.value * vref
            print(x,": ", '{:.2f}'.format(voltage[x]), "V")
    sleep(0.1)