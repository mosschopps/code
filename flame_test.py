from gpiozero import Button

flame = Button(4)
msg1 = ""

while True:
    if flame.value ==1:
        msg1 = "Fire ! "
    else:
        mag1 = "No fire   "