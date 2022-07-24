import pygame
import sys
from gpiozero import MCP3008, PWMLED, LED, Button
from signal import pause
import time

#alarm v 2.0

# Create width and height constants
WINDOW_WIDTH = 1800
WINDOW_HEIGHT = 900
pot1 = MCP3008(0)
pot2 = MCP3008(1)
pot3 = MCP3008(2)
pot4 = MCP3008(3)
pot5 = MCP3008(4)
pot6 = MCP3008(5)
pot7 = MCP3008(6)
pot8 = MCP3008(7)
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





#r1=10k r2=2k2 gives 2.9v output from 16v input

# Game loop
while game_running:
    # Loop through all active events
    for event in pygame.event.get():
        # Close the program if the user presses the 'X'
        if event.type == pygame.QUIT:
            game_running = False




    # Fill the window with black / colours in r g b
    v1 = pot1.value*18.6
    v1a = ('{:.1f}'.format(v1))
    v2 = pot2.value*18.6
    v2a = ('{:.1f}'.format(v2))
    v3 = pot3.value*100
    v3a = ('{:.0f}'.format(v3))
    v4 = pot4.value*100
    v4a = ('{:.0f}'.format(v4))
    v5 = pot5.value*60-20
    v5a = ('{:.1f}'.format(v5))
    v6 = pot6.value*60-20
    v6a = ('{:.1f}'.format(v6))
    game_window.fill((0, 0, 0))
    text0 = font1.render('Alarm system', True, (0, 200, 0)) 
    text1a = font1.render('Main battery voltage  ' + str(v1a) + ' V' , True, (0, 200, 0))
    text1b = font1.render('Main battery voltage  ' + str(v1a) + ' V' , True, (200, 200, 0))
    text1c = font1.render('Main battery voltage  ' + str(v1a) + ' V' , True, (200, 0, 0))
    text2a = font1.render('Backup battery voltage  ' + str(v2a) + ' V', True, (0, 200, 0))
    text2b = font1.render('Backup battery voltage  ' + str(v2a) + ' V', True, (200, 200, 0))
    text2c = font1.render('Backup battery voltage  ' + str(v2a) + ' V', True, (200, 0, 0))
    text3a = font1.render('Outside temp  ' + str(ost) + ' C', True, (0, 0, 200))
    text3b = font1.render('Outside temp  ' + str(ost) + ' C', True, (0, 200, 0))
    text3c = font1.render('Outside temp  ' + str(ost) + ' C', True, (200, 0, 0))
    text4a = font1.render('Inside temp ' + str(ist) + ' C', True, (0, 0, 200))
    text4b = font1.render('Inside temp ' + str(ist) + ' C', True, (0, 200, 0))
    text4c = font1.render('Inside temp ' + str(ist) + ' C', True, (200, 0, 0))
    text5a = font1.render('Cold store temp  ' + str(cst) + ' C', True, (0, 0, 200))
    text5b = font1.render('Cold store temp  ' + str(cst) + ' C', True, (0, 200, 0))
    text5c = font1.render('Cold store temp  ' + str(cst) + ' C', True, (200, 0, 0))
    text6a = font1.render('Plant room temp ' + str(prt) + ' C', True, (0, 0, 200))
    text6b = font1.render('Plant room temp ' + str(prt) + ' C', True, (0, 200, 0))
    text6c = font1.render('Plant room temp ' + str(prt) + ' C', True, (200, 0, 0))
    text7a = font1.render('Front door closed', True, (0, 200, 0))
    text7b = font1.render('Front door open', True, (200, 0, 0))
    text8a = font1.render('Back door closed', True, (0, 200, 0))
    text8b = font1.render('Back door open', True, (200,0, 0))
    text9a = font1.render('Downstairs smoke detectors clear', True, (0, 200, 0))
    text9b = font1.render('Downstairs smoke detectors tripped', True, (200, 0, 0))
    text10a = font1.render('Upstairs smoke detectors clear', True, (0, 200, 0))
    text10b = font1.render('Upstairs smoke detectors tripped', True, (200, 0, 0))
    text11a = font1.render('Front PIRs clear', True, (0, 200, 0))
    text11b = font1.render('Front PIRs tripped', True, (200, 0, 0))
    text12a = font1.render('Rear PIRs clear', True, (0, 200, 0))
    text12b = font1.render('Rear PIRs tripped', True, (200, 0, 0))
    text13a = font1.render('Front tripwires clear', True, (0, 200, 0))
    text13b = font1.render('Front tripwires tripped', True, (200, 0, 0))
    text14a = font1.render('Rear tripwires clear', True, (0, 200, 0))
    text14b = font1.render('Rear tripwires tripped', True, (200, 0, 0))
    text15a = font1.render('Downstairs panic buttons clear', True, (0, 200, 0))
    text15b = font1.render('Downstairs panic buttons tripped', True, (200, 0, 0))
    text16a = font1.render('Upstairs panic buttons clear', True, (0, 200, 0))
    text16b = font1.render('Upstairs panic buttons tripped', True, (200, 0, 0))
    text115 = font1.render('Main fuel oil tank ' + str(mft) + ' % full', True, (0, 200, 0))
    text116 = font1.render('Backup fuel oil tank ' + str(bft) + ' % full', True, (0, 200, 0))
    text117 = font1.render('Main diesel tank ' + str(bft) + ' % full', True, (0, 200, 0))
    text118 = font1.render('Backup diesel tank ' + str(bft) + ' % full', True, (0, 200, 0))
    text119 = font1.render('Main petrol tank ' + str(bft) + ' % full', True, (0, 200, 0))
    text110 = font1.render('Backup petrol tank ' + str(bft) + ' % full', True, (0, 200, 0))
    text111 = font1.render('Backup fuel tank ' + str(bft) + ' % full', True, (0, 200, 0))
    text96a = font2.render('Alarm active', True, (0, 200, 0))
    text96b = font2.render('Alarm muted', True, (200, 200, 0))
    text97 = font2.render('All clear', True, (0, 200, 0))
    text98 = font2.render('Caution !!!', True, (200, 200, 0))
    text99 = font2.render('Alarm !!!', True, (200, 0, 0))
    
    # Draw text
    game_window.blit(text0, (780, 0))
    if v1 >= 12.0 and v1 <14.99:
        game_window.blit(text1a, (100, 50))
        alarm = 0
    elif v1 > 11.5 and v1 < 11.99:
        game_window.blit(text1b, (100, 50))
        alarm = 1
    else:
        game_window.blit(text1c, (100, 50))
        alarm = 2
    if v2 >= 12.0 and v2 <14.99:    
        game_window.blit(text2a, (1120, 50))
        alarm = 0
    elif v2 > 11.5 and v2 < 11.9:
        game_window.blit(text2b, (1120, 50))
        alarm = 1
    else:
        game_window.blit(text2c, (1120, 50))
        alarm = 2
    if ost <= 5:    
        game_window.blit(text3a, (100, 100))
        alarm = 1
    elif ost >5 and ost < 30:
        game_window.blit(text3b, (100, 100))
    else:
        game_window.blit(text3c, (100, 100))
        alarm = 1
    if ist <= 5:    
        game_window.blit(text4a, (1120, 100))
        alarm = 2
    elif ist >5 and ist < 25:
        game_window.blit(text4b, (1120, 100))
    else:
        game_window.blit(text4c, (1120, 100))
        alarm = 2
    game_window.blit(text5b, (100, 150))
    game_window.blit(text6b, (1120, 150))
    game_window.blit(text7a, (100, 200))
    game_window.blit(text8a, (1120, 200))
    game_window.blit(text9a, (100, 250))
    game_window.blit(text10a, (1120, 250))
    game_window.blit(text11a, (100, 300))
    game_window.blit(text12a, (1120, 300))
    game_window.blit(text13a, (100, 350))
    game_window.blit(text14a, (1120, 350))
    game_window.blit(text15a, (100, 400))
    game_window.blit(text16a, (1120, 400))
    
    game_window.blit(text96b, (700, 750))
    if alarm == 1:
        game_window.blit(text98, (780, 820))
        yellowled.on()
        redled.off()
        greenled.off()
    elif alarm == 2:
        game_window.blit(text99, (780, 820))
        redled.on()
        yellowled.off()
        greenled.off()
    else:
        game_window.blit(text97, (780, 820))
        greenled.on()
        redled.off()
        yellowled.off()
    # Update our display
    pygame.display.update()

    clock.tick(2)

# Uninitialize all pygame modules and quit the program
pygame.quit()
sys.exit()