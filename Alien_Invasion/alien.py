import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """A class to manage aliens in Alien Invasion."""

    def __init__(self, ai_game):
        """Initialize the alien and its starting position."""
        super().__init__()
        
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()

        #Load the alien image and set its rect attribute.
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        #Set the starting position of alien.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        #Store the alien's exact horizontal position.
        self.x = float(self.rect.x)
