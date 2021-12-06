from gpiozero import PWMLED, LED
from time import sleep

red = PWMLED(21)
green = LED(20)

green.on()
sleep(0.5)
green.off()
for n in range(100):
    red.value = n/100
    sleep(0.1)

green.on()
sleep(0.5)
green.off()

for m in range(100, 0, -1):
    red.value = m/100
    sleep(0.1)

red.off()

green.on()
sleep(0.5)
green.off()