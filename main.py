import pygame as pg
from sys import exit
import time
import random
import add_points

from random import choice
from bonuses import Bonus
from birds_class import Birds
from frog_class import Frog
from clouds_class import Cloud
from points import Points, Text, Coins
from button_class import Button
from time import sleep
from add_points import add_record, clear_records, get_coins
from settings import sc_size
from item_class import Item


pg.init()
screen = pg.display.set_mode((600, 600))
FPS = pg.time.Clock()
plate = pg.Surface((screen.get_size()[0], 10))
plate_rect = plate.get_rect(centery=500)
finish_points = Points()
frog = Frog()

item1 = Item((200, 150), 1, 'images/coin.png')
item2 = Item((400, 150), 200, 'images/coin.png')
item3 = Item((200, 300), 300, 'images/coin.png')
item4 = Item((400, 300), 400, 'images/coin.png')
item5 = Item((200, 450), 500, 'images/coin.png')
item6 = Item((400, 450), 600, 'images/coin.png')

main_points = Points()
coins = Coins()
coins_text = Text('монеты:' + get_coins(), (80, 70))

points_rect = finish_points.surf.get_rect(center= (300, 300))
shop_button = Button((510, 340), 'images/shop_button.png')
button = Button((300, 300), 'images/button play.png')
button_exit = Button((50, 50), 'images/button exit.png')
records_button = Button((300, 400), 'images/records_button.png')
frog_button = Button((500, 500), 'images/frog_0.png')

volume_button = Button((550, 50), 'images/volume_on.png')
border_rect = pg.Rect(0, 0, 250, 400)
border_rect.center = (300, 300)
record_rect = pg.Rect(15, 100, 145, 400)
menu_music = pg.mixer.Sound('sounds/main_theme.mp3')
menu_music.set_volume(0.1)
start_sound = pg.mixer.Sound('sounds/321_to_start.mp3')
start_sound.set_volume(0.2)

main_font = pg.font.SysFont('Lucida Calligraphy', 30, True, False)
menu_title = main_font.render('Hello, Frogy', True, 'black')
mt_rect = menu_title.get_rect(center= (300, 200))

records = pg.sprite.Group()

def update_records():
    global records
    for index, record in enumerate(add_points.change_record()):
        if record != 0:
            a = Text(record, (55, index * 35 + 130))
            records.add(a)

update_records()

item_group = pg.sprite.Group(item1, item2, item3, item4, item5, item6)

clouds = pg.sprite.Group(Cloud(), Cloud(), Cloud(), Cloud(), Cloud(),
                         Cloud())
buttons = pg.sprite.Group(button, button_exit, records_button, frog_button, volume_button, shop_button)

jetpack_group = pg.sprite.Group()
coins_group = pg.sprite.Group()

bird = Birds()

def run_menu(run : bool) -> None:
    menu_coins = Text('монеты:' + get_coins(), (510, 400))
    records_status = False
    menu_music.play(-1)
    while run:
        screen.fill("seashell1")
        for i in pg.event.get():
            if i.type == pg.KEYDOWN and i.key == pg.K_ESCAPE or button_exit.ispressed():
                exit()

        pg.draw.rect(screen, "seashell3", border_rect, 3, 10)
        buttons.update(screen)
        screen.blit(menu_title, mt_rect)

        if records_status:
            records.draw(screen)
            pg.draw.rect(screen, "seashell3", record_rect, 3, 10)

        if Button.timer == 0 and records_button.ispressed():
            records_status = not records_status

        if Button.timer == 0 and frog_button.ispressed():
            clear_records()
            records.empty()

        if Button.timer == 0 and volume_button.ispressed():
            if menu_music.get_volume() > 0:
                volume_button.image = pg.image.load('images/volume_off.png')
                menu_music.set_volume(0)
            else:
                volume_button.image = pg.image.load('images/volume_on.png')
                menu_music.set_volume(0.1)
            volume_button.image = pg.transform.scale(volume_button.image, (48, 50))
            volume_button.image_copy = volume_button.image

        if button.ispressed():
            start_sound.play()
            sleep(3)
            break

        if Button.timer > 0:
            Button.timer -= 1

        for i in buttons.sprites():
            if i.ispressed() and Button.timer == 0:
                Button.sound.play()
                Button.timer = 15

        menu_coins.update('монеты:' + get_coins())

        if shop_button.ispressed():
            run_shop(True)

        pg.display.update()
        FPS.tick(60)

    run_game(True)

def run_shop(run : bool) -> None:
    menu_music.stop()
    while run:
        screen.fill("seashell1")
        item_group.update(screen)
        for i in pg.event.get():
            if i.type == pg.KEYDOWN and i.key == pg.K_ESCAPE or button_exit.ispressed():
                run = False
        button_exit.update(screen)


        pg.display.update()
        FPS.tick(60)

    menu_music.play(-1)



def run_game (run : bool) -> None:
    start_time = time.time()
    menu_music.stop()
    global bird
    global frog
    frog = Frog()
    clouds = pg.sprite.Group(Cloud(), Cloud(), Cloud(), Cloud(), Cloud(),
                             Cloud())
    bonus_cloud1 = clouds.sprites()[-1]
    bonus_cloud2 = clouds.sprites()[-1]
    while run:
        bird_timer = time.time()
        screen.fill('lightskyblue3')
        for i in pg.event.get():
            if i.type == pg.KEYDOWN:
                if i.key == pg.K_ESCAPE:
                  exit()
        for sprite in clouds:
            if sprite.status:
                clouds.add(Cloud())
                clouds.remove(sprite)

        if main_points == 1:
            pg.display.get_surface().blit(Bonus.image, Bonus.rect)
            print(2)

        if frog.rect.top > sc_size[1]:
            add_record(frog.max_height // 60)
            records.empty()
            update_records()

            break

        frog.move()
        main_points.count(frog)

        clouds.update(frog)


        clouds.draw(screen)
        screen.blit(frog.surf, frog.rect)
        frog.jump(clouds, bird, (jetpack_group, coins_group))
        frog.find_max_hight()
        frog.animate()
        screen.blit(main_points.surf, (10, 0))

        if bird_timer - start_time >= random.randrange(3, 9):
            bird = Birds()
            start_time = bird_timer
        bird.update(frog)

        if frog.max_height // 60 % 20 == 0:
            if len(coins_group.sprites()) < 1:
                coins_group.add(Bonus('coin'))
                bonus_cloud1 = clouds.sprites()[-1]
        coins_group.update(bonus_cloud1)

        if frog.max_height // 60 % 50 == 0:
            if len(jetpack_group.sprites()) < 1:
                jetpack_group.add(Bonus('jetpack'))
                bonus_cloud2 = clouds.sprites()[-1]
        jetpack_group.update(bonus_cloud2)

        coins_text.update('монеты:' + get_coins())

        pg.display.update()
        FPS.tick(60)

    clouds.empty()
    run_menu(show_result())

def show_result():
    while True:
        screen.fill('lightskyblue3')
        for i in pg.event.get():
            if i.type == pg.KEYDOWN:
                if i.key == pg.K_ESCAPE:
                    return True
        screen.blit(main_points.surf, points_rect)
        pg.display.update()
        FPS.tick(60)


run_menu(True)
