import pygame

class GameStats:
    """Manage the statistics in the SS game."""

    def __init__(self, game_instance):
        self.settings = game_instance.settings
        self.reset_stats()
        
        self.game_active = True

    def reset_stats(self):
        self.spaceships_used = 0
        self.enemies_killed = 0