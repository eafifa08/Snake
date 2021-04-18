import pygame
import random

WIDTH = 400
HEIGHT = 400
CELL_SIZE = 20


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
        self.image = pygame.Surface((CELL_SIZE, CELL_SIZE*3), pygame.SRCALPHA, 32)
        #self.image = pygame.image.load('media\snake_head.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.left = WIDTH // 2
        self.rect.bottom = HEIGHT // 2

        self.head_coordinates = [0, CELL_SIZE*2]
        self.body_coordinates = [self.head_coordinates]
        self.polygon_coordinates = [[0, 0], [0, CELL_SIZE*3], [CELL_SIZE, CELL_SIZE*3], [CELL_SIZE, 0]]

        pygame.draw.polygon(self.image, pygame.color.THECOLORS['red'], self.polygon_coordinates)
        self.mask = pygame.mask.from_surface(self.image)
        #self.image.fill(pygame.color.THECOLORS['green'])
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
        if(self.rect.left >= snake.rect.left and self.rect.top >= snake.rect.top
                and self.rect.right <= snake.rect.right and self.rect.bottom <= snake.rect.bottom):
            self.eaten = True
            snake.eaten += 1
            print('food eaten')
            self.kill()
