import pygame as pg

pg.init()


class Button(pg.sprite.Sprite):
    sound = pg.mixer.Sound('../sounds/button_sound.mp3')
    sound.set_volume(0.3)

    def __init__(self, pos: tuple, path: str = '', *groups):
        super().__init__(*groups)
        self.image = pg.image.load(path)
        self.switch = None

        if path == '../images/buttons/play_button.png':
            self.image = pg.transform.scale(self.image, (150, 75))
        if path == '../images/buttons/records_button.png':
            self.image = pg.transform.scale(self.image, (96, 100))
        if path == '../images/buttons/shop_button.png':
            self.image = pg.transform.scale(self.image, (105, 75))
            self.switch = 1

        self.image_copy = self.image.copy()
        self.scaled_image = pg.transform.scale(self.image, (self.image.get_size()[0] * 1.2,
                                                            self.image.get_size()[1] * 1.2)
                                               )

        self.rect = self.image.get_rect(center=pos)
        self.rect_copy = self.rect.copy()
        self.scaled_rect = self.scaled_image.get_rect(center=pos)

        self.press_timer = 0

    def is_pressed(self) -> bool:
        if self.press_timer == 0 and self.rect.collidepoint(pg.mouse.get_pos()) and pg.mouse.get_pressed()[0]:
            self.press_timer = 15
            return True
        return False

    def animate(self):
        if self.rect.collidepoint(pg.mouse.get_pos()):
            self.image = self.scaled_image
            self.rect = self.scaled_rect
        else:
            self.image = self.image_copy
            self.rect = self.rect_copy

    def update(self, screen: pg.Surface):
        if self.press_timer != 0:
            self.press_timer -= 1
        screen.blit(self.image, self.rect)
        self.animate()


class SoundButton(pg.sprite.Sprite):
    def __init__(self, pos: tuple, *groups):
        super().__init__(*groups)
        # Images
        self.image_off = pg.transform.scale(pg.image.load('../images/buttons/volume_off.png'), (48, 50))
        self.image_on = pg.transform.scale(pg.image.load('../images/buttons/volume_on.png'), (48, 50))

        self.scaled_image_off = pg.transform.scale(self.image_off, (self.image_off.get_size()[0] * 1.2,
                                                                    self.image_off.get_size()[1] * 1.2)
                                                   )
        self.scaled_image_on = pg.transform.scale(self.image_on, (self.image_on.get_size()[0] * 1.2,
                                                                  self.image_on.get_size()[1] * 1.2)
                                                  )

        self.image = self.image_on
        self.image_copy = self.image.copy()
        self.scaled_image = self.scaled_image_on

        # Rects
        self.rect = self.image.get_rect(center=pos)
        self.rect_copy = self.rect.copy()
        self.scaled_rect = self.scaled_image.get_rect(center=pos)

        # Switches
        self.volume_switch = True
        self.press_timer = 0

    def is_pressed(self) -> bool:
        if self.press_timer == 0 and self.rect.collidepoint(pg.mouse.get_pos()) and pg.mouse.get_pressed()[0]:
            self.press_timer = 15
            self.volume_switch = not self.volume_switch
            self.change_image()
            return True
        return False

    def change_image(self):
        if self.volume_switch:
            self.image_copy = self.image_on
            self.scaled_image = self.scaled_image_on
        else:
            self.image_copy = self.image_off
            self.scaled_image = self.scaled_image_off
        self.image = self.image_copy

    def animate(self):
        if self.rect.collidepoint(pg.mouse.get_pos()):
            self.image = self.scaled_image
            self.rect = self.scaled_rect
        else:
            self.image = self.image_copy
            self.rect = self.rect_copy

    def update(self, screen: pg.Surface):
        if self.press_timer != 0:
            self.press_timer -= 1
        screen.blit(self.image, self.rect)
        self.animate()
