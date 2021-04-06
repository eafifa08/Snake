class Snake:
    def __init__(self, name, length, life, speed, armor):
        self.name = name
        self.length = length
        self.life = life
        self.speed = speed
        self.armor = armor



class Field:
    def __init__(self, size, dangerous_walls, something_good_max):
        self.width, self.height = size
        self.dangerous_walls = dangerous_walls
        self.something_good_max = something_good_max
        self.something_good_min = 0
        self.something_good



class Something:
    pass


class GameRound:
    pass
