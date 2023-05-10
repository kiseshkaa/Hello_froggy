import pygame as pg
from button_class import Button
from points import Text

class Item(pg.sprite.Sprite):
    def __init__(self, pos : tuple, price : int, image_path : str):
        super().__init__()
        self.button = Button(pos, image_path)
        self.text = Text( f'цена : {price}', (self.button.rect.centerx, self.button.rect.bottom + 25))

    def update(self, screen : pg.Surface) -> None:
        self.button.update(screen)
        self.text.update()
