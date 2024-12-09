import pygame as pg
import sys
import random
from setting import *
from mapping import *

class game:
    def __init__(self):
        #초기화 및 화면 설정
        pg.init()
        pg.display.set_caption(TITLE)
        self.clock = pg.time.Clock()
        self.bg = pg.image.load("background.png")
        self.board = pg.image.load("board.png")
        self.board = pg.transform.scale(self.board, [250, 950])
        self.bg = pg.transform.scale(self.bg, SIZE)
        self.font = pg.font.SysFont("arial", 48, True, False)
        self.new()

    def new(self):
        #점수 등 게임 변수 설정
        self.running = True
        self.score = 0
        self.stage = 1
        self.life = 2
        self.time = 0
        self.clear = False
        self.sol_count = 0
        screen.blit(self.bg, [0, 0])

        #맵 생성
        self.mapping()

        #플레이어 및 오브젝트 생성
        self.player = Player(450, 450)
        self.player_sprites = pg.sprite.Group()
        self.player_sprites.add = self.player
        self.soul_sprites = pg.sprite.Group()
        self.brick_sprites = pg.sprite.Group()

        #텍스트 생성
        self.t_sco = text()
        self.t_sta = text()
        self.t_lif = text()

    def mapping(self):
        #22 (20 - 1 - 1) * 22 숫자맵 생성
        #0 = 빈공간, 1 = 소울, 2 = 벽
        self.m = [[0]*21 for _ in range(21)]
        self.brk = []
        self.sol = []

        #외벽 생성(2)
        for i in range(1, 20):
            self.m[i][1] = 2
            self.m[i][19] = 2
            self.m[1][i] = 2
            self.m[19][i] = 2

        #내부벽 생성(2)
        self.brick_make()

        #소울 위치 생성(1)
        for i in range(2, 20):
            for j in range(2, 20):
                if self.m[i][j] != 2:
                    self.m[i][j] = 1

        #소울, 벽 위치 보내기
        for i in range(1, 20):
            for j in range(1, 20):
                if self.m[i][j] == 1:
                    self.sol.append([i, j])
                if self.m[i][j] == 2:
                    self.brk.append([i, j])
        
        self.brick = brick(self.brk)
        self.soul = soul(self.sol)

    def brick_make(self):
        self.m = mapping(self.m, self.stage)

    def update(self):
        #모든 객체 업데이트
        self.t_sco.score(self.score)
        self.t_lif.life(self.life)
        self.t_sta.stage(self.stage)
        self.player.update()
        self.soul.collision_check(self.player.rect)
        self.sol_count = 0
        self.sol.clear()
        for i in range(1, 20):
            for j in range(1, 20):
                if self.m[i][j] == 1:
                    self.sol.append([i, j])
                    self.sol_count += 1
        if self.sol_count == 0:
            self.clear = True
        self.soul.update(self.sol)
        
    
    def draw(self):
        #모든 객체 스크린에 그리기
        screen.blit(self.bg, [0, 0])
        screen.blit(self.board, [950, 0])
        self.brick.draw()
        self.soul.draw()
        self.player.draw()
        self.t_sco.draw(1050, 350)
        self.t_sta.draw(1060, 160)
        self.t_lif.draw(1060, 525)
        pg.display.update()

    def keys(self, event):
        if event.type == pg.KEYDOWN:
            if event.key == ord('c'):
                self.new()
                
