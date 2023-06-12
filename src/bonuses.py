import pygame as pg
pg.init()


class Bonus(pg.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)
        self.image = pg.Surface((0, 0))
        self.rect = self.image.get_rect()

    def update(self, screen, spawn):
        self.rect.midbottom = spawn.rect.midtop
        screen.blit(self.image, self.rect)
        pg.draw.rect(screen, 'red', self.rect, 2)
        if not spawn.groups():
            self.kill()


class Coin(Bonus):
    sound = pg.mixer.Sound('../sounds/frog_sound.mp3')

    def __init__(self, spawn, *groups):
        super().__init__(*groups)
        self.image = pg.transform.scale(pg.image.load('../images/coin.png'), (50, 50))
        self.rect = self.image.get_rect(midbottom=spawn.rect.midtop)


class JetPack(Bonus):
    sound = pg.mixer.Sound('../sounds/frog_sound.mp3')

    def __init__(self, spawn, *groups):
        super().__init__(*groups)
        self.image = pg.transform.scale(pg.image.load('../images/jetpack.png'), (90, 90))
        self.rect = self.image.get_rect(midbottom=spawn.rect.midtop)
