import pygame
import sys
from settings import Settings
from game_stats import GameStats
from ship import Ship
import game_functions as gf
from pygame.sprite import Group
from alien import Alien
from button import Button
from scoreboard import Scoreboard


def run_game():
    #Инициализация игры,создание экрана
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    # Создание кнопки Play.
    play_button = Button(ai_settings, screen, "Play")
    # Создание экземпляра для хранения игровой статистики и Scoreboard
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)
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
        gf.check_events(ai_settings, screen, stats, play_button, ship, aliens, bullets)
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets)
            gf.update_aliens(ai_settings, stats, screen, ship, aliens,bullets)
            #Отображение последнего прорисованного экрана
        gf.update_screen(ai_settings, screen, stats, sb, ship,aliens,bullets, play_button)
run_game()
