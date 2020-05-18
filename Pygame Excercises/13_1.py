import pygame, sys

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
        self.screen_height = 720
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        self.screen_rect = self.screen.get_rect()
        pygame.display.set_caption('Stars')

        self.stars = pygame.sprite.Group()

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
        star_width, star_height = star.rect.size

        available_space_x = self.screen_width - (2 * star_width)
        number_stars_x = available_space_x // (2 * star_width)

        available_space_y = self.screen_height - (2 * star_height)
        number_stars_y = available_space_y // star_height

        for row_number in range(number_stars_y):
            for star_number in range(number_stars_x):
                self._create_star(star_number, row_number)

    def _create_star(self, star_number, row_number):
        """Create a star and place it on the grid."""
        star = Star(self)
        star_width, star_height = star.rect.size
        star.x = star_width + 2 * star_width * star_number
        star.rect.x = star.x
        star.rect.y = star.rect.height + 2 * star.rect.height * row_number
        self.stars.add(star)


stargrid = StarsGrid()
stargrid.run()