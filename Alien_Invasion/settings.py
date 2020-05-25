#With big projects, it's good to spread out fundamental parts into separate files...
# to get a cleaner main program.

#Lets add settings into this module called settings.py.

class Settings:
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initialize the game's settings."""
        #Scren settings:
        self.screen_width = 1100
        self.screen_height = 734
        self.bg_color = (230, 230, 230)

        #Sounds:
        self.bullet_sound = 'sounds/laser.wav'
        self.alien_kill_sound = 'sounds/explosion.wav'
        self.level_up_sound = 'sounds/level_up_tone.wav'
        self.high_score_sound = 'sounds/high_score.wav'

        #Ship settings:
        self.ship_limit = 3

        #Bullet settings:
        self.bullet_width = 4
        self.bullet_height = 15
        self.bullet_color = (60,60,60)
        self.bullets_allowed = 3

        #Alien settings:
        self.fleet_drop_speed = 10.0
        
        #How quickly the game speeds up:
        self.speedup_scale = 1.1
        self.difficulty = 'easy' #Defaults game-difficulty to easy.

        #How quickly the alien-point-values increase:
        self.score_scale = 1.5

        #Difficulty-buttons' settings:
        self.easy_button_color = (0, 150, 0)
        self.medium_button_color = (170, 170, 0)
        self.hard_button_color = (150, 0, 0)
        self.active_difficulty_text_color = (50, 50, 50)

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Initialize settings that can change during the game."""
        self.ship_speed = 1.5 #Setting amount of pixels moved each pass through the loop.
        self.bullet_speed = 1.5  
        self.alien_speed = 1.0   

        self.fleet_direction = 1
        #fleet_direction of 1 represents right; -1 represents left.

        #Scoring:
        self.alien_points = 50
    
    def increase_speed(self):
        """Increase speed settings and alien-point-values."""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)
        #Converting it to int for simplicity and a clean score value.