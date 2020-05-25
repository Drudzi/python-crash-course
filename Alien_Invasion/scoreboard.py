import pygame.font
from pygame.sprite import Group

from ship import Ship

class ScoreBoard:
    """A class to report scoring information."""

    def __init__(self, ai_game):
        """Initialize scorekeeping attributes."""
        self.ai_game = ai_game
        self.settings = ai_game.settings
        self.stats = ai_game.stats
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()

        #Font settings for scoring information:
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 40)

        #Prepare the initial score image:
        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_ships()

    def prep_score(self):
        """Turn the score into a rendered image."""
        rounded_score = round(self.stats.score, -1) #Round score to nearest 10-value.
        score_str = "{:,}".format(rounded_score)
        #The above 'string formatting directive' tells Python to insert commas into numbers...
        # when converting a numerical value to a string.
        #  ex) 1,000,000 instead of 1000000
        self.score_image = self.font.render(score_str, True, self.text_color, self.settings.bg_color)
        #We set the text img's background to the screen's background, to make it appear transparent.
        
        #Display the score at the top right of the screen:
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 15
        self.score_rect.top = 15
    
    def prep_high_score(self):
        """Turn the high score into a rendered image."""
        high_score = round(self.stats.high_score, -1)
        high_score_str = "{:,}".format(high_score)
        self.high_score_image = self.font.render(high_score_str, True, self.text_color, self.settings.bg_color)

        #Set the high score rect at the top center of screen:
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.screen_rect.top + 15
    
    def prep_level(self):
        """Turn the level into a rendered image."""
        level_str = str(self.stats.level)
        self.level_image = self.font.render(level_str, True, self.text_color) #, self.settings.bg_color)

        #Position the level image below the score:
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 10

    def prep_ships(self):
        """Show how many ships the player has left."""
        self.ships = Group()
        for ship_number in range(self.stats.ships_left):
            ship = Ship(self.ai_game)
            ship.rect.x = 10 + ship_number * ship.rect.width * 1.2
            ship.rect.y = 10
            self.ships.add(ship)
    
    def check_high_score(self, ai_game):
        """Check if there is a new high score."""
        if self.stats.score > self.stats.high_score:
            self.stats.after_high_score_kill_count += 1
            if self.stats.after_high_score_kill_count == 1:
                ai_game.high_score_sound.play()
            self.stats.high_score = self.stats.score
            self.prep_high_score()
    
    def show_score(self):
        """Draw scores and level to the screen."""
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        self.ships.draw(self.screen)