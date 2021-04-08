class Snake:
    def __init__(self, name, length, life, speed, armor, resizable):
        """
        Змея
        :param name: имя
        :param length: длина
        :param life: количество жизней
        :param speed: скорость
        :param armor: броня
        """
        self.name = name
        self.length = length
        self.life = life
        self.speed = speed
        self.armor = armor
        self.resizable = resizable


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
