import pygame
import pygame_menu
import sys
import Logic
import random


class Snake(pygame.sprite.Sprite):
    def __init__(self, name, length, life, speed, armor, resizable, direction, coordinates):
        """
        Змея
        :param name: имя
        :param length: длина
        :param life: количество жизней
        :param speed: скорость
        :param armor: броня
        """
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((CELL_SIZE * 3, CELL_SIZE * 3), pygame.SRCALPHA, 32)
        # self.image = pygame.image.load('media\snake_head.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.left = WIDTH // 2
        self.rect.bottom = HEIGHT // 2
        self.polygon_coordinates = [[0, 0], [0, CELL_SIZE * 3], [CELL_SIZE, CELL_SIZE * 3], [CELL_SIZE, 0]]
        pygame.draw.polygon(self.image, pygame.color.THECOLORS['red'], self.polygon_coordinates)
        self.mask = pygame.mask.from_surface(self.image)
        # self.image.fill(pygame.color.THECOLORS['green'])
        self.direction = 'down'
        self.speed_x = 0
        self.speed_y = 0
        self.eaten = 0

    def update(self, direction):
        if direction == 'up':
            if self.direction != 'down':
                self.speed_y = -20
                self.speed_x = 0
                self.direction = 'up'
        if direction == 'down':
            if self.direction != 'up':
                self.speed_y = 20
                self.speed_x = 0
                self.direction = 'down'
        if direction == 'left':
            if self.direction != 'right':
                self.speed_y = 0
                self.speed_x = -20
                self.direction = 'left'
        if direction == 'right':
            if self.direction != 'left':
                self.speed_y = 0
                self.speed_x = 20
                self.direction = 'right'

        self.image = pygame.Surface((CELL_SIZE * 4, CELL_SIZE * 4), pygame.SRCALPHA, 32)
        self.rect = self.image.get_rect()
        pygame.draw.polygon(self.image, pygame.color.THECOLORS['red'], self.polygon_coordinates)
        self.mask = pygame.mask.from_surface(self.image)

        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT


class Field:
    def __init__(self, size, dangerous_walls, something_good_max):
        """
        Поле
        :param size: ширина,высота
        :param dangerous_walls: столкновение со стеной приводит к гибели
        :param something_good_max: макс.количество полезных сущностей на поле
        """
        self.width, self.height = size
        self.dangerous_walls = dangerous_walls
        self.something_good_max = something_good_max
        self.something_good_min = 0


class Food(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((10, 10))
        self.image.fill(pygame.color.THECOLORS['blue'])
        self.rect = self.image.get_rect()
        self.rect.left = random.randint(1, 399) // 20 * 20
        self.rect.bottom = random.randint(1, 399) // 20 * 20
        self.eaten = False
        self.deleted = False

    def update(self, snake):
        if (self.rect.left >= snake.rect.left and self.rect.top >= snake.rect.top
                and self.rect.right <= snake.rect.right and self.rect.bottom <= snake.rect.bottom):
            self.eaten = True
            snake.eaten += 1
            print('food eaten')
            self.kill()


FPS = 2
PATH_TO_DATABASE = "snake.sqlite"
SCREEN_SIZE = WIDTH, HEIGHT = (400, 400)
CELL_SIZE = 20
MAX_FOOD = 1
ROUND_MAX_FOOD = 3

pygame.init()
clock = pygame.time.Clock()
pygame.display.set_caption('Snake')
screen = pygame.display.set_mode(SCREEN_SIZE)
coordinates = None


def set_difficulty(value, difficulty):
    # Do the job here !
    pass


def start_the_game(ROUND_MAX_FOOD):
    print('play button')
    # screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    coordinates = [[0 for j in range(0, HEIGHT // CELL_SIZE)] for i in range(0, WIDTH // CELL_SIZE)]
    screen.fill(pygame.color.THECOLORS['grey'])
    for i in range(0, SCREEN_SIZE[0]):
        pygame.draw.line(screen, pygame.color.THECOLORS['blue'], (i * CELL_SIZE, 0), (i * CELL_SIZE, SCREEN_SIZE[1]), 2)
    for i in range(0, SCREEN_SIZE[1]):
        pygame.draw.line(screen, pygame.color.THECOLORS['blue'], (0, i * CELL_SIZE), (SCREEN_SIZE[0], i * CELL_SIZE), 2)
    pygame.display.update()
    all_sprite = pygame.sprite.Group()
    food_sprite = pygame.sprite.Group()
    snake = Snake(0, 3, 0, 0, 0, 0, 0, coordinates)
    foods = []
    for i in range(MAX_FOOD):
        foods.append(Food())
        food_sprite.add(foods[i])
    all_sprite.add(snake)
    direction = 'down'

    round_max_food_change = ROUND_MAX_FOOD
    while round_max_food_change > 0:
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
                food = Food()
                foods.append(food)
                food_sprite.add(food)
                round_max_food_change -= 1
                foods[i].deleted = True


menu = pygame_menu.Menu('Welcome', 400, 400, theme=pygame_menu.themes.THEME_DEFAULT)
menu.add.text_input('Name :', default='Sergey')
menu.add.selector('Difficulty :', [('Hard', 1), ('Easy', 2)], onchange=set_difficulty)
menu.add.button('Play', start_the_game, ROUND_MAX_FOOD)
menu.add.button('Quit', pygame_menu.events.EXIT)
menu.mainloop(screen)
