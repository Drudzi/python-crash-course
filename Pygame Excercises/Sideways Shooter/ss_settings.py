import pygame

class Settings:
    """A class to manage and store all settings for Sideways Shooter."""

    def __init__(self):
        """Initialize settings."""
        self.screen_width = 1100
        self.screen_height = 734
        self.background_image = pygame.image.load('sky_background.bmp')
        self.background_color = (255, 255, 255)

        #Spaceship settings:
        self.spaceship_speed = 1.3
        
        #Bullet settings:
        self.bullet_speed = 1.0
        self.amount_bullets_allowed = 3

        #Enemies settings:
        self.amount_enemies_fleet = 10
        self.enemy_speed = 0.2
        self.enemy_spawn_delay = 150 #pixels