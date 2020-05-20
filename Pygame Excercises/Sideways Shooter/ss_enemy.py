from random import randint

import pygame
from pygame.sprite import Sprite

class Enemy(Sprite):
    """A class to manage the enemies (targets) in the game."""
    
    def __init__(self, game_instance):
        super().__init__()

        self.settings = game_instance.settings
        self.screen = game_instance.screen
        self.screen_rect = self.screen.get_rect()

        image_filename = 'enemy.bmp'
        self.image = pygame.image.load(image_filename)
        self.image.set_colorkey((255, 255, 255))
        self.rect = self.image.get_rect()
        self.width, self.height = self.rect.size

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
    
    def update(self):
        self.x -= self.settings.enemy_speed
        self.rect.x = int(self.x)
