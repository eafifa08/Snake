import pygame
import sys
import Logic

FPS = 5
PATH_TO_DATABASE = "snake.sqlite"
SCREEN_SIZE = (400, 400)
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
food_sprite = pygame.sprite.Group()
snake = Logic.Snake(0, 0, 0, 0, 0, 0, 0)
food = Logic.Food()

food_sprite.add(food)
all_sprite.add(snake)
while True:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    if food.eaten == True:
        print('')
    all_sprite.update()
    food_sprite.update(snake)

    screen.fill(pygame.color.THECOLORS['grey'])
    for i in range(0, SCREEN_SIZE[0]):
        pygame.draw.line(screen, pygame.color.THECOLORS['blue'], (i * CELL_SIZE, 0), (i * CELL_SIZE, SCREEN_SIZE[1]), 2)
    for i in range(0, SCREEN_SIZE[1]):
        pygame.draw.line(screen, pygame.color.THECOLORS['blue'], (0, i * CELL_SIZE), (SCREEN_SIZE[0], i * CELL_SIZE), 2)

    all_sprite.draw(screen)
    food_sprite.draw(screen)
    pygame.display.flip()
