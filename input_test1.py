from gpiozero import MCP3008
from time import sleep

pot1 = MCP3008(0)
pot2 = MCP3008(1)

while True:
    
    volt1i = pot1.value * 18.55
    volt1o = round(volt1i,1)
    volt2i = pot2.value * 18.55
    volt2o = round(volt2i,1)
    print(volt1o, volt2o)
    sleep(1)