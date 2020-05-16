import pygame

screen_width = 1000
screen_height = 650

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Blue Sky')

running = True
while running:

    screen.fill((0, 0, 255))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()