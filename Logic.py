import pygame
import random


class Snake:
    def __init__(self, game_settings, screen, coordinates):
        self.coordinates = coordinates
        self.game_settings = game_settings
        self.screen = screen
        self.length = 3
        self.image = pygame.Surface((game_settings.cell_size, game_settings.cell_size*3), pygame.SRCALPHA, 32)
        #self.image = pygame.image.load('media\snake_head.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.left = game_settings.screen_width // 2
        self.rect.bottom = game_settings.screen_height // 2
        self.coordinates[game_settings.screen_width//2//game_settings.cell_size][
            game_settings.screen_height//2//game_settings.cell_size] = 1
        self.coordinates[game_settings.screen_width // 2 // game_settings.cell_size+1][
            game_settings.screen_height // 2 // game_settings.cell_size] = 1
        self.coordinates[game_settings.screen_width // 2 // game_settings.cell_size + 2][
            game_settings.screen_height // 2 // game_settings.cell_size] = 1
        self.coordinates_snake = [[game_settings.screen_width//2//game_settings.cell_size,game_settings.screen_height//2//game_settings.cell_size],
                                  [game_settings.screen_width // 2 // game_settings.cell_size+1,game_settings.screen_height // 2 // game_settings.cell_size],
                                  [game_settings.screen_width // 2 // game_settings.cell_size + 2,game_settings.screen_height // 2 // game_settings.cell_size]]
        self.head_coordinates = []
        self.tail_coordinates = []
        print(self.coordinates_snake)
        for i in range(game_settings.screen_width//game_settings.cell_size):
            print(self.coordinates[i])
        self.polygon_coordinates = [[0, 0], [0, game_settings.cell_size*3], [game_settings.cell_size,
                                    game_settings.cell_size*3], [game_settings.cell_size, 0]]
        pygame.draw.polygon(self.image, pygame.color.THECOLORS['red'], self.polygon_coordinates)
        self.mask = pygame.mask.from_surface(self.image)
        #self.image.fill(pygame.color.THECOLORS['green'])
        self.direction = 'down'
        self.speed_x = 0
        self.speed_y = 0
        self.eaten = 0

    def blitme(self):
       # self.screen.blit(self.image, self.rect)
       for i in range (self.length):
            pygame.draw.rect(self.screen, self.game_settings.green,
                             pygame.Rect(self.coordinates_snake[i][0]*self.game_settings.cell_size,
                           self.coordinates_snake[i][1]*self.game_settings.cell_size,
                            self.game_settings.cell_size, self.game_settings.cell_size))

    def grow_up(self):
        if self.eaten > 0:
            self.tail_coordinates = [self.coordinates_snake[self.length - 1][0],
                                     self.coordinates_snake[self.length - 1][1]]
            self.length += 1
            self.coordinates_snake.append(self.tail_coordinates[:])
            self.eaten = 0

    def update(self, direction):
        if direction == 'up':
            if self.direction != 'down':
                self.speed_y = -20
                self.speed_x = 0
                self.direction = 'up'

                self.head_coordinates = [self.coordinates_snake[0][0],
                                         self.coordinates_snake[0][1]-1]
                self.coordinates_snake = [self.head_coordinates] + self.coordinates_snake[:self.length-1]
        if direction == 'down':
            if self.direction != 'up':
                self.speed_y = 20
                self.speed_x = 0
                self.direction = 'down'
                self.head_coordinates = [self.coordinates_snake[0][0],
                                         self.coordinates_snake[0][1]+1]
                self.coordinates_snake = [self.head_coordinates] + self.coordinates_snake[:self.length-1]
        if direction == 'left':
            if self.direction != 'right':
                self.speed_y = 0
                self.speed_x = -20
                self.direction = 'left'
                self.head_coordinates = [self.coordinates_snake[0][0]-1,
                                         self.coordinates_snake[0][1]]
                self.coordinates_snake = [self.head_coordinates] + self.coordinates_snake[:self.length-1]
        if direction == 'right':
            if self.direction != 'left':
                self.speed_y = 0
                self.speed_x = 20
                self.direction = 'right'
                self.head_coordinates = [self.coordinates_snake[0][0]+1,
                                         self.coordinates_snake[0][1]]

                self.coordinates_snake = [self.head_coordinates] + self.coordinates_snake[:self.length-1]
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
        if self.rect.right > self.game_settings.screen_width:
            self.rect.right = self.game_settings.screen_width
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > self.game_settings.screen_height:
            self.rect.bottom = self.game_settings.screen_height

        print('head_coordinates=' + str(self.head_coordinates))
        self.grow_up()
        self.blitme()


class Food(pygame.sprite.Sprite):
    def __init__(self, game_settings):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('media\\apple_red.png').convert_alpha()
        #self.image = pygame.Surface((10, 10))
        #self.image.fill(pygame.color.THECOLORS['blue'])
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, game_settings.screen_width) // game_settings.cell_size * game_settings.cell_size
        self.rect.y = random.randint(0, game_settings.screen_height) // game_settings.cell_size * game_settings.cell_size
        self.coordinates = [self.rect.left//20, self.rect.top//20]
        print('food_coordinates='+ str(self.coordinates))
        self.eaten = False
        self.deleted = False

    def update(self, snake):
        #if(self.rect.left >= snake.rect.left and self.rect.top >= snake.rect.top
         #       and self.rect.right <= snake.rect.right and self.rect.bottom <= snake.rect.bottom):
        for coords in snake.coordinates_snake:
            if coords == self.coordinates:
                self.eaten = True
                snake.eaten += 1
                print('food eaten')
                self.kill()
