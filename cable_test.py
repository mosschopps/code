# usb cable tester program © moss 09/04/2024
# wait for button press test Vbus, gnd, D+, D-
# light up red for charging only cable
# light up green for data cable
# light up blue for faulty cable
from machine import Pin
from utime import sleep
vb = 0
dp = 0
dm = 0
gn = 0
vbuso = Pin(7, Pin.OUT) #red
vbusi = Pin(8, Pin.IN, Pin.PULL_DOWN)
dpluso = Pin(9, Pin.OUT) #green
dplusi = Pin(10, Pin.IN, Pin.PULL_DOWN)
dminuso = Pin(11, Pin.OUT) #white
dminusi = Pin(12, Pin.IN, Pin.PULL_DOWN)
gndo = Pin(13, Pin.OUT) #black
gndi = Pin(14, Pin.IN, Pin.PULL_DOWN)
ledr = Pin(15, Pin.OUT)
ledg = Pin(16, Pin.OUT)
ledb = Pin(17, Pin.OUT)
button = Pin(18, Pin.IN, Pin.PULL_UP)

def get_button():
    return not button.value()

def lamp_test_function():
    ledr.value(0)
    ledg.value(0)
    ledb.value(0)
    ledr.value(1)
    sleep(.5)
    ledr.value(0)
    ledg.value(1)
    sleep(.5)
    ledg.value(0)
    ledb.value(1)
    sleep(.5)
    ledb.value(0)
    sleep(.5)
    
def button_press_function():
    ledr.value(0)
    ledg.value(0)
    ledb.value(0)
    vbuso.value(0)
    dpluso.value(0)
    dminuso.value(0)
    gndo.value(0)
    vbuso.value(1)
    if vbusi() == 1:
        vb = 1
    else:
        vb = 0
    vbuso.value(0)
    dpluso.value(1)
    if dplusi() == 1:
        dp = 1
    else:
        dp = 0
    dpluso.value(0)
    dminuso.value(1)
    if dminusi() == 1:
        dm = 1
    else:
        dm = 0
    dminuso.value(0)
    gndo.value(1)
    if gndi() == 1:
        gn = 1
    else:
        gn = 0
    gndo.value(0)
    sleep(1)
    if vb and gn == 1:
        if dp and dm == 1:
           ledg.value(1)
        else:   
           ledr.value(1)    
    else:
        ledb.value(1)   


lamp_test_function()        
while True:
    if get_button() == 1:
        button_press_function()
