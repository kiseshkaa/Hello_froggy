import pygame as pg

import frog_class


class Points:
    def __init__(self):
        self.font = pg.font.SysFont('Comic Sans MS', 30, True, True)
        self.surf = self.font.render('очки: ', True, 'black')

    def count(self, frog : frog_class.Frog):
        self.surf = self.font.render('очки:' + str(frog.max_height // 60), True, 'black')

class Coins:
    def __init__(self):
        self.font = pg.font.SysFont('Comic Sans MS', 30, True, True)
        self.surf = self.font.render('монеты: ', True, 'black')

    def count(self, counter : int):
        self.surf = self.font.render('монеты:' + str(counter), True, 'black')




class Text(pg.sprite.Sprite):
    def __init__(self, text : str, center_pos : tuple):
        super().__init__()
        self.font = pg.font.SysFont('Comic Sans MS', 28, True, True)
        self.image = self.font.render(str(text), True, 'black')
        self.rect = self.image.get_rect(center= center_pos)
        self.text = text

    def update(self, text = ''):
        if text:
            self.image = self.font.render(str(text), True, 'black')
        pg.display.get_surface().blit(self.image, self.rect)



