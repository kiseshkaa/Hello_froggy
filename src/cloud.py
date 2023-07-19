import pygame as pg
from random import randrange, choice, choices
import math


class Cloud(pg.sprite.Sprite):
    def __init__(self, sc_size, *groups):
        super().__init__(*groups)
        self.angle = 0
        self.dir = 1
        self.time = 0
        self.type = choice(choices(['simple', 'storm'], [10, 1]))
        self.move_choice = choice(['circle', 'horizontal', 'vertical', 'diagonal'])

        if self.type == 'simple':
            self.image = pg.transform.scale(pg.image.load('../images/clouds/cloud.png'), (90, 70))
        elif self.type == 'storm':
            self.image = pg.transform.scale(pg.image.load('../images/clouds/rainy_cloud.png'), (90, 70))

        self.rect = self.image.get_rect(center=(randrange(100, sc_size[0] - 100, 100),
                                                randrange(0, sc_size[1] - 150, 80)))

    def move(self):
        self.time += 1
        if self.move_choice == 'horizontal':
            self.rect.centerx += self.dir
        elif self.move_choice == 'vertical':
            self.rect.centery += self.dir
        elif self.move_choice == 'diagonal':
            self.rect.centerx += self.dir
            self.rect.centery += self.dir
        elif self.move_choice == 'circle':
            self.rotate()

        if self.time == 60:
            self.dir *= -1
            self.time = 0

    def rotate(self):
        if self.angle <= 360:
            #перевод градусов в радианы
            angle = self.angle * (math.pi / 180)
            self.rect.x += math.cos(angle)
            self.rect.y += math.sin(angle)
            self.angle += 2
        else:
            self.angle = 0

    def refresh(self, sc_size):
        self.rect = self.image.get_rect(center=(randrange(100, sc_size[0] - 100, 100),
                                                randrange(0, sc_size[1] - 150, 80)))

    def update(self, screen, player):
        screen.blit(self.image, self.rect)
        self.rect.bottom += player.speed
        self.move()

        if player.is_dead:
            self.refresh(screen.get_size())

        if len(self.groups()[0]) < 7:
            Cloud(screen.get_size(), *self.groups())

        if self.rect.top >= screen.get_size()[1]:
            self.kill()




