import pygame
import sys

FPS = 60
PATH_TO_DATABASE = "snake.sqlite"

pygame.init()
clock = pygame.time.Clock()
pygame.display.set_caption('Snake')
screen = pygame.display.set_mode((500, 300))
screen.fill(pygame.color.THECOLORS['grey'])
pygame.display.update()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()