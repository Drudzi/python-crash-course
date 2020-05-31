import pygame

class GameStats:
    """Manage the statistics in the SS game."""

    def __init__(self, game_instance):
        self.settings = game_instance.settings
        self.reset_stats()
        
        self.game_active = False

        try:
            with open('high_score.txt') as f:
                self.stored_hs = f.read()
                if not self.stored_hs:
                    self.stored_hs = 0
        except FileNotFoundError:
            self.stored_hs = 0
        
        self.high_score = int(self.stored_hs)

    def reset_stats(self):
        self.spaceships_used = 0
        self.score = 0
        self.level = 1
    
    def save_high_score(self):
        """Save the high score into a text file."""
        hs_str = str(self.high_score)
        with open('high_score.txt', 'w') as f:
            f.write(hs_str)