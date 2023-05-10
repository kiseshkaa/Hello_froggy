import pygame as pg
from random import randrange, choice, choices
import math

from settings import sc_size


class Cloud(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.angle = 0
        self.dir = 1
        self.time = 0
        self.type = choice(choices(['simple', 'storm'], [10, 1]))
        self.move_choice = choice(['circle', 'horizontal', 'vertical', 'diagonal'])
        if self.type == 'simple':
            self.image = pg.transform.scale(pg.image.load('images/cloud.png'), (90, 70))
        elif self.type == 'storm':
            self.image = pg.transform.scale(pg.image.load('images/rainy_cloud.png'), (90, 70))
        self.rect = self.image.get_rect(center=(randrange(100, sc_size[0] - 100, 100),
                                                randrange(0, sc_size[1] - 150, 80)))
        self.status = False
    def change_status(self):
        if self.rect.centery >= sc_size[1]:
            self.status = True

    def move(self):
        self.time += 1
        if self.move_choice == 'horizontal':
            self.rect.centerx += self.dir
            if self.time == 60:
                self.dir *= -1
                self.time = 0
        if self.move_choice == 'vertical':
            self.rect.centery += self.dir
            if self.time == 60:
                self.dir *= -1
                self.time = 0
        if self.move_choice == 'diagonal':
            self.rect.centerx += self.dir
            self.rect.centery += self.dir
            if self.time == 60:
                self.dir *= -1
                self.time = 0
        if self.move_choice == 'circle':
            self.rotate()


    def rotate(self):
        if self.angle <= 360:
            angle = self.angle * (math.pi / 180)
            self.rect.x += math.cos(angle)
            self.rect.y += math.sin(angle)
            self.angle += 2
        else:
            self.angle = 0


    def update(self, frog):
        self.rect.bottom += frog.speed
        self.change_status()
        self.move()



