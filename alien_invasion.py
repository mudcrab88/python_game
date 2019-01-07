import pygame
import sys
from settings import Settings

def run_game():
    #Инициализация игры,создание экрана
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    #Запуск основного цикла игры
    while True:
        #Отслеживание событий клавиатуры и мыши
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("Good Bye!")
                sys.exit()
        #Отображение последнего прорисованного экрана
        screen.fill(ai_settings.bg_color)
        pygame.display.flip()
run_game()