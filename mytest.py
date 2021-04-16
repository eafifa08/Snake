import pygame_menu
import pygame
pygame.init()
surface = pygame.display.set_mode((600, 400))

def set_difficulty(value, difficulty):
    # Do the job here !
    pass

def start_the_game():
    # Do the job here !
    print('play')
    pass

menu = pygame_menu.Menu(300, 400, 'Welcome',
                       theme=pygame_menu.themes.THEME_GREEN)

menu.add.text_input('Name :', default='Sergey')
menu.add.selector('Difficulty :', [('Hard', 1), ('Easy', 2)], onchange=set_difficulty)
menu.add.button('Play', start_the_game)
menu.add.button('Quit', pygame_menu.events.EXIT)

menu.mainloop(surface)