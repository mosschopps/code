import pygame
import sys
from gpiozero import MCP3008, PWMLED, LED, Button
from signal import pause
import time


# Create width and height constants
WINDOW_WIDTH = 890
WINDOW_HEIGHT = 600
mbv = 12.1
bbv = 12.1
ost = 10
ist = 17
mft = 98
bft = 97
cst = 0
prt = 10
alarm = 0
redled = LED(23)
yellowled = LED(24)
greenled = LED(25)
# Initialise all the pygame modules
pygame.init()

# Create a game window
game_window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

# Set title
pygame.display.set_caption("Alarm window")
font1 = pygame.font.Font('freesansbold.ttf', 40)
font2 = pygame.font.Font('freesansbold.ttf', 80)

clock = pygame.time.Clock()

game_running = True

pot1 = MCP3008(0)
pot2 = MCP3008(1)

mbv = pot1.value*20

#r1=10k r2=2k2 gives 2.9v ouyput from 16v input

# Game loop
while game_running:
    # Loop through all active events
    for event in pygame.event.get():
        # Close the program if the user presses the 'X'
        if event.type == pygame.QUIT:
            game_running = False




    # Fill the window with black / colours in r g b 
    game_window.fill((0, 0, 0))
    text0 = font1.render('Alarm system', True, (0, 200, 0)) 
    text1a = font1.render('Main battery voltage  ' + str(mbv) + ' V' , True, (0, 200, 0))
    text1b = font1.render('Main battery voltage  ' + str(mbv) + ' V' , True, (200, 200, 0))
    text1c = font1.render('Main battery voltage  ' + str(mbv) + ' V' , True, (200, 0, 0))
    text2a = font1.render('Backup battery voltage  ' + str(bbv) + ' V', True, (0, 200, 0))
    text2b = font1.render('Backup battery voltage  ' + str(bbv) + ' V', True, (200, 200, 0))
    text2c = font1.render('Backup battery voltage  ' + str(bbv) + ' V', True, (200, 0, 0))


    
    # Draw text
    game_window.blit(text0, (280, 0))
    if mbv >= 12.0:
        game_window.blit(text1a, (100, 50))
    elif mbv > 11.5 and mbv < 11.9:
        game_window.blit(text1b, (100, 50))
        alarm = 1
    else:
        game_window.blit(text1c, (100, 50))
        alarm = 2
    
    


    clock.tick(2)

# Uninitialize all pygame modules and quit the program
pygame.quit()
sys.exit()