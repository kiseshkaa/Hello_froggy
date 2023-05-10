import pygame as pg
from settings import sc_size
from random import choice

class Birds(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.dir = choice((1, -1))
        self.image = pg.image.load('images/bird_1.png')
        if self.dir == -1:
            self.rect = self.image.get_rect(x= sc_size[0], y= sc_size[1] // 4)
        else:
            self.image = pg.transform.flip(self.image, True, False)
            self.rect = self.image.get_rect(y= sc_size[1] // 4)

    def fly(self):
        self.rect.x += 5 * self.dir

    def update(self, frog) -> None:
        self.rect.y += frog.speed
        pg.display.get_surface().blit(self.image, self.rect)
        self.fly()




