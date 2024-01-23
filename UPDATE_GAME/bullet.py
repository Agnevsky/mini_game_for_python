import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):

    def __init__(self, ai_settings, screen, ship):
        """ Создает объект пули"""
        super(Bullet, self).__init__()
        self.screen = screen

        # создание пули в позиции корабля
        self.image = pygame.image.load('images/heart.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        # сохранение пули в вещественном формате
        self.y = float(self.rect.y)

        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor

    def update(self):
        """ Перемещает пулю вверх по экрнау """
        # обновление позиции пули в вещественном формате
        self.y -= self.speed_factor

        # обновление позиции прямоугольника
        self.rect.y = self.y

    def draw_bullet(self):
        """ вывод пули на экран"""
        self.screen.blit(self.image, self.rect)
