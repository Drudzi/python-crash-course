import pygame.font

class DifficultyButton:
    """Manage and set the difficulty button's."""

    def __init__(self, ai_game, msg, button_color, difficulty):
        """Initialize attributes for the button."""
        self.settings = ai_game.settings
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()

        #Create an instance of play-button to refer to while setting positions:
        self.play_button = ai_game.play_button

        self.difficulty = difficulty

        self.width = 95
        self.height = 40
        self.button_color = button_color
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 30)

        self.rect = pygame.Rect(0, 0, self.width, self.height)
        #Setting y-pos at the top of the screen:
        self.rect.bottom = self.play_button.rect.top - self.height
        self._set_x()

        self._prep_msg(msg)
        
    def _prep_msg(self, msg):
        """Turn text into a rendered image and set its position."""
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def _set_x(self):
        """Set the x position of the given difficulty's button."""
        if self.difficulty == 'easy':
            self.rect.right = self.screen_rect.centerx - (self.width / 2) - 30            

        elif self.difficulty == 'medium':
            self.rect.centerx = self.screen_rect.centerx

        elif self.difficulty.lower() == 'hard':
            self.rect.left = self.screen_rect.centerx + (self.width / 2) + 30

    def draw_button(self):
        """Draw the blank button and then the text onto the screen."""
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)