from gpiozero import Button, MCP3008
from time import sleep
pot1 = MCP3008(0)
v1 = pot1.value*100

btn = Button(4)
while True:
    while not btn.is_pressed:
        pass
    print("Magnet near !")
    sleep(1)
    #print(v1)