"""

event_handlers.py

Contains different generic methods to handle key inputs and other events

All methods return false if a quit condition is met and true otherwise

"""

import pygame
from pygame.locals import *

import vector

def check_quit(events, keys):
    """Checks for quit keys (e.g. esc)"""
    
    for e in events:
        if e.type == KEYDOWN and e.key == K_ESCAPE:
            return False
            
    return True


def move_player(events, keys, player):
    """Checks for player movement keys and moves player accordingly"""
    
    if keys[K_UP] and keys[K_RIGHT]:
        player.move(vector.NORTHEAST)
    elif keys[K_UP] and keys[K_LEFT]:
        player.move(vector.NORTHWEST)
    elif keys[K_DOWN] and keys[K_RIGHT]:
        player.move(vector.SOUTHEAST)
    elif keys[K_DOWN] and keys[K_LEFT]:
        player.move(vector.SOUTHWEST)
    elif keys[K_LEFT]:
        player.move(vector.WEST)
    elif keys[K_RIGHT]:
        player.move(vector.EAST)
    elif keys[K_UP]:
        player.move(vector.NORTH)
    elif keys[K_DOWN]:
        player.move(vector.SOUTH)

    return True


def check_shoot_button(events, keys, action):
    """Checks for the shoot buttons (e.g. space)
    
    action is a no-args function which should be called if the button is pressed"""
    
    for e in events:
        if e.type == KEYDOWN and e.key == K_SPACE:
            action()
    
    return True
