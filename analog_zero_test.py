from gpiozero import MCP3008
from time import sleep
pot1 = MCP3008(0)
pot2 = MCP3008(1)
pot3 = MCP3008(2)
pot4 = MCP3008(3)
pot5 = MCP3008(4)
pot6 = MCP3008(5)
pot7 = MCP3008(6)
pot8 = MCP3008(7)
while True: 
    v1 = pot1.value*18.6
    v1a = ('{:.2f}'.format(v1))
    v2 = pot2.value*18.6
    v2a = ('{:.2f}'.format(v2))
    v3 = pot3.value*100
    v3a = ('{:.0f}'.format(v3))
    v4 = pot4.value*100
    v4a = ('{:.0f}'.format(v4))
    v5 = pot5.value*60-20
    v5a = ('{:.1f}'.format(v5))
    v6 = pot6.value*60-20
    v6a = ('{:.1f}'.format(v6))
    print("voltage 1 in volts")
    print(v1a)
    print("voltage 2 in volts")
    print(v2a)
    print("main fuel tank")
    print(v3a)
    print("aux fuel tank")
    print(v4a)
    print("inside temp")
    print(v5a)
    print("outside temp")
    print(v6a)
    print()
    sleep(1)