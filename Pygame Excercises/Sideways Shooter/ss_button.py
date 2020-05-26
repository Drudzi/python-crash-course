import pygame.font

class Button:
    """A class representing  a button
    msg: str
    type: What kind of button (play, easy, medium, hard)
    button_color: Tuple containing an RGB code
    font_size: int
    """
    
    def __init__(self, game_instance, msg, type, button_color, font_size):
        """Initialize attributes for a button."""
        self.settings = game_instance.settings
        self.screen = game_instance.screen
        self.screen_rect = self.screen.get_rect()

        if type.lower() == 'easy' or 'medium' or 'hard':
            self.width, self.height = self.settings.diff_button_width, self.settings.diff_button_height
        elif type.lower() == 'play':
            self.width, self.height = self.settings.play_button_width, self.settings.play_button_height

        self.button_color = button_color
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, font_size)
        self.rect = pygame.Rect(0, 0, self.width, self.height)

        self._set_x(type)
        self._set_y(type)
        self._prep_msg(msg)

    def _prep_msg(self, msg):
        self.msg_image = self.font.render(msg, True, self.text_color)
        self.msg_rect = self.msg_image.get_rect()
        self.msg_rect.center = self.rect.center

    def _set_x(self, type):
        """Set x pos of button."""
        if type.lower() == 'play':
            self.rect.centerx = self.screen_rect.centerx
        elif type.lower() == 'easy':
            self.rect.right = self.screen_rect.centerx - self.rect.width / 2 - 50
        elif type.lower() == 'medium':
            self.rect.centerx = self.screen_rect.centerx
        elif type.lower() == 'hard':
            self.rect.left = self.screen_rect.centerx + self.rect.width / 2 + 50
    
    def _set_y(self, type):
        """Set y pos of button."""
        if type.lower() == 'play':
            self.rect.centery = self.screen_rect.centery
        elif type.lower() == 'easy' or 'medium' or 'hard':
            self.rect.bottom = self.screen_rect.centery - self.settings.play_button_height / 2 - 50
    
    def draw_button(self):
        """Draw the button onto the screen."""
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_rect)