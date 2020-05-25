import pygame

class GameStats:
    """Track statistics for Alien Invasion."""

    def __init__(self, ai_game):
        """Initialize statistics."""
        self.settings = ai_game.settings
        
        self.high_score_file = 'high_score.txt'
        try:
            with open(self.high_score_file, 'r') as f:
                self.stored_high_score = f.read()
                if not self.stored_high_score:
                    self.stored_high_score = 0
        except FileNotFoundError:
            with open(self.high_score_file, 'w') as f:
                f.write('0')

        self.reset_stats()

        #Start Alien Invasion in a false state so the player can start manually:
        self.game_active = False

        #High-score should never be reset:
        self.high_score = int(self.stored_high_score)

    def reset_stats(self):
        """Initialize statistics that can change during the game."""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1
        self.after_high_score_kill_count = 0