# import all the needed modules
import pygame
import sys
from gpiozero import MCP3008, PWMLED, LED, Button
from signal import pause
import time
import datetime

#alarm v 2.3

# Create width and height constants
WINDOW_WIDTH = 1350
WINDOW_HEIGHT = 700
#setup other constants
pot1 = MCP3008(0)
pot2 = MCP3008(1)
pot3 = MCP3008(2)
pot4 = MCP3008(3)
pot5 = MCP3008(4)
pot6 = MCP3008(5)
pot7 = MCP3008(6)
pot8 = MCP3008(7)
muted = Button(21)
alarm = 0
redled = LED(23)
yellowled = LED(24)
greenled = LED(25)
mutedled = LED(27)
# old testing constants
mbv = 12.1
bbv = 12.1
ost = 10
ist = 17
frt = 0
fzt = -10

ww = WINDOW_WIDTH/2 - 100
ww1 = ww - 190
ww2 = ww - 100
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


# Game loop
while game_running:
    # Loop through all active events
    for event in pygame.event.get():
        # Close the program if the user presses the 'X'
        if event.type == pygame.QUIT:
            game_running = False



    #now = datetime.datetime.today()
    now = '{0:%A - %d - %B - %Y  %H:%M:%S}'.format(datetime.datetime.now())
    #r1=10k r2=2k2 gives 2.9v output from 16v input
    # 18.6 is value of multiplication needed to scale from 0 - 1 to 0 - 15
    v1 = pot1.value*18.6
    v1a = ('{:.1f}'.format(v1))
    #testing v2 = v1
    #v2 = pot2.value*18.6
    v2 = v1
    v2a = ('{:.1f}'.format(v2))
    v3 = pot3.value*100
    v3a = ('{:.0f}'.format(v3))
    v4 = pot4.value*100
    v4a = ('{:.0f}'.format(v4))
    v5 = pot5.value*60-20
    v5a = ('{:.1f}'.format(v5))
    v6 = pot6.value*60-20
    v6a = ('{:.1f}'.format(v6))
     # Fill the window with black / colours in r g b
    game_window.fill((0, 0, 0))
    # define all messages, value, anti alised, colour
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
    text5a = font1.render('Fridge temp  ' + str(frt) + ' C', True, (0, 0, 200))
    text5b = font1.render('Fridge temp  ' + str(frt) + ' C', True, (0, 200, 0))
    text5c = font1.render('Fridge temp  ' + str(frt) + ' C', True, (200, 0, 0))
    text6a = font1.render('Freezer temp ' + str(fzt) + ' C', True, (0, 0, 200))
    text6b = font1.render('Freezer temp ' + str(fzt) + ' C', True, (0, 200, 0))
    text6c = font1.render('Freezer temp ' + str(fzt) + ' C', True, (200, 0, 0))
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
    text15b = font1.render('Downstairs panic buttons pressed', True, (200, 0, 0))
    text16a = font1.render('Upstairs panic buttons clear', True, (0, 200, 0))
    text16b = font1.render('Upstairs panic buttons pressed', True, (200, 0, 0))
    text17a = font1.render('the current date and time is ' +(str(now)), True, (0, 200, 0))
    #text17a = font1.render('Main fuel oil tank ' + str(mft) + ' % full', True, (0, 200, 0))
    # put other messages, value, anti alised, colour items here
    # is alarm muted or active ?
    text96a = font2.render('Alarm active', True, (0, 200, 0))
    text96b = font2.render('Alarm muted', True, (200, 200, 0))
    # the 3 alarm states
    text97 = font2.render('All clear', True, (0, 200, 0))
    text98 = font2.render('Caution !!!', True, (200, 200, 0))
    text99 = font2.render('Alarm !!!', True, (200, 0, 0))
    
    # Draw text
    # alarm = 0 = all clear
    # alarm = 1 = caution state
    # alarm = 2 = alarm state
    
    # test battery voltages
    
    game_window.blit(text0, (ww2, 0))
    if v1 >= 12.0 and v1 <14.99:
        game_window.blit(text1a, (10, 50))
        alarm = 0
    elif v1 > 11.5 and v1 < 11.99:
        game_window.blit(text1b, (10, 50))
        alarm = 1
    else:
        game_window.blit(text1c, (10, 50))
        alarm = 2
    if v2 >= 12.0 and v2 <14.99:    
        game_window.blit(text2a, (700, 50))
        alarm = 0
    elif v2 > 11.5 and v2 < 11.9:
        game_window.blit(text2b, (700, 50))
        alarm = 1
    else:
        game_window.blit(text2c, (700, 50))
        alarm = 2
        
        # test tempratures
        
    if ost <= 5:    
        game_window.blit(text3a, (10, 100))
        alarm = 1
    elif ost >5 and ost < 30:
        game_window.blit(text3b, (10, 100))
    else:
        game_window.blit(text3c, (10, 100))
        alarm = 1
    if ist <= 5:    
        game_window.blit(text4a, (700, 100))
        alarm = 2
    elif ist >5 and ist < 25:
        game_window.blit(text4b, (700, 100))
    else:
        game_window.blit(text4c, (700, 100))
        alarm = 2
        
    # test other inputs
    # need to add logic for testing inputs
        
    game_window.blit(text5b, (10, 150))
    game_window.blit(text6b, (700, 150))
    game_window.blit(text7a, (10, 200))
    game_window.blit(text8a, (700, 200))
    game_window.blit(text9a, (10, 250))
    game_window.blit(text10a, (700, 250))
    game_window.blit(text11a, (10, 300))
    game_window.blit(text12a, (700, 300))
    game_window.blit(text13a, (10, 350))
    game_window.blit(text14a, (700, 350))
    game_window.blit(text15a, (10, 400))
    game_window.blit(text16a, (700, 400))
    game_window.blit(text17a, (10, 450))

    # test alarm states
    # also light LEDs to show alarm muted/active and alarm state
    # green all clear, yellow caution or red alarm
    # need to add logic for mute state LED (done)
    
    if muted.is_pressed:
        game_window.blit(text96b, (ww1, 500))
        mutedled.on()
    else:
        game_window.blit(text96a, (ww1, 500))
        mutedled.off()
        
    # make caution and alarm LEDs blink
    
    if alarm == 1:
        game_window.blit(text98, (ww2, 600))
        yellowled.blink()
        redled.off()
        greenled.off()
    elif alarm == 2:
        game_window.blit(text99, (ww2, 600))
        redled.blink()
        yellowled.off()
        greenled.off()
    else:
        game_window.blit(text97, (ww2, 600))
        greenled.on()
        redled.off()
        yellowled.off()
    # Update our display
    pygame.display.update()

    clock.tick(2)

# Uninitialize all pygame modules and quit the program
pygame.quit()
sys.exit()