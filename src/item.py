import pygame as pg
from button import Button
from inscription import CInscription
from support import Saver

class Item(pg.sprite.Sprite):
    number = 0
    statuses = Saver.get_data('suits')
    bought_items = []
    def __new__(cls, *args, **kwargs):
        obj = object.__new__(cls)
        cls.number += 1
        obj.number = cls.number
        obj.bought = cls.statuses[str(obj.number)][0]
        obj.dressed = cls.statuses[str(obj.number)][1]
        if obj.bought:
            cls.bought_items.append(obj)
        return obj
    def __init__(self, pos: tuple, price: int, image_path: str, *groups):
        super().__init__(*groups)
        self.button = Button(pos, image_path)
        self.price = price
        self.inscription = CInscription(f'Цена', price, 20, (self.button.rect.centerx, self.button.rect.bottom + 25))
        if self.bought and not self.dressed:
            self.inscription.text = 'доступно'
            self.inscription.change()
        elif self.dressed:
            self.inscription.text = 'надето'
            self.inscription.change()
        self.check_mark = pg.image.load('../images/chek_mark.png')
        self.check_mark_rect = self.check_mark.get_rect(center=(self.button.rect.right, self.button.rect.bottom - 20))

    def buy(self):
        if not self.bought and self.button.is_pressed():
            Saver.save_coins(Saver.get_data('coins') - self.price)
            Item.bought_items.append(self)
            self.inscription.text = 'доступно'
            self.inscription.change()
            self.bought = True
            self.refresh()

    def put_on(self):
        if not self.dressed and self.button.is_pressed():
            Item.pull_off_all()
            self.inscription.text = 'надето'
            self.inscription.change()
            self.dressed = True
            self.refresh()

    def pull_off(self):
        if self.dressed and self.button.is_pressed():
            self.dressed = False
            self.inscription.text = 'доступно'
            self.inscription.change()
            self.refresh()

    def change_status(self):
        self.buy()
        self.put_on()
        self.pull_off()

    def refresh(self):
        Saver.save_suits(self.number, self.bought, self.dressed)

    @classmethod
    def pull_off_all(cls):
        for item in cls.bought_items:
            item.dressed = False
            item.inscription.text = 'доступно'
            item.inscription.change()
            cls.refresh(item)


    def update(self, screen: pg.Surface) -> None:
        self.change_status()
        self.button.update(screen)
        if self.dressed:
            screen.blit(self.check_mark, self.check_mark_rect)
        self.inscription.update()

