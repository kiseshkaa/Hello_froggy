import pygame as pg
from bonuses import JetPack, Coin
from support import Saver

pg.init()


class Player(pg.sprite.Sprite):
    jumping_sound = pg.mixer.Sound('../sounds/frog_sound.mp3')
    jumping_sound.set_volume(0.2)
    falling_sound = pg.mixer.Sound('../sounds/falling_sound.mp3')
    falling_sound.set_volume(0.2)

    def __init__(self, sc_size):
        super().__init__()
        self.animate_images = (pg.image.load('../images/frog/frog_0.png'),
                               pg.image.load('../images/frog/frog_1.png'),
                               pg.image.load('../images/frog/frog_2.png'),
                               pg.transform.rotate(pg.image.load('../images/frog/frog_2.png'), 180)
                               )
        self.image = self.animate_images[1]
        self.rect = self.image.get_rect(centerx=sc_size[0] // 2, centery=sc_size[1] // 2)

        self.time = 0
        self.speed = 0
        self.start_speed = 10
        self.boost = 10

        self.height = 0
        self.max_height = 0
        self.is_fallen = False
        self.is_dead = False

    # +
    def move(self):
        keys = pg.key.get_pressed()
        if keys[pg.K_LEFT]:
            self.rect.x -= 2
        if keys[pg.K_RIGHT]:
            self.rect.x += 2

    def change_speed(self):
        self.time += 1 / 60
        self.speed = self.start_speed - self.boost * self.time

    # +-
    def jump(self, clouds):
        for sprite in clouds:
            if self.speed <= 0 and self.rect.colliderect(sprite.rect) and \
                    sprite.rect.top < self.rect.bottom < sprite.rect.centery:
                if sprite.type == 'storm':
                    self.start_speed = 5
                else:
                    self.start_speed = 10
                self.jumping_sound.play()
                self.time = 0

        if self.speed > 0:
            self.height += 0.1
        elif self.speed < 0:
            self.height -= 0.1

        self.set_max_height()

    def set_max_height(self):
        self.max_height = int(max(self.height, self.max_height))

    def take_bonus(self, bonuses):
        if self.rect.collidelistall(bonuses.sprites()):
            if isinstance(bonuses.sprites()[0], JetPack):
                self.start_speed = 20
                self.time = 0
            elif isinstance(bonuses.sprites()[0], Coin):
                Saver.save_coins(Saver.get_data('coins') + 1)
            bonuses.sprites()[0].kill()

    # +
    def animate(self):
        if self.speed <= 0:
            self.image = self.animate_images[0]
        elif self.speed >= 5:
            self.image = self.animate_images[1]
        else:
            self.image = self.animate_images[2]
        if self.speed <= -10:
            self.image = self.animate_images[3]
            self.rect.y -= self.speed // 2
            if not self.is_fallen:
                self.falling_sound.play()
                self.is_fallen = True

    def refresh(self, sc_size):
        self.is_dead = False
        self.is_fallen = False
        self.rect = self.image.get_rect(centerx=sc_size[0] // 2, centery=sc_size[1] // 2)
        self.height = 0
        self.max_height = 0
        self.time = 0
        self.speed = 0
        self.start_speed = 10
        self.boost = 10

    def update(self, screen, clouds, bonuses):
        self.move()
        self.change_speed()
        self.jump(clouds)
        self.animate()
        self.take_bonus(bonuses)
        pg.draw.rect(screen, 'red', self.rect, 2)
        screen.blit(self.image, self.rect)
        if self.rect.top > screen.get_size()[1]:
            self.is_dead = True

