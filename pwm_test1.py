from gpiozero import PWMLED
from time import sleep

led = PWMLED(21)

for n in range(100):
    led.value = n/100
    sleep(0.2)
    
led.off()    