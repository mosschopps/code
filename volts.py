import pygame
import sys
from gpiozero import MCP3008, PWMLED, LED, Button
from signal import pause
import time


# Create width and height constants
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 500
v2 = 0
# Initialise all the pygame modules
pygame.init()

# Create a game window
game_window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

# Set title
pygame.display.set_caption("Raspberry Pi Voltmeter")
font1 = pygame.font.Font('freesansbold.ttf', 40)

clock = pygame.time.Clock()

game_running = True

pot1 = MCP3008(0)
pot2 = MCP3008(1)
pot3 = MCP3008(2)
pot4 = MCP3008(3)
pot5 = MCP3008(4)
pot6 = MCP3008(5)
pot7 = MCP3008(6)
pot8 = MCP3008(7)


#r1=10k r2=2k2 gives 2.9v ouyput from 16v input

# Game loop
while game_running:
    # Loop through all active events
    for event in pygame.event.get():
        # Close the program if the user presses the 'X'
        if event.type == pygame.QUIT:
            game_running = False

    v1 = pot1.value*5
    v1a = ('{:.2f}'.format(v1))
    v1 = pot1.value*10
    v2a = ('{:.2f}'.format(v1))
    v1 = pot1.value*15
    v3a = ('{:.2f}'.format(v1))
    v1 = pot1.value*20
    v4a = ('{:.2f}'.format(v1))
    v1 = pot1.value*25
    v5a = ('{:.2f}'.format(v1))
    v1 = pot1.value*30
    v6a = ('{:.2f}'.format(v1))
    v1 = pot1.value*35
    v7a = ('{:.2f}'.format(v1))
    v1 = pot1.value*40
    v8a = ('{:.2f}'.format(v1))
    # Fill the window with black / colours in r g b 
    game_window.fill((0, 0, 0))
    text0 = font1.render('Raspberry Pi Voltmeter', True, (0, 200, 0)) 
    text1 = font1.render('voltage 1 = ' + str(v1a) + ' V' + ' 5 volt range', True, (0, 200, 0))    
    text2 = font1.render('voltage 2 = ' + str(v2a) + ' V' + ' 10 volt range', True, (0, 200, 0))
    text3 = font1.render('voltage 3 = ' + str(v3a) + ' V' + ' 15 volt range', True, (0, 200, 0))    
    text4 = font1.render('voltage 4 = ' + str(v4a) + ' V' + ' 20 volt range', True, (0, 200, 0))
    text5 = font1.render('voltage 5 = ' + str(v5a) + ' V' + ' 25 volt range', True, (0, 200, 0))    
    text6 = font1.render('voltage 6 = ' + str(v6a) + ' V' + ' 30 volt range', True, (0, 200, 0))
    text7 = font1.render('voltage 7 = ' + str(v7a) + ' V' + ' 35 volt range', True, (0, 200, 0))    
    text8 = font1.render('voltage 8 = ' + str(v8a) + ' V' + ' 40 volt range', True, (0, 200, 0))
    
    # Draw text
    game_window.blit(text0, (50, 0))
    game_window.blit(text1, (50, 50))
    game_window.blit(text2, (50, 100))
    game_window.blit(text3, (50, 150))
    game_window.blit(text4, (50, 200))
    game_window.blit(text5, (50, 250))
    game_window.blit(text6, (50, 300))
    game_window.blit(text7, (50, 350))
    game_window.blit(text8, (50, 400))

    # Update our display
    pygame.display.update()

    clock.tick(2)

# Uninitialize all pygame modules and quit the program
pygame.quit()
sys.exit()