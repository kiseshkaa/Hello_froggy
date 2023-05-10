import pygame as pg

class Player(pg.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = pg.Surface((50, 120))
        self.image.fill('orange')
        self.rect = self.image.get_rect(center=pos)

    def update(self):
        keys = pg.key.get_pressed()
        if keys[pg.K_UP]:
            self.rect.top -= 4
        if keys[pg.K_DOWN]:
            self.rect.top += 4
