import pygame
import pygame_menu
import sys
import Logic

FPS = 2
PATH_TO_DATABASE = "snake.sqlite"
SCREEN_SIZE = (400, 400)
CELL_SIZE = 20
MAX_FOOD = 1
ROUND_MAX_FOOD = 3

pygame.init()
clock = pygame.time.Clock()
pygame.display.set_caption('Snake')
screen = pygame.display.set_mode(SCREEN_SIZE)

def set_difficulty(value, difficulty):
    # Do the job here !
    pass

def start_the_game(ROUND_MAX_FOOD):
    print('play button')
    # screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    screen.fill(pygame.color.THECOLORS['grey'])
    for i in range(0, SCREEN_SIZE[0]):
        pygame.draw.line(screen, pygame.color.THECOLORS['blue'], (i * CELL_SIZE, 0), (i * CELL_SIZE, SCREEN_SIZE[1]), 2)
    for i in range(0, SCREEN_SIZE[1]):
        pygame.draw.line(screen, pygame.color.THECOLORS['blue'], (0, i * CELL_SIZE), (SCREEN_SIZE[0], i * CELL_SIZE), 2)

    pygame.display.update()
    all_sprite = pygame.sprite.Group()
    food_sprite = pygame.sprite.Group()
    snake = Logic.Snake(0, 3, 0, 0, 0, 0, 0)
    foods = []
    for i in range(MAX_FOOD):
        foods.append(Logic.Food())
        food_sprite.add(foods[i])
    all_sprite.add(snake)
    direction = 'down'

    while ROUND_MAX_FOOD > 0:

        clock.tick(FPS)
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                print('escape')
                return None
            if event.type == pygame.KEYDOWN:
                print(str(event.key))
                if event.key == pygame.K_UP:
                    direction = 'up'
                if event.key == pygame.K_DOWN:
                    direction = 'down'
                if event.key == pygame.K_LEFT:
                    direction = 'left'
                if event.key == pygame.K_RIGHT:
                    direction = 'right'


        all_sprite.update(direction)
        food_sprite.update(snake)

        screen.fill(pygame.color.THECOLORS['grey'])
        for i in range(0, SCREEN_SIZE[0]):
            pygame.draw.line(screen, pygame.color.THECOLORS['blue'], (i * CELL_SIZE, 0),
                             (i * CELL_SIZE, SCREEN_SIZE[1]), 2)
        for i in range(0, SCREEN_SIZE[1]):
            pygame.draw.line(screen, pygame.color.THECOLORS['blue'], (0, i * CELL_SIZE),
                             (SCREEN_SIZE[0], i * CELL_SIZE), 2)

        all_sprite.draw(screen)
        food_sprite.draw(screen)
        pygame.display.flip()
        pygame.display.update()
        for i in range(0, len(foods)):
            if foods[i].eaten and foods[i].deleted == False:
                food = Logic.Food()
                foods.append(food)
                food_sprite.add(food)
                ROUND_MAX_FOOD -= 1
                foods[i].deleted = True


menu = pygame_menu.Menu('Welcome', 400, 400, theme=pygame_menu.themes.THEME_DEFAULT)

menu.add.text_input('Name :', default='Sergey')
menu.add.selector('Difficulty :', [('Hard', 1), ('Easy', 2)], onchange=set_difficulty)
menu.add.button('Play', start_the_game, ROUND_MAX_FOOD)
menu.add.button('Quit', pygame_menu.events.EXIT)
menu.mainloop(screen)


