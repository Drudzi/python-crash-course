import pygame

class Settings:
    """A class to manage and store all settings for Sideways Shooter."""

    def __init__(self):
        """Initialize settings."""
        self.screen_width = 1100
        self.screen_height = 734
        self.background_image = pygame.image.load('sky_background.bmp')
        self.background_color = (255, 255, 255)

        self.difficulty = 'easy'
        self.speedup_scale = 1.1
        self.score_scale = 1.5

        #Spaceship settings:
        self.spaceship_limit = 3
        
        #Bullet settings:
        self.amount_bullets_allowed = 3

        #Enemies settings:
        self.amount_enemies_fleet = 14  
        self.enemy_spawn_delay = 150 #pixels

        #Button settings:
        self.play_button_width = 200
        self.play_button_height = 100
        
        self.diff_button_width = 120
        self.diff_button_height = 70

        self.active_diff_text_color = (50, 50, 50)
    
    def initialize_dynamic_settings(self):
        self.enemy_speed = 0.3
        self.bullet_speed = 1.0
        self.spaceship_speed = 1.1

        self.kill_score = 100
    
    def increase_speed(self):
        """Increase the speed of the game."""
        self.enemy_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.kill_score *= self.score_scale