class Player():
    def __init__(self, x, y):
        self.index = 1
        self.img = False
        self.frames = []
        self.frames.append(pg.image.load('player_1.png'))
        self.frames.append(pg.image.load('player_2.png'))
        self.frames.append(pg.image.load('player_3.png'))
        self.frames.append(pg.image.load('player_4.png'))
        self.frames.append(pg.image.load('player_5.png'))
        self.image = self.frames[self.index]
        self.image = pg.transform.scale(self.image, [40, 40])
        self.rect = self.image.get_rect()
        self.rect.x = x #left
        self.rect.y = y #top
        self.x_move = 0
        self.y_move = 0
        self.last_key = 0
        self.up = False
        self.down = False
        self.left = False
        self.right = False
        self.m = False
        self.t_check = 0
        self.y_gap = 0
        self.x_gap = 0
        
    def update(self):
        self.x = round(self.rect.x / 50) + 1
        self.y = round(self.rect.y / 50) + 1
        self.up_block = g.m[self.x][self.y - 1]
        self.down_block = g.m[self.x][self.y + 1]
        self.left_block = g.m[self.x - 1][self.y]
        self.right_block = g.m[self.x + 1][self.y]

        #근처 벽돌 확인
        if  self.up_block == 2:
            self.up = False
        else :
            self.up = True
            
        if  self.down_block == 2:
            self.down = False
        else :
            self.down = True
        
        if  self.left_block == 2:
            self.left = False
        else :
            self.left = True
            
        if  self.right_block == 2:
            self.right = False
        else :
            self.right = True

        #움직임 설정
        self.x_gap = self.rect.x % 50
        self.y_gap = self.rect.y % 50
        if self.last_key == pg.K_UP and self.up == True:
            self.x_move = 0
            self.y_move = 0
            if self.x_gap == 0:
                self.y_move = -SPEED
            elif self.x_gap < 25:
                if self.x_gap >= SPEED:
                    self.x_move = -SPEED
                elif self.x_gap < 5:
                    self.x_move = -self.x_gap
            elif self.x_gap >= 25:
                if self.x_gap >= SPEED:
                    self.x_move = SPEED
                elif self.x_gap < 5:
                    self.x_move = self.x_gap

        elif self.last_key == pg.K_DOWN and self.down == True:
            self.x_move = 0
            self.y_move = 0
            if self.x_gap == 0:
                self.y_move = SPEED
            elif self.x_gap < 25:
                if self.x_gap >= SPEED:
                    self.x_move = -SPEED
                elif self.x_gap < 5:
                    self.x_move = -self.x_gap
            elif self.x_gap >= 25:
                if self.x_gap >= SPEED:
                    self.x_move = SPEED
                elif self.x_gap < 5:
                    self.x_move = self.x_gap

        elif self.last_key == pg.K_LEFT and self.left == True:
            self.x_move = 0
            self.y_move = 0
            if self.y_gap == 0:
                self.x_move = -SPEED
            elif self.y_gap < 25:
                if self.y_gap >= SPEED:
                    self.y_move = -SPEED
                elif self.y_gap < 5:
                    self.y_move = -self.y_gap
            elif self.y_gap >= 25:
                if self.y_gap >= SPEED:
                    self.y_move = SPEED
                elif self.y_gap < 5:
                    self.y_move = self.y_gap

        elif self.last_key == pg.K_RIGHT and self.right == True:
            self.x_move = 0
            self.y_move = 0
            if self.y_gap == 0:
                self.x_move = SPEED
            elif self.y_gap < 25:
                if self.y_gap >= SPEED:
                    self.y_move = -SPEED
                elif self.y_gap < 5:
                    self.y_move = -self.y_gap
            elif self.y_gap >= 25:
                if self.y_gap >= SPEED:
                    self.y_move = SPEED
                elif self.y_gap < 5:
                    self.y_move = self.y_gap
                    
        #충돌 확인
        if self.y_move < 0 and self.up == False and self.rect.y % 50 == 0:
            self.y_move = 0
        elif self.y_move > 0 and self.down == False and self.rect.y % 50 == 0:
            self.y_move = 0
        elif self.x_move < 0 and self.left == False and self.rect.x % 50 == 0:
            self.x_move = 0
        elif self.x_move > 0 and self.right == False and self.rect.x % 50 == 0:
            self.x_move = 0

        if self.x_move != 0 or self.y_move != 0:
            self.m = True
        else:
            self.m = False

        self.load_image()
            
        self.rect.x += self.x_move
        self.rect.y += self.y_move

    def load_image(self):
        if self.y_move < 0:
            self.index = 4
        elif self.y_move > 0:
            self.index = 2
        elif self.x_move > 0:
            self.index = 1
        elif self.x_move < 0:
            self.index = 3
                
        if self.m == True:
            if self.t_check > 5:
                self.t_check = 0
                if self.img == True:
                    self.img = False
                else:
                    self.img = True
                    
        if self.img == True:
            self.image = self.frames[0]
        elif self.img == False:
            self.image = self.frames[self.index]

        self.image = pg.transform.scale(self.image, [40, 40])
    
    def move(self, event):
        if event.type == pg.KEYDOWN:
            self.last_key = event.key
           
    def draw(self):
        screen.blit(self.image, [self.rect.x + 5, self.rect.y + 5])

class soul():
    def __init__(self, sol):
        self.image = pg.image.load("soul.png")
        self.image = pg.transform.scale(self.image, [10, 10])
        self.rect = self.image.get_rect()
        self.num = sol

    def collision_check(self, rect):
        for i in self.num:
            self.rect[0] = int((i[0] - 1) * 50 + 20)
            self.rect[1] = int((i[1] - 1) * 50 + 20)
            self.rect[2] = 10
            self.rect[3] = 10
            if g.player.rect.colliderect(self.rect):
                g.m[i[0]][i[1]] = 0
                g.score += 10

    def update(self, sol):
        self.num = sol

    def draw(self):
        for i in self.num:
            x = int((i[0] - 1) * 50 + 20)
            y = int((i[1] - 1) * 50 + 20)
            screen.blit(self.image, [x, y])

class brick():
    def __init__(self, brk):
        self.image = pg.image.load("Brick.png")
        self.rect = self.image.get_rect()
        self.num = brk

    def draw(self):
        for i in self.num:
            screen.blit(self.image, [(i[0]-1) * 50, (i[1]-1) * 50])

class text():
    def score(self, score):
        self.text = g.font.render("{}".format(score), True, BLACK)

    def stage(self, stage):
        self.text = g.font.render("{}".format(stage), True, BLACK)

    def life(self, life):
        self.text = g.font.render("{}".format(life), True, BLACK)
    
    def draw(self, x, y):
        screen.blit(self.text, [x, y])

screen = pg.display.set_mode(SIZE)
g = game()

while g.running:
    g.clock.tick(30)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            g.running = False
            g.keys(event)
        g.player.move(event)
    g.player.t_check += 1
    g.update()
    g.draw()
    if g.clear == True:
        print("성공!")
pg.quit()
sys.exit()
