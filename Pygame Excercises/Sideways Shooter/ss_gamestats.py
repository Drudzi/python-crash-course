import pygame

class GameStats:
    """Manage the statistics in the SS game."""

    def __init__(self, game_instance):
        self.settings = game_instance.settings
        self.reset_stats()
        
        self.game_active = False

        self.high_score = 0

    def reset_stats(self):
        self.spaceships_used = 0
        self.score = 0
        self.level = 1