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

    def prep_score(self):
        """Turn the score into an image and set its position."""
        score_string = str(self.stats.score)
        self.score_image = self.font.render(score_string, True, self.text_color)
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20
    
    def draw_score(self):
        """Display the scoreboard onto the screen."""
        self.screen.blit(self.score_image, self.score_rect)