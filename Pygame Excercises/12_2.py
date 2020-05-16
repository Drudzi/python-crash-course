import pygame

pygame.init()

class Image:
    """Show the image."""

    def __init__(self, image_file):
        """Initialize image resources."""
        self.screen = pygame.display.set_mode((800,600))
        self.screen_rect = self.screen.get_rect()
        
        self.image = pygame.image.load(image_file)
        self.image_rect = self.image.get_rect()

        self.image_rect.center = self.screen_rect.center

    def display_image(self):
        self.screen.blit(self.image, self.image_rect)

image = Image('ship.bmp')

running = True
while running:
    image.screen.fill((230, 230, 230))
    image.display_image()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    pygame.display.flip()