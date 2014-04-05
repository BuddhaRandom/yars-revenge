"""

levelends.py

"""

import pygame
from pygame.locals import *
from pygame.sprite import Sprite, Group, collide_mask, spritecollide, groupcollide

from gamestate import GameState

from options import *
from vector import *
from ship import Ship, Bullet
from enemy_base import EnemyBase
from formations import formation, formation_center
from enemy_shield import EnemyShield
from homing_bullet import HomingBullet
from cannon import Cannon

class DeathAnimation(GameState):
    """Plays an animation where the player spins around in a circle
    Other sprites are drawn but stay motionless
    """

    def __init__(self, manager, player, other_sprites):

        self.manager = manager
        self.player = player
        self.other_sprites = other_sprites

        self.tick = 0
        self.delay = 4
        self.total_runtime = 64

    def update(self):

        self.tick += 1

        if self.tick == self.total_runtime:
            self.manager.restart_level()

        elif self.tick % self.delay == 0:
            self.player.turn_right()


    def handle_events(self, events, keys):

        for e in events:
            if e.type == pygame.KEYDOWN:
                if e.key == K_ESCAPE:
                    return False


    def draw(self, screen):

        self.player.draw(screen)

        for curr in self.other_sprites:
            curr.draw(screen)


class WinAnimation(GameState):

    def __init__(self, manager, player):

        self.manager = manager
        self.player = player


    def update(self):

        pass

    
    def handle_events(self, events, keys):

        pass


    def draw(self, screen):

        self.player.draw(screen)