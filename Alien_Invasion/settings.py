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

        self.ship_speed = 1.5 #Setting amount of pixels moved each pass through the loop.

        #Bullet settings:
        self.bullet_speed = 1.5
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60,60,60)
        self.bullets_allowed = 3

        #Alien settings:
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10.0
        self.fleet_direction = 1
       # fleet_direction of 1 represents right; -1 represents left.