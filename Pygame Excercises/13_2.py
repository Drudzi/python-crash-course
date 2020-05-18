#Creates a screen with 20 stars randomly placed!

import pygame, sys
from random import randint

from pygame.sprite import Sprite

class Star(Sprite):
    """A class representing the star and its attributes."""

    def __init__(self, main_class):
        super().__init__()
        self.screen = main_class.screen
        self.image = pygame.image.load('white_star.png')
        self.rect = self.image.get_rect()
        self.width = self.rect.width
        self.height = self.rect.height

        self.rect.x = self.width
        self.rect.y = self.height


class StarsGrid:
    """A class displaying a simple grid of stars."""

    def __init__(self):
        """Initialize attributes."""
        pygame.init()
        self.screen_width = 800
        self.screen_height = 700
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        self.screen_rect = self.screen.get_rect()
        pygame.display.set_caption('Stars')

        self.stars = pygame.sprite.Group()
        self.random = randint(-10, 10)
        self._create_stargrid()

    def run(self):
        """Main loop."""
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            self.stars.draw(self.screen)
            pygame.display.flip()

    def _create_stargrid(self):
        """Create a grid of stars."""
        star = Star(self)
        for num in range(20):
            self._create_star()

    def _create_star(self):
        """Create a star and place it on the grid."""
        star = Star(self)
        star.rect.x = randint(0, 800)
        star.rect.y = randint(0, 700)
        self.stars.add(star)


stargrid = StarsGrid()
stargrid.run()