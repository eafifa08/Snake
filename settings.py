import pygame
import os


class Settings():
    """Класс для хранения настроек игры Snake"""
    def __init__(self):
        """Инициализирует настройки игры"""
        self.username = 'Your nick'
        self.screen_width = 500
        self.screen_height = 500
        self.difficulty = 1
        if self.difficulty == 1:
            self.fps = 4
        elif self.difficulty == 2:
            self.fps = 5
        else:
            self.fps = 6
        self.cell_size = 20
        self.max_food = 1
        self.round_max_foods = [1, 1, 1]
        self.green = (19, 71, 27)
        self.fpss = [self.fps, self.fps * 2, self.fps * 3]
        self.sound_on = False
        self.fail_sound_string = os.path.join(os.path.abspath((os.curdir)), 'media', 'fail_sound.wav')
        self.game_win_sound_string = os.path.join(os.path.abspath((os.curdir)), 'media', 'game_win_sound.wav')
        self.round_win_sound_string = os.path.join(os.path.abspath((os.curdir)), 'media', 'round_win_sound.wav')
        self.shit_sound_string = os.path.join(os.path.abspath((os.curdir)), 'media', 'shit_sound.wav')
        self.snake_head_up_string = os.path.join(os.path.abspath((os.curdir)), 'media', 'snake_head_up.png')
        self.snake_head_down_string = os.path.join(os.path.abspath((os.curdir)), 'media', 'snake_head_down.png')
        self.snake_head_left_string = os.path.join(os.path.abspath((os.curdir)), 'media', 'snake_head_left.png')
        self.snake_head_right_string = os.path.join(os.path.abspath((os.curdir)), 'media', 'snake_head_right.png')
        self.snake_body_green_string = os.path.join(os.path.abspath((os.curdir)), 'media', 'snake_body_green.png')
        
        self.apple_sound_string = os.path.join(os.path.abspath((os.curdir)), 'media', 'apple_sound.wav')
        self.apple_red_string = os.path.join(os.path.abspath((os.curdir)), 'media', 'apple_red.png')
        self.banan_string = os.path.join(os.path.abspath((os.curdir)), 'media', 'banan.png')
        self.pear_string = os.path.join(os.path.abspath((os.curdir)), 'media', 'pear.png')
        self.shit_sound_string = os.path.join(os.path.abspath((os.curdir)), 'media', 'shit_sound.wav')
        self.shit_string = os.path.join(os.path.abspath((os.curdir)), 'media', 'shit.png')
        self.life_sound_string = os.path.join(os.path.abspath((os.curdir)), 'media', 'life_sound.wav')
        self.heart_string = os.path.join(os.path.abspath((os.curdir)), 'media', 'heart.png')
        self.PATH_TO_DATABASE = os.path.join(os.path.abspath((os.curdir)), 'Snake_database.db')


    def set_difficulty(self, difficulty):
        self.difficulty = difficulty
        if self.difficulty == 1:
            self.fps = 4
        elif self.difficulty == 2:
            self.fps = 5
        else:
            self.fps = 6
        self.fpss = [self.fps, self.fps * 2, self.fps * 3]



