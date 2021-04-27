import pygame


class Settings():
    """Класс для хранения настроек игры Snake"""
    def __init__(self):
        """Инициализирует настройки игры"""
        self.screen_width = 600
        self.screen_height = 600
        self.difficulty = 1
        if self.difficulty == 1:
            self.fps = 4
        elif self.difficulty == 2:
            self.fps = 5
        else:
            self.fps = 6
        self.cell_size = 20
        self.max_food = 1
        self.round_max_foods = [10, 15, 20]
        self.green = (19, 71, 27)
        self.fpss = [self.fps, self.fps * 2, self.fps * 3]
        self.sound_on = False

    def set_difficulty(self, difficulty):
        self.difficulty = difficulty
        if self.difficulty == 1:
            self.fps = 4
        elif self.difficulty == 2:
            self.fps = 5
        else:
            self.fps = 6
        self.fpss = [self.fps, self.fps * 2, self.fps * 3]



