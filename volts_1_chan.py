import pygame
import sys
from gpiozero import MCP3008, PWMLED, LED, Button
from signal import pause
import time


# Create width and height constants
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 200
v2 = 0
# Initialise all the pygame modules
pygame.init()

# Create a game window
game_window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

# Set title
pygame.display.set_caption("Raspberry Pi Voltmeter")
font1 = pygame.font.Font('freesansbold.ttf', 70)

clock = pygame.time.Clock()

game_running = True

pot1 = MCP3008(0)



#r1=10k r2=2k2 gives 2.9v ouyput from 16v input

# Game loop
while game_running:
    # Loop through all active events
    for event in pygame.event.get():
        # Close the program if the user presses the 'X'
        if event.type == pygame.QUIT:
            game_running = False

    v1 = pot1.value*18.6
    v1a = ('{:.2f}'.format(v1))
    
    
    # Fill the window with black / colours in r g b 
    game_window.fill((0, 0, 0))
    text0 = font1.render('Raspberry Pi Voltmeter', True, (0, 200, 0)) 
    text1 = font1.render('Channel 1 = ' + str(v1a) + ' V', True, (0, 200, 0))    
    
    
    # Draw text
    game_window.blit(text0, (10, 0))
    game_window.blit(text1, (60, 90))
    

    # Update our display
    pygame.display.update()

    clock.tick(2)

# Uninitialize all pygame modules and quit the program
pygame.quit()
sys.exit()