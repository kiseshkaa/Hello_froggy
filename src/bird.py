import pygame as pg

from random import choice


class Bird(pg.sprite.Sprite):
    def __init__(self, screen, *groups):
        super().__init__(*groups)
        self.dir = choice((1, -1))
        self.image = pg.image.load('../images/bird.png')
        if self.dir == -1:
            self.rect = self.image.get_rect(x=screen.get_size()[0], y=screen.get_size()[1] // 4)
        else:
            self.image = pg.transform.flip(self.image, True, False)
            self.rect = self.image.get_rect(y=screen.get_size()[1] // 4)

    def fly(self):
        self.rect.x += 5 * self.dir

    def hit_player(self, player):
        if self.rect.colliderect(player.rect):
            if self.dir == 1:
                player.rect.x += 5
            else:
                player.rect.x -= 5

    def __del__(self):
        print('Птица пока :(')

    def update(self, screen, player) -> None:
        self.rect.y += player.speed
        screen.blit(self.image, self.rect)
        self.fly()
        self.hit_player(player)
        if self.rect.right < 0 or self.rect.left > screen.get_size()[0] or self.rect.top > screen.get_size()[1]:
            self.kill()
