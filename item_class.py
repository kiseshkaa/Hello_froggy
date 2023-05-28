import pygame as pg
from button_class import Button
from points import Text
from add_points import get_coins, set_coins

class Item(pg.sprite.Sprite):
    items = pg.sprite.Group()
    def __new__(cls, *args, **kwargs):
        obj = super().__new__(cls)
        cls.items.add(obj)
        return obj
    def __init__(self, pos : tuple, price : int, image_path : str):
        super().__init__()
        self.button = Button(pos, image_path)
        self.text = Text( f'цена : {price}', (self.button.rect.centerx, self.button.rect.bottom + 25))
        self.price = price
        self.bought = False
        self.dressed = False
        self.check_mark = pg.image.load('images/chek_mark.png')
        self.check_mark_rect = self.check_mark.get_rect(center= (self.button.rect.right, self.button.rect.bottom - 20))


    def buy(self):
        if self.button.ispressed() and int(get_coins()) >= self.price and not self.bought:
            self.text.text = 'доступно'
            set_coins(int(get_coins()) - self.price)
            self.bought = True

    def put_on(self):
        if self.bought and self.button.ispressed() and not self.dressed and self.button.timer == 60:
            self.dressed = True
            self.text.text = 'надето'
            self.button.timer = 0
        if self.dressed and self.button.ispressed() and self.button.timer == 60:
            self.dressed = False
            self.text.text = 'доступно'
            self.button.timer = 0
        if self.button.timer < 60 and self.bought:
            self.button.timer += 1

    def update(self, screen : pg.Surface) -> None:
        self.button.update(screen)
        self.text.update()
        self.buy()
        self.put_on()
        if self.dressed:
            screen.blit(self.check_mark, self.check_mark_rect)

#comment