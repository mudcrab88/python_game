import pygame
import sys
from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group
from alien import Alien


def run_game():
    #Инициализация игры,создание экрана
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    ship = Ship(ai_settings, screen)
    # Создание пришельца
    alien = Alien(ai_settings, screen)
    # Создание группы для хранения пуль.
    bullets = Group()
    aliens = Group()
    gf.create_fleet(ai_settings, screen, ship, aliens)
    #Запуск основного цикла игры
    while True:
        #Отслеживание событий клавиатуры и мыши
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        gf.update_bullets(aliens, bullets)
        gf.update_aliens(ai_settings, aliens)
        #Отображение последнего прорисованного экрана
        gf.update_screen(ai_settings, screen, ship, aliens, bullets)
run_game()
