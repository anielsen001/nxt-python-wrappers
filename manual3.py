#!/usr/bin/env python
#
# this is an experiment in using pygame to create a manual interface
# to drive the robot
#
# pygame reference at:
# https://www.pygame.org/docs/tut/PygameIntro.html
# and
# https://stackoverflow.com/questions/19370622/pygame-simple-bouncing-animation
#
# key press info here:
# https://stackoverflow.com/questions/16044229/how-to-get-keyboard-input-in-pygame

from __future__ import print_function

import nxt, thread, time
import numpy as np
import drive
from nxt.bluesock import BlueSock

# configure NXT brick for drive
ID1 = '00:16:53:17:52:EE' # MAC address
sock1 = BlueSock(ID1)
b1 = sock1.connect()
mx = nxt.Motor(b1, nxt.PORT_A) # left-side
my = nxt.Motor(b1, nxt.PORT_B) # right-side

d = drive.Drive(mx,my)

import pygame
pygame.init()

window_w = 800
window_h = 600

white = (255, 255, 255)
black = (0, 0, 0)

FPS = 120

window = pygame.display.set_mode((window_w, window_h))
pygame.display.set_caption("DonnaBot: ")
clock = pygame.time.Clock()

# set a lock on key presses to the key that's locked
KEY_LOCK = None

def drive_loop():

    running = True

    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print( "quitting..." )
                pygame.quit()
                return None
                #quit()

            # every key down must be followed by a release key up
            # before the next key down will do anything
                
            if event.type == pygame.KEYDOWN and not KEY_LOCK :
                # only look at another KEYDOWN event if the
                # KEY_LOCK  is not set
                if event.key == pygame.K_UP or \
                   event.key == pygame.K_W : 
                    # move forward 
                    d.forward()
                    
                if event.key == pygame.K_DOWN or\
                   event.key == pygame.K_S : 
                    # move reverse
                    d.reverse()
                
                if event.key == pygame.K_LEFT or\
                   event.key == pygame.K_A :
                    # turn left
                    d.turnInPlace(turnLeft = True)
                    
                if event.key == pygame.K_RIGHT or\
                   event.key == pygame.K_D :
                    # turn right
                    d.turnInPlace(turnLeft = False)

                # set KEY_LOCK to key that was pressed
                KEY_LOCK = event.key
                                       
            if event.type == pygame.KEYUP:
                
                if event.key == KEY_LOCK:
                    # if the released key is the locked key, then stop
                    # the drive, and unset KEY_LOCK
                    d.brakeAll()
                    KEY_LOCK = None
                
   
        # DRAW
        window.fill(white)
        pygame.draw.rect(window, black, [pos_x, pos_y, block_size, block_size])
        pygame.display.update()
        clock.tick(FPS)


if __name__=='__main__':
    drive_loop()
    b1.close()
