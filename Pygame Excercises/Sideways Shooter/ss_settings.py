import pygame

class Settings:
    """A class to manage and store all settings for Sideways Shooter."""

    def __init__(self):
        """Initialize settings."""
        self.screen_width = 1100
        self.screen_height = 734
        self.background_image = pygame.image.load('sky_background.bmp')
        self.background_color = (255, 255, 255)

        self.spaceship_speed = 1.0