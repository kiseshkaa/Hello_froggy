import pygame as pg
from player import Player
from cloud import Cloud
from bonuses import JetPack, Coin
from random import choice
from support import get_highest_cloud, Saver
from bird import Bird
from button import Button, SoundButton
from inscription import Inscription, CInscription
from item import Item
from src.records_board import RecordsBoard

pg.init()


class Game:
    sc_size = (600, 600)
    menu_sound = pg.mixer.Sound('../sounds/menu.mp3')
    menu_sound.set_volume(0.1)
    shop_sound = pg.mixer.Sound('../sounds/shop_music.mp3')
    shop_sound.set_volume(0.1)

    def __init__(self):

        # Main settings
        self.screen = pg.display.set_mode(self.sc_size, pg.RESIZABLE)
        self.FPS = pg.time.Clock()

        # Gameplay attributes

        self.player = Player(self.sc_size)
        self.clouds = pg.sprite.Group()
        Cloud(self.sc_size, self.clouds)

        self.bonuses = pg.sprite.Group()
        self.bonus_spawn = None

        self.birds = pg.sprite.Group()

        self.result_inscription = CInscription('Результат:', 0, 40, (275, 300))
        self.points_inscription = CInscription('Очки:', 0, 25, (50, 20))

        # Menu attributes

        # Buttons
        self.buttons = pg.sprite.Group()

        self.play_button = Button((300, 300), '../images/buttons/play_button.png', self.buttons)
        self.records_button = Button((300, 400), '../images/buttons/records_button.png', self.buttons)
        self.exit_button = Button((50, 50), '../images/buttons/exit_button.png', self.buttons)
        self.shop_button = Button((510, 340), '../images/buttons/shop_button.png', self.buttons)
        self.sound_button = SoundButton((550, 50), self.buttons)

        # Border
        self.border = pg.Rect(175, 100, 250, 400)

        # Inscriptions
        self.title = Inscription('Hello, Froggy', 28, (300, 200))
        self.coins_inscription = CInscription('Монеты:', Saver.get_data('coins'), 20, (480, 400))
        self.records_insription = RecordsBoard()
        self.shop_coins_inscription = CInscription('Монеты:', Saver.get_data('coins'), 28, (275, 60))

        # Shop
        self.items = pg.sprite.Group()
        price = 100

        for i in range(150, 451, 150):
            for j in range(200, 401, 200):
                Item((j, i), price, '../images/coin.png', self.items)
                price += 100

    def play(self):
        self.player.refresh(self.sc_size)
        while True:
            self.screen.fill((94, 178, 230))
            self.result_inscription.change(self.player.max_height)
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    exit()

            self.player.update(self.screen, self.clouds, self.bonuses)
            self.clouds.update(self.screen, self.player)
            self.birds.update(self.screen, self.player)

            # Bonus spawn
            if int(self.player.height) % 20 == 0 and not self.bonuses.sprites():
                self.bonus_spawn = get_highest_cloud(self.screen, self.clouds)
                choice((Coin, JetPack))(self.bonus_spawn, self.bonuses)
            else:
                self.bonuses.update(self.screen, self.bonus_spawn)

            # Bird spawn
            if int(self.player.height) % 30 == 0 and not self.birds.sprites():
                Bird(self.screen, self.birds)

            if self.player.is_dead:
                Saver.save_point(self.player.max_height)
                self.records_insription.refresh()
                break

            self.points_inscription.change(self.player.max_height)
            self.points_inscription.update()

            pg.display.update()
            self.FPS.tick(60)

    def run_menu(self):
        self.menu_sound.play(-1)
        self.coins_inscription.change(Saver.get_data('coins'))
        while True:
            self.screen.fill("seashell1")
            self.title.update()
            self.coins_inscription.update()
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    exit()

            self.buttons.update(self.screen)
            self.records_insription.update(self.screen)

            if self.play_button.is_pressed():
                break
            elif self.records_button.is_pressed():
                self.records_insription.vision = not self.records_insription.vision
            elif self.exit_button.is_pressed():
                exit()
            elif self.shop_button.is_pressed():
                self.menu_sound.stop()
                self.run_shop()
                self.menu_sound.play(-1)
            elif self.sound_button.is_pressed():
                if self.sound_button.volume_switch:
                    self.menu_sound.set_volume(0.1)
                else:
                    self.menu_sound.set_volume(0)


            pg.draw.rect(self.screen, 'seashell3', self.border, 5, 10)

            pg.display.update()
            self.FPS.tick(60)
        self.menu_sound.stop()


    def run_shop(self):
        self.shop_sound.play(-1)
        while True:
            self.screen.fill("seashell1")
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    exit()

            self.items.update(self.screen)
            self.exit_button.update(self.screen)
            self.shop_coins_inscription.update()
            self.shop_coins_inscription.change(Saver.get_data('coins'))

            if self.exit_button.is_pressed() or pg.key.get_pressed()[pg.K_ESCAPE]:
                self.player.change_suit()
                self.shop_sound.stop()
                break

            pg.display.update()
            self.FPS.tick(60)
        self.coins_inscription.change(Saver.get_data('coins'))

    def show_results(self):
        while True:
            self.screen.fill((94, 178, 230))
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    exit()

            self.result_inscription.update()

            if pg.key.get_pressed()[pg.K_ESCAPE]:
                break

            pg.display.update()
            self.FPS.tick(60)

    def run(self):
        while True:
            self.run_menu()
            self.play()
            self.show_results()


game = Game()
game.run()
