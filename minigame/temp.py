import pygame as pg
import os, time
from pygame.locals import *

WIDTH = 1280
HEIGHT = 720
SIZE = [WIDTH, HEIGHT]
TITLE = "SH mini game"
WHITE = (255, 255, 255)
FRAME = 120
BOX_POS = [150, 0]
LINE_WIDTH = 110


def isin(v, a, b):
    if v > a and v < b: return True
    return False

class set():
    # 초기화 및 변수 지정    
    def __init__(self):
        # 스크린 설정
        self.screen = pg.display.set_mode(SIZE, HWSURFACE | DOUBLEBUF)
        self.title = pg.display.set_caption(TITLE)
        self.clock = pg.time.Clock()

        # 오프닝 변수
        self.menu_state = 0 #main, ready, instruction
        self.op_select = 0

        # 인게임 변수
        self.running = True
        self.state = 2
        self.pressed_key = []
        self.lastkey = []
        self.usedkey = [pg.K_d, pg.K_f, pg.K_j, pg.K_k]
        self.speed = 1

        self.line_height = 620
        self.timing = 565
        self.gap = self.line_height - self.timing
        self.load_data()
        #메뉴 이미지
        # self.bg_instruction = pg.image.load("first_copy/image/instruction.png")
        # self.bg_gameover = [] # Yes, No
        # self.bg_gameover.append(pg.image.load("first_copy/image/game_over_screen_yes.png"))
        # self.bg_gameover.append(pg.image.load("first_copy/image/game_over_screen_no.png"))
        # self.bg_ready = [] # Nor, Eas, Har
        # self.bg_ready.append(pg.image.load("first_copy/image/ready_screen_easy.png"))
        # self.bg_ready.append(pg.image.load("first_copy/image/ready_screen_nomal.png"))
        # self.bg_ready.append(pg.image.load("first_copy/image/ready_screen_hard.png"))
        # self.bg_menu = [] # Str, Dis, Exi
        # self.bg_menu.append(pg.image.load("first_copy/image/background1.png"))
        # self.bg_menu.append(pg.image.load("first_copy/image/background0.png")) 
        # self.bg_menu.append(pg.image.load("first_copy/image/background2.png"))

        # self.img_mani = [] # C, L, R
        # self.img_mani.append(pg.image.load("first_copy/image/menu1.png"))
        # self.img_mani.append(pg.image.load("first_copy/image/menu0.png"))
        # self.img_mani.append(pg.image.load("first_copy/image/menu2.png")) 
    
    def load_data(self):
        self.dir = os.path.dirname(__file__)
        self.img_dir = os.path.join(self.dir, "image")
        #인게임 이미지
        self.bg_ingame = pg.image.load(os.path.join(self.img_dir, "background.png"))
        self.bg_skin = pg.image.load(os.path.join(self.img_dir, "Skin.png"))
        
        self.img_line = pg.image.load(os.path.join(self.img_dir, "Line.png"))
        self.img_line_pre = pg.image.load(os.path.join(self.img_dir, "Line_pressed.png"))
        self.img_health_bar = pg.image.load(os.path.join(self.img_dir, "health_bar.png"))
        self.btn_pre = [] #cen, sid
        self.btn_pre.append(pg.image.load(os.path.join(self.img_dir, "btn_pre_cen.png")))
        self.btn_nor = [] 
        self.btn_nor.append(pg.image.load(os.path.join(self.img_dir, "btn_nor_cen.png")))
        self.img_score = []
        self.img_score.append(pg.image.load(os.path.join(self.img_dir, "Exerlent.png")))
        self.img_score.append(pg.image.load(os.path.join(self.img_dir, "Good.png")))
        self.img_score.append(pg.image.load(os.path.join(self.img_dir, "Bad.png")))
        self.img_score.append(pg.image.load(os.path.join(self.img_dir, "Miss.png")))
        self.img_note = []
        self.img_note.append(pg.image.load(os.path.join(self.img_dir, "note_cen.png")))
        self.img_note.append(pg.image.load(os.path.join(self.img_dir, "note_sid.png")))

        self.num = []
        for i in range(10):
            self.num.append(pg.image.load(os.path.join(self.img_dir, "n_w_{}.png".format(i))))
        self.new_song() #나중에 지우기

    def run(self):
        if self.state == 1: self.opening()
        elif self.state == 2: self.ingame()
        self.lastkey = []
        pg.display.update()

    def opening(self):
        if self.menu_state == 0: self.screen.blit(self.bg_menu[self.op_select], [0, 0])
        elif self.menu_state == 1: self.screen.blit(self.bg_ready[self.op_select], [0, 0])
        else: self.screen.blit(self.bg_instruction, [0, 0])
    
        if self.lastkey != []:
            if pg.K_LEFT in self.lastkey:
                self.op_select -= 1 if self.op_select != 0 else 0
            elif pg.K_RIGHT in self.lastkey:
                self.op_select += 1 if self.op_select != 2 else 0
            elif pg.K_SPACE in self.lastkey:
                if self.menu_state == 0: # when main
                    if self.op_select == 0: self.menu_state = 1 # main to ready
                    elif self.op_select == 1: self.menu_state = 2 # main to instruction
                elif self.menu_state == 1: # when ready
                    if self.op_select == 0: print("easy") # easy
                    elif self.op_select == 1: print("normal") # easy
                    else: print("hard") # easy
                    self.new_song()
                    self.state = 2 # goto ingame!

            elif pg.K_ESCAPE in self.lastkey:
                self.menu_state = 0

    def new_song(self):
        self.note_num = 0
        self.song_note = [[1.0, 1], [2.0, 3], [3.0, 1], [4.0, 3], [5.0, 1], [6.0, 3], [7.0, 3], [8.0, 1]]
        self.bpm = 128
        self.start_ticks = pg.time.get_ticks()
        self.inscreen_note = []
        self.metro = [4, 4]
        self.last_score = 0
        self.score = 0
        self.life = 100
        self.fps_sum = 0
        self.fps = 0
        self.last_time = 0

    def ingame(self):
        self.update()
        self.draw()

    def update(self):
        self.ingame_time = (pg.time.get_ticks() - self.start_ticks) / 1000
        self.fps_sum += self.ingame_time - self.last_time
        self.fps += 1
        self.fps_avg = round(self.fps_sum / self.fps, 3)
        self.last_time = self.ingame_time
        print(self.ingame_time)

    def draw(self):
        pass
        # pg.draw.rect(self.screen, [50, 50, 50], [0, 0, 1280, 720])
        # self.screen.blit(self.img_line, BOX_POS)
        # self.screen.blit(self.img_health_bar, [860, 0])
        # self.screen.blit(self.bg_skin, [70, 0])
        # pg.draw.rect(self.screen, [255, 147, 30], [868, 8, (404 * self.life * 0.01), 32])
        # temp = self.score #Score
        # for i in range(6):
        #     self.screen.blit(self.white_num[temp % 10], [1240-(i*25), 50])
        #     temp = temp // 10

        # for i in range(4):
        #     if self.usedkey[i] in self.pressed_key:
        #         self.screen.blit(self.img_line_pre, [BOX_POS[0]+(LINE_WIDTH*i), 220])
        #         self.screen.blit(self.btn_pre[0], [BOX_POS[0]+(LINE_WIDTH*i), 620])
        #     else: 
        #         self.screen.blit(self.btn_nor[1], [BOX_POS[0]+(LINE_WIDTH*i), 620])
        # for i, note in enumerate(self.inscreen_note):
        #     self.screen.blit(self.img_note[0], [BOX_POS[0]+(LINE_WIDTH*i), note[0]])
        #     self.inscreen_note[i][0] += self.note_speed

        

        
g = set()
while g.running:
    g.run()
    g.clock.tick(FRAME)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            print(g.fps_avg)
            g.running = False
        if event.type == pg.KEYDOWN:
            g.pressed_key.append(event.key)
            g.lastkey.append(event.key)
        if event.type == pg.KEYUP:
            g.pressed_key.remove(event.key)

    g.run()


#할일
# 콤보 만들기
# 점수 구현
# 맞출 경우 효과
# 목숨 만들기
