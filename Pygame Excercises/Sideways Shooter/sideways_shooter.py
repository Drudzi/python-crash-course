import sys, cProfile

import pygame

from ss_settings import Settings
from ss_spaceship import SpaceShip

class SidewaysShooter:
    """An overall class to manage the game and it's resources and behaviour."""
    
    def __init__(self):
        """Initialize the game and create its resources."""
        pygame.init()

        self.fps = 120
        self.fps_clock = pygame.time.Clock()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Sideways Shooter")

        self.spaceship = SpaceShip(self)
    
    def run_game(self):
        """Method including the main game loop. Runs the game."""
        
        while True:
            self._check_events()
            self.spaceship.update()
            self._update_screen()
        
    def _check_events(self):
        """Respond to user inputs."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        """Check if a key has been pressed."""
        if event.key == pygame.K_UP:
            self.spaceship.moving_up = True
        if event.key == pygame.K_DOWN:
            self.spaceship.moving_down = True
        if event.key == pygame.K_q:
            sys.exit()

    def _check_keyup_events(self, event):
        """Check if key has been released."""
        if event.key == pygame.K_UP:
            self.spaceship.moving_up = False
        if event.key == pygame.K_DOWN:
            self.spaceship.moving_down = False
    
    def _update_screen(self):
        """Update the surfaces on the screen and flip the new one."""
        #self.screen.blit(self.settings.background_image, (0, 0))
        self.screen.fill((self.settings.background_color))
        self.spaceship.blit_spaceship()
        pygame.display.flip()


if __name__ == '__main__':
    game = SidewaysShooter()
    game.run_game()