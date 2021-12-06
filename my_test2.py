from gpiozero import LED
from signal import pause

red = LED(21)

red.blink()

pause()