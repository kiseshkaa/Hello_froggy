import pygame as pg
from test_file import Player

screen = pg.display.set_mode((500, 500))
FPS = pg.time.Clock()
ball = pg.Surface((30, 30))
ball_rect = ball.get_rect(center = (250, 250))
dir = 1
plank_2 = Player((20, 20))
plank_3 = Player((60, 60))
plank_4 = Player((200, 200))
group = pg.sprite.Group()
group.add(plank_2, plank_3, plank_4)

while True:
    screen.fill('lightskyblue3')
    for i in pg.event.get():
        if i.type == pg.KEYDOWN:
            if i.key == pg.K_ESCAPE:
                exit()
    ball_rect.left -= 1 * dir
    group.draw(screen)
    group.update()

    screen.blit(ball, ball_rect)
    FPS.tick(60)
    pg.display.update()
