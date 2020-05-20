import pygame, sys

from pygame.sprite import Sprite

class Rain:
    """A class representing a raindrop scenario."""

    def __init__(self):
        """Initialize attributes necessary for the raindrops."""
        self.screen = pygame.display.set_mode((700, 600))
        self.screen_rect = self.screen.get_rect()
        self.raindrop = pygame.Rect(0, 0, 10, 20)

    def run(self):
        """The main loop running the visualization."""
        while True:
            self.screen.fill((0, 0, 0))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            pygame.display.flip()


instance = Rain()
instance.run()