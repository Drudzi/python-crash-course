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

        #Ship settings:
        self.ship_limit = 3

        #Bullet settings:
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60,60,60)
        self.bullets_allowed = 3

        #Alien settings:
        self.fleet_drop_speed = 10.0
        
        #How quickly the game speeds up:
        self.speedup_scale = 1.1

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Initialize settings that can change during the game."""
        self.ship_speed = 1.5 #Setting amount of pixels moved each pass through the loop.
        self.bullet_speed = 1.5  
        self.alien_speed = 1.0   

        self.fleet_direction = 1
        #fleet_direction of 1 represents right; -1 represents left.   
    
    def increase_speed(self):
        """Increase speed settings."""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale