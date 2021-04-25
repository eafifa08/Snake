import pygame
import random


class Snake:
    def __init__(self, game_settings, screen):
        self.game_settings = game_settings
        self.screen = screen
        self.length = 3
        self.direction = 'down'
        self.coordinates_snake = []
        self.set_coordinates_snake_center()
        self.head_coordinates = []
        self.tail_coordinates = []
        self.eaten = 0
        self.want_to_grow = 0
        self.life = 3

    def set_coordinates_snake_center(self):
        self.length = 3
        self.coordinates_snake = [[self.game_settings.screen_width // 2 // self.game_settings.cell_size,
                                   self.game_settings.screen_height // 2 // self.game_settings.cell_size, self.direction],
                                  [self.game_settings.screen_width // 2 // self.game_settings.cell_size + 1,
                                   self.game_settings.screen_height // 2 // self.game_settings.cell_size, self.direction],
                                  [self.game_settings.screen_width // 2 // self.game_settings.cell_size + 2,
                                   self.game_settings.screen_height // 2 // self.game_settings.cell_size, self.direction]]

    def blitme(self):
        if self.direction == 'up':
            myimage = pygame.image.load('media\\snake_head_up.png').convert_alpha()
        elif self.direction == 'down':
            myimage = pygame.image.load('media\\snake_head_down.png').convert_alpha()
        elif self.direction == 'left':
            myimage = pygame.image.load('media\\snake_head_left.png').convert_alpha()
        elif self.direction == 'right':
            myimage = pygame.image.load('media\\snake_head_right.png').convert_alpha()
        self.screen.blit(myimage, (self.coordinates_snake[0][0] * self.game_settings.cell_size,
                                   self.coordinates_snake[0][1] * self.game_settings.cell_size))
        for i in range(1, self.length):
            if self.coordinates_snake[i][2] == 'up':
                bodyimage = pygame.image.load('media\\snake_body_green.png').convert_alpha()
            elif self.coordinates_snake[i][2] == 'down':
                bodyimage = pygame.image.load('media\\snake_body_green.png').convert_alpha()
            elif self.coordinates_snake[i][2] == 'left':
                bodyimage = pygame.image.load('media\\snake_body_green.png').convert_alpha()
            elif self.coordinates_snake[i][2] == 'right':
                bodyimage = pygame.image.load('media\\snake_body_green.png').convert_alpha()
            self.screen.blit(bodyimage, (self.coordinates_snake[i][0] * self.game_settings.cell_size,
                                       self.coordinates_snake[i][1] * self.game_settings.cell_size))

    def grow_up(self):
        if self.want_to_grow > 0:
            self.tail_coordinates = [self.coordinates_snake[self.length - 1][0],
                                     self.coordinates_snake[self.length - 1][1],
                                     self.coordinates_snake[self.length - 1][2]]
            self.length += 1
            self.coordinates_snake.append(self.tail_coordinates[:])
            self.want_to_grow = 0

    def check_coordinates_and_borders(self):
        if self.coordinates_snake[0][0] < 0 or \
                self.coordinates_snake[0][0] > self.game_settings.screen_width // self.game_settings.cell_size - 1 or \
                self.coordinates_snake[0][1] < 0 or \
                self.coordinates_snake[0][1] > self.game_settings.screen_height // self.game_settings.cell_size - 1:
            self.life -= 1
            return False
        else:
            return True

    def move_snake(self, direction):
        if direction == 'up':
            if self.coordinates_snake[0][1] >= 1:
                if self.direction != 'down':
                    self.direction = 'up'
                    self.head_coordinates = [self.coordinates_snake[0][0],
                                             self.coordinates_snake[0][1] - 1, self.direction]
                    self.coordinates_snake = [self.head_coordinates] + self.coordinates_snake[:self.length - 1]
                else:
                    self.head_coordinates = [self.coordinates_snake[0][0],
                                             self.coordinates_snake[0][1] + 1, self.direction]
                    self.coordinates_snake = [self.head_coordinates] + self.coordinates_snake[:self.length - 1]
            else:
                self.life -= 1
                self.set_coordinates_snake_center()
        if direction == 'down' and self.coordinates_snake[0][1] <= \
                self.game_settings.screen_height//self.game_settings.cell_size-2:
            if self.direction != 'up':
                self.direction = 'down'
                self.head_coordinates = [self.coordinates_snake[0][0],
                                         self.coordinates_snake[0][1] + 1, self.direction]
                self.coordinates_snake = [self.head_coordinates] + self.coordinates_snake[:self.length - 1]
            else:
                self.head_coordinates = [self.coordinates_snake[0][0],
                                         self.coordinates_snake[0][1] - 1, self.direction]
                self.coordinates_snake = [self.head_coordinates] + self.coordinates_snake[:self.length - 1]

        if direction == 'left' and self.coordinates_snake[0][0] >= 1:
            if self.direction != 'right':
                self.direction = 'left'
                self.head_coordinates = [self.coordinates_snake[0][0] - 1,
                                         self.coordinates_snake[0][1], self.direction]
                self.coordinates_snake = [self.head_coordinates] + self.coordinates_snake[:self.length - 1]
            else:
                self.head_coordinates = [self.coordinates_snake[0][0] + 1,
                                         self.coordinates_snake[0][1], self.direction]
                self.coordinates_snake = [self.head_coordinates] + self.coordinates_snake[:self.length - 1]

        if direction == 'right' and self.coordinates_snake[0][0] <= \
            self.game_settings.screen_width//self.game_settings.cell_size-2:
            if self.direction != 'left':
                self.direction = 'right'
                self.head_coordinates = [self.coordinates_snake[0][0] + 1,
                                         self.coordinates_snake[0][1], self.direction]
                self.coordinates_snake = [self.head_coordinates] + self.coordinates_snake[:self.length - 1]
            else:
                self.head_coordinates = [self.coordinates_snake[0][0] - 1,
                                         self.coordinates_snake[0][1], self.direction]
                self.coordinates_snake = [self.head_coordinates] + self.coordinates_snake[:self.length - 1]

    def update(self, direction):
       # if not self.check_coordinates_and_borders():
        self.move_snake(direction)
        self.grow_up()
        self.blitme()


class Food(pygame.sprite.Sprite):
    def __init__(self, game_settings):
        pygame.sprite.Sprite.__init__(self)
        pygame.init()
        self.apple_sound = pygame.mixer.Sound('media\\apple_sound.wav')
        self.game_settings = game_settings
        self.image = pygame.image.load('media\\apple_red.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, game_settings.screen_width) // game_settings.cell_size * game_settings.cell_size
        self.rect.y = random.randint(0,
                                     game_settings.screen_height) // game_settings.cell_size * game_settings.cell_size
        self.coordinates = [self.rect.left // 20, self.rect.top // 20]
        print('food_coordinates=' + str(self.coordinates))
        self.eaten = False
        self.deleted = False

    def update(self, snake):
        for c in snake.coordinates_snake:
            if [c[0], c[1]] == self.coordinates:
                self.eaten = True
                self.apple_sound.play()
                snake.eaten += 1
                snake.want_to_grow += 1
                print('food eaten')
                self.kill()
