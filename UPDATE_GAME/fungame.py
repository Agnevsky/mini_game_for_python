import pygame
from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard


def run_game():
    # Инициализирует pygame, settings и объект экрана.
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    bg = pygame.image.load('images/beach.png').convert_alpha()
    rect = bg.get_rect()

    # Создание кнопки Play.
    play_button = Button(ai_settings, screen, "Play")

    # Создание экземпляров GameStats и Scoreboard.
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)

    # Создание корабля.
    ship = Ship(ai_settings, screen)

    # создание группы пуль
    bullets = Group()

    # создание пришельца
    aliens = Group()

    # Создание флота пришельцев.
    gf.create_fleet_egor(ai_settings, screen, ship, aliens)
    gf.create_fleet_sasha(ai_settings, screen, ship, aliens)
    gf.create_fleet_ilya(ai_settings, screen, ship, aliens)

    # Запуск основного цикла игры.
    while True:
        screen.blit(bg, rect)
        gf.check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets)
        gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button)
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets)
            gf.update_aliens(ai_settings, screen, stats, sb, ship, aliens, bullets)
            # gf.update_screen(ai_settings, screen, stats, ship, aliens, bullets, play_button)


run_game()
