import sys #We use sys to exit the game when player quits.

#Let's import pygame module, which contains the functionality we need to make a game.
import pygame

from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien


class AlienInvasion:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init() #Initializes pygame.
        self.settings = Settings() #Creating instance for our settings from settings.py.

        monitor_size = [pygame.display.Info().current_w, pygame.display.Info().current_h]
        #self.screen = pygame.display.set_mode(monitor_size, pygame.FULLSCREEN)
        #self.settings.screen_width = self.screen.get_rect().width
        #self.settings.screen_height = self.screen.get_rect().height
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion") #Title the game window.

        self.ship = Ship(self) #We make an instance of our ship.
        #Ship() requires one argument, an instance of AlienInvasion.
        #The self argument I passed refers to whatever current instance of AlienInvasion we are working with.
        
        self.bullets = pygame.sprite.Group()
        #This group class is like a list with some more functionality to it...
        # practical when building games.
        self.aliens = pygame.sprite.Group()

        self._create_fleet()

    def run_game(self):
        """Start the main loop for the game."""
        while True:
        #This while loop is continually running the game.
            self._check_events()
            self.ship.update()
            self._update_bullets()            
            self._update_screen()

    def _check_events(self):
        #This is a helper method, used to simplify code inside class.
        #Helper methods are named beginning with an underscore: def _helper_method.
        """Respond to keypresses and mouse events."""
        
        #Watch for keyboard and mouse events:
        for event in pygame.event.get(): 
            #This event loop looks for events (pressed keys and mouse movements etc.)
            #pygame.event.get() gives a list of events that have taken place since last time function was called.
            #Inside this loop, we write series of if-statements to detect and respond to specific events.
                
            if event.type == pygame.QUIT: #If player clicks at window's close button, pygame.QUIT() is detected.
                sys.exit() #Exits the game.
            
            elif event.type == pygame.KEYDOWN:      #If a key is pressed down...
                self._check_keydown_events(event)
            
            elif event.type == pygame.KEYUP: #If a key is released...
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        """Respond to keypresses."""
        if event.key == pygame.K_RIGHT:     #If right arrow key is pressed...
            #Move the ship to the right:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT: #If left arrow key is pressed...
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            #If q is pressed, exit the game.
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_events(self, event):
        """Respond to key releases."""
        if event.key == pygame.K_RIGHT: #If right arrow key is released...
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT: #If left arrow key is released...
            self.ship.moving_left = False

    def _fire_bullet(self):
        """Create a new bullet and add it to the bullets group."""
        if len(self.bullets) < self.settings.bullets_allowed: #This line allows only 3 bullets at once.
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet) #add() is similar to append, but specific for pygame groups.

    def _update_bullets(self):
        """Update position of bullets and get rid of old bullets."""
        #Update bullet positions:
        self.bullets.update()
        #When you call update() on a sprite Group, it automatically updates each sprite in the group.

        #Get rid of bullets that have disappeared:
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

    def _create_fleet(self):
        """Create the fleet of Aliens."""
        #Make an alien:
        alien = Alien(self)
        alien_width = alien.rect.width
        
        #Find number of aliens that can be placed in a row, with a certain spacing in between:
        available_space_x = self.settings.screen_width - (2 * alien_width)
        number_aliens_x = available_space_x // (2 * alien_width)
        
        #Create the first row of aliens:
        for alien_number in range(number_aliens_x):
            #Create an alien and place it in the row:
            alien = Alien(self)
            alien.x = alien_width + 2 * alien_width * alien_number
            alien.rect.x = alien.x
            self.aliens.add(alien)

    def _update_screen(self): #Also a HELPER method.
        """Update images on the screen, and flip the new screen."""

        #Redraw the screen:
        self.screen.fill(self.settings.bg_color) #fill() takes a color and fills the background.
        self.ship.blit_ship() #We draw the ship on top of the background after filling the background.

        for bullet in self.bullets.sprites(): #sprites() returns a list of all sprites in group.
            bullet.draw_bullet()
        
        self.aliens.draw(self.screen)
        #Make the most recently drawn screen visible:
        pygame.display.flip()
        #pygame.display.flip() draws an empty screen every time we pass through the while loop and erases the old screen.


if __name__ == '__main__':
    #Make a game instance, and run the game.
    ai = AlienInvasion() #We create an instance of the game.
    ai.run_game() #We run it!