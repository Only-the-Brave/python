#弹球游戏 by bigbigli_大李
#微信公众号：大李日志

import pygame as pg
import sys
import time

from pygame import mouse

pg.init()
screen = pg.display.set_mode((600,500))
pg.display.set_caption('弹球游戏')
#引入所需图片
ball = pg.image.load("source/ball.png")
ban = pg.image.load("source/ban.png")
bg = pg.image.load("source/bg.jpg")

#设置球的起始坐标
ball_x,ball_y = 400,20
#球每次动的距离
move_x,move_y = 3,3

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
    #球开始移动
    ball_x += move_x
    ball_y += move_y

    #板子随着鼠标移动
    mouse_x,mouse_y = pg.mouse.get_pos()

    #球碰撞反弹
    if ball_x <= 0 or ball_x >= 560:
        move_x = -move_x
    if ball_y <= 0:
        move_y = -move_y
    
    #球碰到板子反弹，否则失败
    if ball_y > 440:
        if ball_x > mouse_x - 10 and ball_x < mouse_x + 120:
            move_y = -move_y
        else:
            pg.quit()
            sys.exit()
    #画图片：背景、球、板子
    screen.blit(bg,(0,0))
    screen.blit(ball,(ball_x,ball_y))
    screen.blit(ban,(mouse_x,478))
    pg.display.update()
    time.sleep(0.01)