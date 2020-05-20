import pygame, sys
from random import randint

from pygame.sprite import Sprite

class Raindrop(Sprite):
    """Rain drops."""
    
    def __init__(self, main_class):
        """Init raindrop attributes."""
        super().__init__()
        self.screen = main_class.screen
        self.rect = pygame.Rect(randint(0, 700), randint(-600, 0), 5, 15)
        self.color = (251, 251, 251)
        self.y = float(self.rect.y)
        self.fall_speed = 1.0
    
    def update(self):
        """Update the positions of the raindrops."""
        self.y += self.fall_speed
        self.rect.y = self.y

    def draw_raindrop(self):
        """Draw raindrop onto the screen."""
        pygame.draw.rect(self.screen, self.color, self.rect)


class Rain:
    """A class representing a raindrop scenario."""

    def __init__(self):
        """Initialize attributes necessary for the visualization."""
        pygame.init()
        self.screen_width = 700
        self.screen_height = 600
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        self.screen_rect = self.screen.get_rect()
        pygame.display.set_caption('Rainfall')
        self.raindrop = Raindrop(self)
        self.raindrops = pygame.sprite.Group()

    def run(self):
        """The main loop running the visualization."""
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            self._create_rainfall()
            self._update_rainfall()
            self._update_screen()
            print(len(self.raindrops))
    
    def _update_rainfall(self):
        """Update the positions of all raindrops in the rainfall."""
        self._check_disappear()
        self.raindrops.update()
    
    def _create_rainfall(self):
        raindrop = Raindrop(self)
        while len(self.raindrops) <= 60:
            self._create_raindrop()
    
    def _create_raindrop(self):
        """Make a raindrop and set it to a random position."""
        raindrop = Raindrop(self)
        # raindrop.rect.x = randint(0, 700)
        # raindrop.rect.y = randint(0, 600)
        self.raindrops.add(raindrop)

    def _check_disappear(self):
        """Check whether a raindrop's y has reached the bottom and delete if that's the case."""
        for raindrop in self.raindrops.sprites():
            if raindrop.rect.y >= self.screen_height:
                self.raindrops.remove(raindrop)

    def _update_screen(self):
        self.screen.fill((5, 5, 5))
        for raindrop in self.raindrops.sprites():
                raindrop.draw_raindrop()
        pygame.display.flip()


instance = Rain()
instance.run()