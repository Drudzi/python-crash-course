import pygame, sys

from pygame.sprite import Sprite

class Raindrop(Sprite):
    """Rain drops."""
    
    def __init__(self, main_class):
        """Init raindrop attributes."""
        super().__init__()
        self.screen = main_class.screen
        self.rect = pygame.Rect(0, 0, 4, 11)
        self.color = (251, 251, 251)
        self.y = float(self.rect.y)
        self.fall_speed = 0.5
    
    def update(self):
        """Update the positions of the raindrops."""
        self.y += self.fall_speed
        self.rect.y = int(self.y)

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

        #Initial attributes for _create_rainfall():
        self.available_space_x = self.screen_width # - self.screen_width // 10
        self.number_drops_x = self.available_space_x // (self.screen_width // 20)
        self.available_space_y = self.screen_height + self.screen_height // 20
        self.number_rows_y = self.available_space_y // (self.screen_height // 20)

        self._create_rainfall()

    def run(self):
        """The main loop running the visualization."""
        while True:
            self._check_events()
            self._update_rainfall()
            self._update_screen()
    
    def _check_events(self):
        """Check for user events."""
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        sys.exit()
    
    def _update_rainfall(self):
        """Update the positions of all raindrops in the rainfall."""
        self._check_disappear()
        self.raindrops.update()
        self._create_rain_row()
    
    def _create_rainfall(self):
        raindrop = Raindrop(self)

        for row_number in range(self.number_rows_y):
            for drop_number in range(self.number_drops_x):
                self._create_raindrop(drop_number, row_number)
    
    def _create_rain_row(self):
        """Create a new row of raindrops when a row hits bottom edge."""
        if len(self.raindrops) <= (self.number_drops_x * self.number_rows_y - self.number_drops_x):
            for row_number in range(1):
                for drop_number in range(self.number_drops_x):
                    self._create_raindrop(drop_number, row_number)
    
    def _create_raindrop(self, drop_number, row_number):
        """Make a raindrop and set it to a random position."""
        raindrop = Raindrop(self)
        raindrop.rect.x = (self.screen_width // 20) + (self.screen_width // 20) * drop_number
        raindrop.y = (self.screen_height // 20) * row_number - self.screen_height // 20
        raindrop.rect.y = raindrop.y
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