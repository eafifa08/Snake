import pygame


class Snake(pygame.sprite.Sprite):
    def __init__(self, name, length, life, speed, armor, resizable):
        """
        Змея
        :param name: имя
        :param length: длина
        :param life: количество жизней
        :param speed: скорость
        :param armor: броня
        """
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 40))
        self.image.fill(pygame.color.THECOLORS['green'])
        self.rect = self.image.get_rect()
        self.rect.centerx = 20
        self.rect.bottom = 20
        self.name = name
        self.length = length
        self.life = life
        self.speed = speed
        self.armor = armor
        self.resizable = resizable

    def update(self):
        self.speed = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_LEFT]:
            self.speed = -8
        if keystate[pygame.K_RIGHT]:
            self.speed = 8
        self.rect.x += self.speed


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


class Something:
    pass


class GameRound:
    pass
