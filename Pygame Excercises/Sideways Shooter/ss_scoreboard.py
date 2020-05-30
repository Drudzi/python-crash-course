import pygame.font

class ScoreBoard:
    """Manage the scoreboard and display it."""

    def __init__(self, game_instance):
        """Initialize attributes for the scoreboard."""
        self.settings = game_instance.settings
        self.stats = game_instance.stats
        
        self.screen = game_instance.screen
        self.screen_rect = self.screen.get_rect()

        self.text_color = (10, 10, 10)
        self.font = pygame.font.SysFont(None, 40)

        self.prep_score()
        self.prep_level()
        self.prep_high_score()

    def prep_score(self):
        """Turn the score into an image and set its position."""
        score_string = str(self.stats.score)
        self.score_image = self.font.render(score_string, True, self.text_color)
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20
    
    def prep_level(self):
        """Turn the level into an image and set its position."""
        level_string = str(self.stats.level)
        self.level_image = self.font.render(level_string, True, self.text_color)
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.screen_rect.right - 20
        self.level_rect.top = self.score_rect.bottom + 10

    def prep_high_score(self):
        """Turn the high score into an image and set its position."""
        high_score_string = str(self.stats.high_score)
        self.high_score_image = self.font.render(high_score_string, True, self.text_color)
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = 20
    
    def check_high_score(self):
        """Check if the score has reached the high score and respond."""
        if self.stats.score > self.stats.high_score:
            self.stats.high_score = self.stats.score
            self.prep_high_score()
    
    def draw_score(self):
        """Display the scoreboard onto the screen."""
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)