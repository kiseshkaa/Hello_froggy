import pygame as pg
from settings import sc_size


class Frog:
    def __init__(self):
        self.surf = pg.image.load('images/frog_0.png')
        self.rect = self.surf.get_rect(centerx= sc_size [0] // 2, centery= sc_size[1] // 2)
        self.dir = 1
        self.speed = 0
        self.start_speed = 10
        self.time = 0
        self.boost = 10
        self.max_height = 0
        self.height = 0
        self.fall_image = pg.image.load('images/frog_3.png')
        self.fall_image_copy = self.fall_image
        self.jumping_sound = pg.mixer.Sound('sounds/frog_sound.mp3')
        self.jumping_sound.set_volume(0.2)
        self.falling_sound = pg.mixer.Sound('sounds/falling_sound.mp3')
        self.falling_sound.set_volume(0.2)
        self.isfallen = False

    def move(self):
        keys = pg.key.get_pressed()
        if keys[pg.K_LEFT]:
            self.rect.x -= 2
        if keys[pg.K_RIGHT]:
            self.rect.x += 2


    def jump(self, clouds, bird, bonuses):
        self.time += 1 / 60
        self.speed = self.start_speed - self.boost * self.time
        if self.iscollide(clouds, bird, bonuses):
            self.speed = self.start_speed
            self.time = 0
        if self.speed <= -10:
            self.rect.bottom -= self.speed // 4

    def find_max_hight(self):
        self.height += self.speed
        self.max_height = int(max(self.height, self.max_height))


    def iscollide(self, clouds: pg.sprite.Group, bird: pg.sprite.Sprite, bonuses: tuple):
        if bird.rect.colliderect(self.rect):
            if bird.dir == 1 and bird.rect.right > self.rect.left:
                self.rect.x += 5
            elif bird.dir == -1 and bird.rect.left < self.rect.right:
                self.rect.x -= 5
        for sprite in clouds:
            if self.speed <= 0 and self.rect.colliderect(sprite.rect) and\
                    sprite.rect.top < self.rect.bottom < sprite.rect.centery:
                if sprite.type == 'storm':
                    self.start_speed = 5
                else:
                    self.start_speed = 10
                self.jumping_sound.play()
                return True
        for bonus in bonuses[0]:
            if self.rect.colliderect(bonus.rect):
                self.start_speed = 20
                bonus.kill()
        for bonus in bonuses[1]:
            if self.rect.colliderect(bonus.rect):
                bonus.kill()
                file = open('coins.txt')
                coins_counter = int(file.readline()) + 1
                file.close()
                file = open('coins.txt', 'w')
                file.write(str(coins_counter))
                file.close()



    def animate(self):
        if self.speed <= 0:
            self.surf = pg.image.load('images/frog_1.png')
        elif self.speed >= 5:
            self.surf = pg.image.load('images/frog_0.png')
        else:
            self.surf = pg.image.load('images/frog_2.png')
        if self.speed <= -10:
            self.fall_image = pg.transform.rotate(self.fall_image_copy, 180)
            self.rect = self.fall_image.get_rect(center= self.rect.center)
            self.surf = self.fall_image
            if not self.isfallen:
                self.falling_sound.play()
            self.isfallen = True

