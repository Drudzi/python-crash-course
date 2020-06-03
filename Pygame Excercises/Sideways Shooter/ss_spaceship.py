import pygame
from pygame.sprite import Sprite

class SpaceShip(Sprite):
    """A class manage the spaceship in the game."""

    def __init__(self, game_instance, image):
        """Initialize attributes of the spaceship."""
        super().__init__()
        self.screen = game_instance.screen
        self.screen_rect = game_instance.screen.get_rect()
        self.settings = game_instance.settings
        
        self.image = pygame.image.load(image)
        self.image.set_colorkey((255, 255, 255))
        if image == 'spaceship_small.bmp':
            self.image.set_alpha(150)

        self.rect = self.image.get_rect()

        self.rect.midleft = self.screen_rect.midleft
        
        self.y = float(self.rect.y)

        self.moving_up = False
        self.moving_down = False
    
    def update(self):
        """Update the position of the spaceship."""
        if self.moving_up and self.rect.top > self.screen_rect.top:
            self.y -= self.settings.spaceship_speed
        
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.spaceship_speed

        self.rect.y = self.y

    def blit_spaceship(self):
        """Draw the spaceship onto the screen."""
        self.screen.blit(self.image, self.rect)
    
    def center_spaceship(self):
        """Center the position of the spaceship."""
        self.rect.midleft = self.screen_rect.midleft
        self.y = float(self.rect.y)