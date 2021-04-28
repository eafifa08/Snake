import pygame
import pygame_menu
import sys
import Logic
import settings

game_settings = settings.Settings()
pygame.init()
clock = pygame.time.Clock()
pygame.display.set_caption('Game "Snake"')
screen = pygame.display.set_mode((game_settings.screen_width, game_settings.screen_height))

def set_difficulty(value, difficulty):
    print('value: ' + str(value) + ' difficulty: ' + str(difficulty))
    game_settings.set_difficulty(difficulty)

def set_sound(value, sound_on):
    print('value: ' + str(value) + ' sound_on: ' + str(sound_on))
    game_settings.sound_on = sound_on

def show_stats(snake, round_count):
    pygame.font.init()
    myfont = pygame.font.SysFont('Comic Sans MS', 20)
    round = myfont.render(' round # ' + str(round_count+1), True, (0, 0, 0))
    screen.blit(round, (0, 0))
    eaten = myfont.render(' eaten: '+str(snake.eaten) + '/' + str(game_settings.round_max_foods[round_count]), True, (0, 0, 0))
    screen.blit(eaten, (0, 30))
    length = myfont.render(' length: ' + str(snake.length), True, (0, 0, 0))
    screen.blit(length, (0, 60))
    life = myfont.render(' life: '+ str(snake.life), True, (0, 0, 0))
    screen.blit(life, (0, 90))


def draw_lines(is_drawing_lines):
    """Рисование сетки из клеток на фоне: True или False"""
    if is_drawing_lines:
        for i in range(0, game_settings.screen_width):
            pygame.draw.line(screen, pygame.color.THECOLORS['blue'], (i * game_settings.cell_size, 0), (i * game_settings.cell_size,  game_settings.screen_height), 2)
        for i in range(0, game_settings.screen_height):
            pygame.draw.line(screen, pygame.color.THECOLORS['blue'], (0, i * game_settings.cell_size), ( game_settings.screen_width, i * game_settings.cell_size), 2)


def start_the_round(round_count):
    pygame.mouse.set_visible(False)
    screen.fill(pygame.color.THECOLORS['grey'])
    food_sprite = pygame.sprite.Group()
    snake = Logic.Snake(game_settings, screen)
    pygame.display.update()
    foods = []
    for i in range(game_settings.max_food):
        food = Logic.Food(game_settings)
        while food.type != 'food':
            foods.append(food)
            food_sprite.add(food)
            food = Logic.Food(game_settings)
        foods.append(food)
        food_sprite.add(food)
    direction = 'down'
    round_max_food_change = game_settings.round_max_foods[round_count]
    while round_max_food_change > 0 and snake.life > 0:
        clock.tick(game_settings.fpss[round_count])
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                menu.mainloop(screen)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    direction = 'up'
                if event.key == pygame.K_DOWN:
                    direction = 'down'
                if event.key == pygame.K_LEFT:
                    direction = 'left'
                if event.key == pygame.K_RIGHT:
                    direction = 'right'

        screen.fill(pygame.color.THECOLORS['grey'])
        draw_lines(False)
        snake.update(direction)
        direction = snake.direction
        food_sprite.update(snake)
        food_sprite.draw(screen)
        show_stats(snake, round_count)
        pygame.display.flip()
        pygame.display.update()
        for i in range(0, len(foods)):
            if foods[i].eaten and not foods[i].deleted:
                food = Logic.Food(game_settings)
                while food.type != 'food':
                    foods.append(food)
                    food_sprite.add(food)
                    food = Logic.Food(game_settings)
                foods.append(food)
                food_sprite.add(food)
                round_max_food_change -= 1
                foods[i].deleted = True
        if snake.life <= 0:
            menu.mainloop(screen)


def start_the_game():
    start_the_round(0)
    start_the_round(1)
    start_the_round(2)


menu = pygame_menu.Menu('Snake by Sergey Meshkov', game_settings.screen_width, game_settings.screen_height, theme=pygame_menu.themes.THEME_BLUE)
menu.add.button('Play', start_the_game)
menu.add.selector('Difficulty :', [('Easy', 1), ('Normally', 2), ('Hard', 3)], onchange=set_difficulty)
menu.add.selector('Sound :', [('OFF', False), ('ON', True)], onchange=set_sound)
menu.add.text_input('Name :', default='Your Name')
menu.add.button('Quit', pygame_menu.events.EXIT)
menu.mainloop(screen)
