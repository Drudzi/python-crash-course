import pygame.font

class DifficultyButton:
    """Manage the easy-difficulty button."""

    def __init__(self, ai_game, msg, button_color):
        """Initialize attributes for the button."""
        self.settings = ai_game.settings
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()

        self.width = 150
        self.height = 80
        self.text_color = (255, 255, 255)
        self.font = pygame.sysfont(None, 40)

        self.rect = pygame.Rect(0, 0, self.width, self.height)
        #Setting y-pos at the top of the screen:
        self.rect.top = self.screen_rect.top
    
    def _prep_msg(self, msg, button_color):
        """Turn text into a rendered image and set its position."""
        self.msg_image = self.font.render(msg, True, self.text_color, button_color)
        self.msg_rect = self.msg_image.get_rect()
        self.msg_rect.center = self.rect.center


class EasyButton(DifficultyButton):
    """Manage the easy-button and set attributes."""
    
    def __init__(self, ai_game, msg, button_color):
        """Initialize attributes for the easy-button."""
        super().__init__(ai_game, msg, button_color)

        #Set easy-button's x pos:
        self.rect.right = self.screen_rect.centerx - (self.width / 2) - 50


class MediumButton(DifficultyButton):
    """Manage the medium-button and set attributes."""
    
    def __init__(self, ai_game, msg, button_color):
        """Initialize attributes for the medium-button."""
        super().__init__(ai_game, msg, button_color)

        #Set medium-button's x pos:
        self.rect.centerx = self.screen_rect.centerx


class HardButton(DifficultyButton):
    """Manage the hard-button and set attributes."""
    
    def __init__(self, ai_game, msg, button_color):
        """Initialize attributes for the hard-button."""
        super().__init__(ai_game, msg, button_color)

        #Set hard-button's x pos:
        self.rect.left = self.screen_rect.centerx + (self.width / 2) + 50