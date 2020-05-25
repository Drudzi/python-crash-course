import pygame.font

class ScoreBoard:
    """A class to report scoring information."""

    def __init__(self, ai_game):
        """Initialize scorekeeping attributes."""
        self.settings = ai_game.settings
        self.stats = ai_game.stats
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()

        #Font settings for scoring information:
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)

        #Prepare the initial score image:
        self.prep_score()
        self.prep_high_score()

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
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20
    
    def prep_high_score(self):
        """Turn the high score into a rendered image."""
        high_score = round(self.stats.high_score, -1)
        high_score_str = "{:,}".format(high_score)
        self.high_score_image = self.font.render(high_score_str, True, self.text_color, self.settings.bg_color)

        #Set the high score rect at the top center of screen:
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.screen_rect.top
    
    def check_high_score(self):
        """Check if there is a new high score."""
        if self.stats.score > self.stats.high_score:
            self.stats.high_score = self.stats.score
            self.prep_high_score()
    
    def show_score(self):
        """Draw score to the screen."""
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)