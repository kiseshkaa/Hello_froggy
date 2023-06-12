import pygame as pg

pg.init()


class Inscription(pg.sprite.Sprite):
    def __init__(self, text: str, size: int, center_pos: tuple):
        super().__init__()
        self.text = text
        self.font = pg.font.SysFont('Comic Sans MS', size, True, True)
        self.image = self.font.render(text, True, 'black')
        self.rect = self.image.get_rect(center=center_pos)

    def update(self):
        pg.display.get_surface().blit(self.image, self.rect)


class CInscription(Inscription):
    def __init__(self, text: str, value: int, size: int, center_pos: tuple):
        super().__init__(text, size, center_pos)
        self.value = value
        self.image = self.font.render(f'{self.text} {value}', True, 'black')

    def change(self, new_value: int = ''):
        self.image = self.font.render(f'{self.text} {new_value}', True, 'black')