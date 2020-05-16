import pygame

from pygame.sprite import Sprite
#Sprite class let's you group related elements in the game and act on all the grouped elements at once.

class Bullet(Sprite):
    #Inheriting from Sprite-class.
    """A class to manage bulltes fired from the ship."""

    def __init__(self, ai_game):
        """Create a bullet object at the ship's current position."""
        super().__init__() #Initializing the init attributes of superclass (parent class).
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        #Create a bullet rect at (0, 0) and then set current position:
        self.rect = pygame.Rect(
            0, 0, self.settings.bullet_width, self.settings.bullet_height)
        #We create the bullet's visual using a basic Rect(), no image atm.
        #When creating a rect from scratch, you also need to give it a position...
        # we give it (0, 0) (any random pos works because we're changing it below.)
        
        self.rect.midtop = ai_game.ship.rect.midtop
        #Here, we give the bullet-rect a new starting position, at the ship.

        #Store the bullet's y-position as a decimal value:
        #This let's us adjust the speed of the bullet in detail.
        self.y = float(self.rect.y)

    def update(self):
        """Move the bullet up the screen."""
        #Update the decimal position of the bullet:
        self.y -= self.settings.bullet_speed #Decrease the y-coordinate, which makes it move up.
        #We'll never change bullet's x, because it shouldn't move sideways.
        #Update the rect position:
        self.rect.y = self.y

    def draw_bullet(self):
        """Draw the bullet onto the screen."""
        pygame.draw.rect(self.screen, self.color, self.rect)