

import itertools, sys, time, random, math, pygame
from pygame import display
from pygame import image
from pygame.locals import *
from MyLibrary import *

go = pygame.image.load("img/gameover.jpg")
gameover = pygame.transform.scale(go,(870,600))
victory = pygame.image.load("img/victory.jpg")

t = 60 #时间
coin_cnt = 0

def calc_velocity(direction, vel=1.0):
    velocity = Point(0,0)
    if direction == 0: #向上
        velocity.y = -vel
    elif direction == 2: #向右
        velocity.x = vel
    elif direction == 4: #向下
        velocity.y = vel
    elif direction == 6: #向左 
        velocity.x = -vel
    return velocity

def reverse_direction(sprite):
    if sprite.direction == 0:
        sprite.direction = 4
    elif sprite.direction == 2:
        sprite.direction = 6
    elif sprite.direction == 4:
        sprite.direction = 0
    elif sprite.direction == 6:
        sprite.direction = 2

pygame.init()
screen = pygame.display.set_mode((870,600))
ico = pygame.image.load("img/ico.png")
pygame.display.set_icon(ico)
pygame.display.set_caption("坚持60秒")
timer = pygame.time.Clock()

player_group = pygame.sprite.Group()
zombie_group = pygame.sprite.Group()
coin_group = pygame.sprite.Group()

#bili诞生之日
player = MySprite()
player.load("img/bili.png", 96, 96, 8)
player.position = 300,280
player.direction = 4
player_group.add(player)

#创建僵尸
zombie_image = pygame.image.load("img/zombie.png").convert_alpha()
for n in range(0, 10):
    zombie = MySprite()
    zombie.load("img/zombie.png", 96, 96, 8)
    zombie.position = random.randint(0,780), random.randint(100,500)
    zombie.direction = random.randint(0,3) * 2
    zombie_group.add(zombie)

#创建宝币
coin = MySprite()
coin.load("img/coin.png", 32, 32, 1)
coin.position = 400,300
coin_group.add(coin)

#创建背景
bg = pygame.image.load("img/bg.png")

game_over = False
player_moving = False
player_health = 100

while True:
    timer.tick(30)
    ticks = pygame.time.get_ticks()

    for event in pygame.event.get():
        if event.type == QUIT: sys.exit()
    keys = pygame.key.get_pressed()
    if keys[K_ESCAPE]: sys.exit()
    elif keys[K_UP] or keys[K_w]:
        player.direction = 0
        player_moving = True
    elif keys[K_RIGHT] or keys[K_d]:
        player.direction = 2
        player_moving = True
    elif keys[K_DOWN] or keys[K_s]:
        player.direction = 4
        player_moving = True
    elif keys[K_LEFT] or keys[K_a]:
        player.direction = 6
        player_moving = True
    else:
        player_moving = False


    if not game_over:
        #设置动画帧
        player.first_frame = player.direction * player.columns
        player.last_frame = player.first_frame + player.columns-1
        if player.frame < player.first_frame:
            player.frame = player.first_frame

        if not player_moving:
            player.frame = player.first_frame = player.last_frame
        else:
            #玩家行走
            player.velocity = calc_velocity(player.direction, 1.5)
            player.velocity.x *= 3.5
            player.velocity.y *= 3.5

        player_group.update(ticks, 50)

        if player_moving:
            player.X += player.velocity.x
            player.Y += player.velocity.y
            if player.X < 0: player.X = 0
            elif player.X > 780: player.X = 780
            if player.Y < 100: player.Y = 100
            elif player.Y > 500: player.Y = 500

        zombie_group.update(ticks, 50)

        for z in zombie_group:
            #设置僵尸运动范围
            z.first_frame = z.direction * z.columns
            z.last_frame = z.first_frame + z.columns-1
            if z.frame < z.first_frame:
                z.frame = z.first_frame
            z.velocity = calc_velocity(z.direction)
            z.X += z.velocity.x * 2
            z.Y += z.velocity.y * 2
            if z.X < 0 or z.X > 780 or z.Y < 100 or z.Y > 500:
                reverse_direction(z)    

        #侦测与僵尸是否发生碰撞
        attacker = None
        attacker = pygame.sprite.spritecollideany(player, zombie_group)
        if attacker != None:
            if pygame.sprite.collide_rect_ratio(0.5)(player,attacker):
                player_health -= 10
                if attacker.X < player.X:   attacker.X -= 10
                elif attacker.X > player.X: attacker.X += 10
            else:
                attacker = None

        coin_group.update(ticks, 50)

        #侦测与硬币是否发生碰撞
        if pygame.sprite.collide_rect_ratio(0.5)(player,coin):
            coin_cnt += 1
            coin.X = random.randint(20,780)
            coin.Y = random.randint(100,500)
        
    #判断bili是否还活着 时间&血量检测
    t = t-1/30
    if player_health <= 0 or t <= 0:
        game_over = True

    screen.blit(bg,(0,0))
    coin_group.draw(screen)
    zombie_group.draw(screen)
    player_group.draw(screen)

    #时间
    font = pygame.font.Font("img/Lmovie.ttf",50)
    print_text(font,600,90,str(t//1),"red")

    #血条
    font = pygame.font.Font("img/kaiti.ttf", 25)
    print_text(font, 20, 90, "血量:","red")
    pygame.draw.rect(screen, (50,100,50,180), Rect(77,90,player_health*2,25))

    #硬币收集数
    font = pygame.font.Font("img/Lmovie.ttf",50)
    print_text(font, 420, 50, str(coin_cnt),"green")

    #胜利判断
    if coin_cnt >= 6: 
        screen.blit(victory,(0,0))
        font = pygame.font.Font("img/kaiti.ttf", 50)

    #失败判断
    if game_over:
        screen.blit(gameover,(0,0))
        font = pygame.font.Font("img/kaiti.ttf", 50)
        print_text(font, 125, 450, "bili：大李，你救救我啊！！！")

    pygame.display.update()
