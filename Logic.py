import pygame

WIDTH = 400
HEIGHT = 400


class Snake(pygame.sprite.Sprite):
    def __init__(self, name, length, life, speed, armor, resizable, direction):
        """
        Змея
        :param name: имя
        :param length: длина
        :param life: количество жизней
        :param speed: скорость
        :param armor: броня
        """
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((20, 20))
        self.image.fill(pygame.color.THECOLORS['green'])
        self.rect = self.image.get_rect()
        self.rect.centerx = 0
        self.rect.bottom = 0
        self.direction = 'down'
        self.name = name
        self.length = length
        self.life = life
        self.speed_x = 0
        self.speed_y = 0
        self.armor = armor
        self.resizable = resizable


    def update(self):
        #self.speed = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_LEFT]:
            self.speed_x = -5
            self.speed_y = 0
            self.direction = 'left'
        if keystate[pygame.K_RIGHT]:
            self.speed_x = 5
            self.speed_y = 0
            self.direction = 'right'
        if keystate[pygame.K_DOWN]:
            self.speed_y = 5
            self.speed_x = 0
            self.direction = 'down'
        if keystate[pygame.K_UP]:
            self.speed_y = -5
            self.speed_x = 0
            self.direction = 'up'
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
        self.image = pygame.Surface((20, 20))
        self.image.fill(pygame.color.THECOLORS['blue'])
        self.rect = self.image.get_rect()
        self.rect.centerx = 300
        self.rect.bottom = 300
        self.eaten = False


    def update(self, snake):
        if(self.rect.left >= snake.rect.left and self.rect.top >= snake.rect.top
                and self.rect.right <= snake.rect.right and self.rect.bottom <= snake.rect.bottom):
            self.eaten = True
            self.kill()





class GameRound:
    pass
