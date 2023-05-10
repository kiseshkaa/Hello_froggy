import pygame as pg
from random import choice


class Bonus(pg.sprite.Sprite):
    def __init__(self, type):
        super().__init__()
        self.type = type
        if self.type == 'jetpack':
            self.image = pg.transform.scale(pg.image.load('images/jetpack.png'), (90, 90))
            self.rect = self.image.get_rect(bottomright= (0, 0))
        if self.type == 'coin':
            self.image = pg.image.load('images/coin.png')
            self.rect = self.image.get_rect(bottomright= (0, 0))

    def update(self, cloud):
        pg.display.get_surface().blit(self.image, self.rect)
        self.rect.bottom = cloud.rect.top
        self.rect.centerx = cloud.rect.centerx
        if self.rect.bottom > 500:
            self.kill()


