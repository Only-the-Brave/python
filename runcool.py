

import pygame as pg
import sys
import time
import random

pg.init()     
screen = pg.display.set_mode((800,500))
pg.display.set_caption('runcool')
screen.fill((135, 206, 235))
bili = pg.image.load('bili.png')

#得分
coin = 0
game_font = pg.font.Font(None, 50)

#人物大小
man = pg.transform.scale(bili, (60, 85))
man_x, man_y = 200, 415
onfloor = 1                 #是否在地面上
gravity = 0.2               #重力加速度
man_vy = 0                  #Y方向速度
passed = True               #跳过加分

#初始化障碍物
piece = pg.Surface((30,200))
piece.fill((255, 255, 255))
piece_x, piece_y = 800, 410

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_SPACE and onfloor == 1:
                man_vy = -10
                onfloor = 0
    man_vy += gravity                   # V = V0 + at
    man_y += man_vy                     # S = V0t + 1/2 a * t * t = V平 * t

    if man_y >= 415:
        man_vy = 0
        man_y = 415
        onfloor = 1

    #绘制背景及人物
    screen.fill((135,206,235))
    screen.blit(man,(man_x,man_y))
    #绘制障碍物
    screen.blit(piece,(piece_x,piece_y))
    piece_x -= 2
    if piece_x <= 0:
        passed = True
        piece_y = random.randint(350, 450)
        piece_x = 850

    #得硬币检测
    if piece_x < man_x and passed:
        coin += 1
        passed = False

    #绘制硬币得分
    screen.blit(game_font.render('coin: %d' % coin, True, [255, 0, 0]), [20, 20])
    #碰撞检测
    if man_x+60 >= piece_x and man_x <= piece_x+30 and man_y+85 >= piece_y:
        print('得分: %d' % coin) 
        pg.quit()
        sys.exit()

    pg.display.update()
    time.sleep(0.005)
