import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
    """A class to manage the ship."""

    def __init__(self, ai_game): #Argument AlienInvasion instance to get access to all the game resources.
        """Initialize the ship and set its starting position."""
        super().__init__()
        self.screen = ai_game.screen #This lets us work with the AI screen in this class.
        self.screen_rect = ai_game.screen.get_rect() #We access the screen's rectangle values with get_rect().
        self.settings = ai_game.settings #We access game settings in the ship methods.

        #Load the ship image and get its rect (rectangle):
        self.image = pygame.image.load('images/ship.bmp') #Loading 'ship.bmp' into self.class as a surface object.
        self.rect = self.image.get_rect() #We access the rectangle values of the ship image, so we later can place it.

        #When you work with a rect object, you can use x- and y-coordinates of the top, bottom, left and right edges...
        # of the rectangle as well as the center, to place the object.

        #When you're centering a game object, work with the center, center x and centery attributes of a rect.
        #When working at an edge of the screen, work with top, bottom, left or right attributes.
        #You can also combine these with midbottom, midtop, midleft and midright.

        #When you're adjusting the horizontal or vertical placement of rect object, you can use its x- and y.
        #The x and y coordinates of a rect object is at its top-left corner.

        #On the pygame screen, coordinates (0, 0) are at top-left. X increases as you go right and Y increases as you go down.

        #Start each new ship at the bottom center of the screen:
        self.rect.midbottom = self.screen_rect.midbottom
        #Set's the position of self.rect to midbottom of the screen.
       
        #We place the ship-rect at midbottom of screen by...
        # matching its midbottom values with the midbottom values of the screen.

        #Store a decimal value for the ship's horizontal position:
        self.x = float(self.rect.x)

        #Movement flags:
        self.moving_right = False
        self.moving_left = False
    
    def update(self):
        """Update the ship's position based on the movement flag."""
        #Update the ship's x value, not the rect.
        if self.moving_right and self.rect.right < self.screen_rect.right:
            #if right arrow key is pressed and right edge (x) of ship rect is less than right egde (x) of screen...
            #This doesn't allow the ship to move out of the actual screen.
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0: #Same thing as above, we check the moving flag and position.
            self.x -= self.settings.ship_speed
        
        #Update rect object from self.x:
        self.rect.x = self.x
        #You can't modify rect attributes such as x or y with decimal values, only integers...
        # so if you give it a float value, it will always round it and convert in into integer.

        #Using float in self.x, we can store an accurate(detailed) x value and choose any float we want as the ship_speed.
        #The self.x will contain the exact x value we want the ship to be at...
        # but the actual self.rect.x will round that x value off to the closest integer.
        #Even though it won't be perfect, it will be compleeetely fine for displaying it.
    
    def blit_ship(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect) 
        #blit() wants 1. a source (image), and 2. a destination for it, which is self.rect in this case.
    
    def center_ship(self):
        """Center the position of the ship."""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)