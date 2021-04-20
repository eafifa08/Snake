import pygame


class Settings():
    """Класс для хранения настроек игры Snake"""
    def __init__(self):
        """Инициализирует настройки игры"""
        self.screen_width = 400
        self.screen_height = 400
        self.fps = 4
        self.cell_size = 20
        self.max_food = 1
        self.round_max_food = 10
        self.green = (19, 71, 27)
        self.fpss = [self.fps, self.fps * 2, self.fps * 3]



