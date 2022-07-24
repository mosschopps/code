from gpiozero import Button

btn = Button(21)
while not btn.is_pressed:
    pass
print("button pressed")