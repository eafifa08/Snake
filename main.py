import pygame
import sys

FPS = 60
PATH_TO_DATABASE = "snake.sqlite"
SCREEN_SIZE = (200, 200)
CELL_SIZE = 20

pygame.init()
clock = pygame.time.Clock()
pygame.display.set_caption('Snake')
screen = pygame.display.set_mode(SCREEN_SIZE)
#screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
screen.fill(pygame.color.THECOLORS['grey'])
for i in range(0, SCREEN_SIZE[0]):
    pygame.draw.line(screen, pygame.color.THECOLORS['blue'], (i*CELL_SIZE, 0), (i*CELL_SIZE, SCREEN_SIZE[1]), 2)
for i in range(0, SCREEN_SIZE[1]):
    pygame.draw.line(screen, pygame.color.THECOLORS['blue'], (0, i*CELL_SIZE), (SCREEN_SIZE[0], i*CELL_SIZE), 2)

pygame.display.update()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()