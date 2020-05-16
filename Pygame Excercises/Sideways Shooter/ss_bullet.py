import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """A class representing the bullets in the game."""

    def __init__(self, game_instance):
        """Initialize attributes for bullets."""
        super().__init__()
        
        self.screen = game_instance.screen
        self.settings = game_instance.settings
        self.image = pygame.image.load('laser_bullet.bmp')
        self.rect = self.image.get_rect()

        #Set bullets default pos to ship's midleft pos:
        self.rect.midright = game_instance.spaceship.rect.midright

        self.x = float(self.rect.x)

    def update(self):
        """Update the position of the bullet."""
        self.x += self.settings.bullet_speed
        self.rect.x = self.x
    
    def blit_bullet(self):
        """Draw the bullet onto the screen."""
        self.screen.blit(self.image, self.rect)