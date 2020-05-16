import pygame, sys

pygame.display.set_mode((500, 500))
pygame.display.set_caption('Keys')

while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            print(event.key)
        if event.type == pygame.QUIT:
            sys.exit()