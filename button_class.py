import pygame as pg
pg.init()

class Button(pg.sprite.Sprite):
    sound = pg.mixer.Sound('sounds/button_sound.mp3')
    sound.set_volume(0.3)
    timer = 0
    def __init__(self, pos : tuple, path : str):
        super().__init__()
        self.image = pg.image.load(path)
        if path == 'images/button play.png':
            self.image = pg.transform.scale(self.image, (150, 75))
        if path == 'images/records_button.png':
            self.image = pg.transform.scale(self.image, (96, 100))
        if path == 'images/volume_on.png':
            self.image = pg.transform.scale(self.image, (48, 50))
        if path == 'images/shop_button.png':
            self.image = pg.transform.scale(self.image, (105, 75))

        self.rect = self.image.get_rect(center= pos)
        self.size = self.image.get_size()
        self.image_copy = self.image

    def draw(self, surface : pg.Surface):
        surface.blit(self.image, self.rect)



    def ispressed(self) -> bool:
        return self.rect.collidepoint(pg.mouse.get_pos()) and pg.mouse.get_pressed()[0]


    def animate(self):
        if self.rect.collidepoint(pg.mouse.get_pos()):
            self.image = pg.transform.scale(self.image, (self.size[0] * 1.2, self.size[1] * 1.2))
            rect_center = self.rect.center
            self.rect = self.image.get_rect(center= rect_center)
        else:
            self.image = self.image_copy
            rect_center = self.rect.center
            self.rect = self.image.get_rect(center=rect_center)


    def update(self, screen : pg.Surface):
        self.draw(screen)
        self.animate()

