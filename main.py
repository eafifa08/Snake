import pygame
import sys
import Logic

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
all_sprite = pygame.sprite.Group()
snake = Logic.Snake(0, 0, 0, 0, 0, 0)
all_sprite.add(snake)

while True:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    all_sprite.update()
    screen.fill(pygame.color.THECOLORS['black'])
    all_sprite.draw(screen)
    pygame.display.flip()
