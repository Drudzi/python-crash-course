import pygame, sys

from pygame.sprite import Sprite

class Star(Sprite):
    """A class representing the star and its attributes."""

    def __init__(self, main_class):
        super().__init__()
        self.image = pygame.image.load('white_star.png')
        self.rect = self.image.get_rect()


class Starsgrid:
    """A class displaying a simple grid of stars."""

    def __init__(self):
        """Initialize attributes."""
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        self.screen_rect = self.screen.get_rect()
        pygame.display.set_caption('Stars')

        self.stars = pygame.sprite.Group()

    def run(self):
        """Main loop."""
        while True:
           ...

    def _create_stargrid(self):
        """Create a grid of stars."""

    def _create_star(self):
        """Create a star and place it on the grid.""" 