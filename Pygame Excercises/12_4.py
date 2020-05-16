import pygame, sys

class RocketGame:
    """A rocket moving around, manage the resources here."""
    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((600, 600))
        self.screen_rect = self.screen.get_rect()

        self.rocket_image = pygame.image.load('rocketship.bmp')
        self.rocket_rect = self.rocket_image.get_rect()

        self.rocket_rect.center = self.screen_rect.center

        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False 

        pygame.display.set_caption('Rocket Ship')
    
    def run_game(self):
        while True:
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        self.moving_right = True
                    elif event.key == pygame.K_LEFT:
                        self.moving_left = True
                    elif event.key == pygame.K_UP:
                        self.moving_up = True
                    elif event.key == pygame.K_DOWN:
                        self.moving_down = True
                
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_RIGHT:
                        self.moving_right = False
                    elif event.key == pygame.K_LEFT:
                        self.moving_left = False
                    elif event.key == pygame.K_UP:
                        self.moving_up = False
                    elif event.key == pygame.K_DOWN:
                        self.moving_down = False

            self.screen.fill((150, 255, 150))
            self._update_rocket()
            self.screen.blit(self.rocket_image, self.rocket_rect)
            pygame.display.flip()

    def _update_rocket(self):
        
        if self.moving_right and self.rocket_rect.right < self.screen_rect.right:
            self.rocket_rect.x += 1
        
        elif self.moving_left and self.rocket_rect.left > 0:
            self.rocket_rect.x -= 1
        
        elif self.moving_up and self.rocket_rect.top > 0:
            self.rocket_rect.y -= 1
        
        elif self.moving_down and self.rocket_rect.bottom < self.screen_rect.bottom:
            self.rocket_rect.y += 1

game = RocketGame()
game.run_game()