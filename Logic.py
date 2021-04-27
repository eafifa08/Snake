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
                                   self.game_settings.screen_height // 2 // self.game_settings.cell_size, 'down'],
                                  [self.game_settings.screen_width // 2 // self.game_settings.cell_size + 1,
                                   self.game_settings.screen_height // 2 // self.game_settings.cell_size, 'down'],
                                  [self.game_settings.screen_width // 2 // self.game_settings.cell_size + 2,
                                   self.game_settings.screen_height // 2 // self.game_settings.cell_size, 'down']]
        self.direction = 'down'

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
            if self.coordinates_snake[0][1] >= 0:
                if self.direction != 'down':
                    self.direction = 'up'
                    self.head_coordinates = [self.coordinates_snake[0][0],
                                             self.coordinates_snake[0][1] - 1, self.direction]
                    self.coordinates_snake = [self.head_coordinates] + self.coordinates_snake[:self.length - 1]
                else:
                    self.head_coordinates = [self.coordinates_snake[0][0],
                                             self.coordinates_snake[0][1] + 1, self.direction]
                    self.coordinates_snake = [self.head_coordinates] + self.coordinates_snake[:self.length - 1]
        if direction == 'down' and self.coordinates_snake[0][1] <= \
                self.game_settings.screen_height//self.game_settings.cell_size-1:
            if self.direction != 'up':
                self.direction = 'down'
                self.head_coordinates = [self.coordinates_snake[0][0],
                                         self.coordinates_snake[0][1] + 1, self.direction]
                self.coordinates_snake = [self.head_coordinates] + self.coordinates_snake[:self.length - 1]
            else:
                self.head_coordinates = [self.coordinates_snake[0][0],
                                         self.coordinates_snake[0][1] - 1, self.direction]
                self.coordinates_snake = [self.head_coordinates] + self.coordinates_snake[:self.length - 1]

        if direction == 'left' and self.coordinates_snake[0][0] >= 0:
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
            self.game_settings.screen_width//self.game_settings.cell_size-1:
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
        if self.check_coordinates_and_borders():
            self.move_snake(direction)
        else:
            self.set_coordinates_snake_center()
        self.grow_up()
        self.blitme()


class Food(pygame.sprite.Sprite):
    def __init__(self, game_settings):
        pygame.sprite.Sprite.__init__(self)
        pygame.init()
        self.types = ['food', 'bad', 'life']
        self.type = random.choices(self.types, weights=[15, 5, 1], k=1)[0]
        self.apple_sound = pygame.mixer.Sound('media\\apple_sound.wav')
        self.game_settings = game_settings
        if self.type == 'food':
            self.image = pygame.image.load('media\\apple_red.png').convert_alpha()
        elif self.type == 'bad':
            self.image = pygame.image.load('media\\shit.png').convert_alpha()
        elif self.type == 'life':
            self.image = pygame.image.load('media\\heart.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, (game_settings.screen_width) // game_settings.cell_size - 1) * game_settings.cell_size
        self.rect.y = random.randint(0,
                                     (game_settings.screen_height) // game_settings.cell_size - 1) * game_settings.cell_size
        self.coordinates = [self.rect.left // game_settings.cell_size, self.rect.top // game_settings.cell_size]
        print(str(self.type) + 'coordinates=' + str(self.coordinates))
        self.eaten = False
        self.deleted = False

    def update(self, snake):
        for c in snake.coordinates_snake:
            if [c[0], c[1]] == self.coordinates:
                if self.type == 'food':
                    self.eaten = True
                    self.apple_sound.play()
                    snake.eaten += 1
                    snake.want_to_grow += 1
                    print('food eaten')
                    self.kill()
                elif self.type == 'bad':
                    #self.eaten = True
                    #self.apple_sound.play()
                    #snake.eaten += 1
                    snake.want_to_grow += 0
                    snake.life -= 1
                    print('shit eaten')
                    self.kill()
                elif self.type == 'life':
                    #self.eaten = True
                    #self.apple_sound.play()
                    #snake.eaten += 1
                    snake.want_to_grow += 0
                    snake.life += 1
                    print('life eaten')
                    self.kill()
