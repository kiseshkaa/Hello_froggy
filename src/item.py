import pygame as pg
from button import Button
from inscription import CInscription


class Item(pg.sprite.Sprite):
    bought_items = pg.sprite.Group()
    def __init__(self, pos: tuple, price: int, image_path: str, *groups):
        super().__init__(*groups)
        self.button = Button(pos, image_path)
        self.price = price
        self.inscription = CInscription(f'Цена', price, 20, (self.button.rect.centerx, self.button.rect.bottom + 25))
        self.bought = False
        self.dressed = False
        self.check_mark = pg.image.load('../images/frog/frog_0.png')
        self.check_mark_rect = self.check_mark.get_rect(center=(self.button.rect.right, self.button.rect.bottom - 20))

    def buy(self):
        if not self.bought and self.button.is_pressed():
            Item.bought_items.add(self)
            self.inscription.text = 'доступно'
            self.inscription.change()
            self.bought = True

    def put_on(self):
        if not self.dressed and self.button.is_pressed():
            Item.pull_off_all()
            self.inscription.text = 'надето'
            self.inscription.change()
            self.dressed = True

    def pull_off(self):
        if self.dressed and self.button.is_pressed():
            self.dressed = False
            self.inscription.text = 'доступно'
            self.inscription.change()
            print(1)

    def change_status(self):
        self.buy()
        self.put_on()
        self.pull_off()

    @classmethod
    def pull_off_all(cls):
        for item in cls.bought_items:
            item.dressed = False
            item.inscription.text = 'доступно'
            item.inscription.change()


    def update(self, screen: pg.Surface) -> None:
        self.change_status()
        if self.dressed:
            screen.blit(self.check_mark, self.check_mark_rect)
        self.button.update(screen)
        self.inscription.update()

