import pygame
import random

def frame_num(self):
    columns = 9
    rows = 5

    # 스크린 여백
    screen_left_margin = 55
    screen_top_margin = 20
    # 셀 사이즈
    cell_size = 130
    # 버튼 크기
    num_button = 110
    
    # 나오는 숫자의 개수
    num_count = 6 + (self.level // 2)
    max_num_count = min(num_count, 10) # 최대 10개 이하
    
    # 게임에 나오는 숫자 번호
    num_list = range(1, max_num_count)
    n = 0 # num_list 숫자를 꺼내기 위한 변수
    
    # 숫자 버튼 좌표설정 및 rect받기
    num_list_show = self.num_font.render(str(num_list), True, self.WHITE)
    num_list_show_rect= num_list_show.get_rect()
    num_list_x = num_list_show.get_width()
    num_list_y = num_list_show.get_height()
    
    frame = [[0 for col in range(0, columns)] for row in range(0, rows)] # 격자 생성
    
    # 격자안의 숫자 위치를 생성할 랜덤 행과 열번호를 생성
    for row in range(0, rows): # 행 5개
        frame_row = random.randrange(0, rows)
        for col in range(0, columns): # 열 9개
            frame_col = random.randrange(0, columns)
        
        # 격자안에 게임에 나오는 숫자 번호를 기입
        frame[frame_row][frame_col] = num_list[n]
        
        num_list_show_x = screen_left_margin + (num_list_x * frame_col) - (num_list_x / 2)
        num_list_show_y = screen_top_margin + (num_list_y * frame_row) - (num_list_y / 2)
        num_list_show_center = (num_list_show_x, num_list_show_y)
        
        self.screen.blit(num_list_show, num_list_show_center)

        # for루프가 한번 돌때마다 num_list의 n번째 정수를 가져오기위해 추가
        n += 1

    print(frame)


# 기억력 게임
class g1:
    def game_screen(self):
        # num_list를 받아 오고 함수를 실행 시킴
        self.frame_num(self)

    # 게임 시작 버튼 클릭(충돌)
    def collide(self, click_pos):
        # 스타트 버튼을 클릭하면 일어 나는 일
        if self.start_btn_rect.collidepoint(click_pos):
            self.state = 1
            self.game_screen(self)
            print(self.state)

    def __init__(self):

        # 파이 게임 스크린 설정
        self.screen_width = 1280 # 창 가로 넓이
        self.screen_height = 720 # 창 세로 길이

        # 스타트 버튼 설정
        self.start_btn = pygame.image.load("/Users/kimsoohyeong/Desktop/Project Python/first_copy/image/start_button.png")
        self.start_btn_width = self.start_btn.get_width()
        self.start_btn_height = self.start_btn.get_height()
        self.start_btn_x = (self.screen_width / 2) - (self.start_btn_width / 2)
        self.start_btn_y = (self.screen_height / 2) - (self.start_btn_height / 2)
        self.start_btn_center = (self.start_btn_x, self.start_btn_y)
        self.start_btn_rect_center = ((self.screen_width / 2), (self.screen_height / 2))
        self.start_btn_rect = self.start_btn.get_rect(center = (self.start_btn_rect_center))

        # 레벨
        self.level = 1

        # 색깔 정의
        self.BLACK = (0, 0, 0)
        self.WHITE = (255, 255, 255)
        self.GRAY = (0, 0 , 255)
        
        # 게임 실행 여부 변수
        self.run = True

        # 기억력 게임 실행 상황 변수
        self.state = 0 # 게임 시작 전
        # self.state = 1 # 게임 중
        # self.state = 2 # 게임 오버
        
        pygame.init() # 파이 게임 초기화
        
        # 폰트
        self.num_font = pygame.font.Font(None, 80)

        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height)) # 파이게임 스크린 화면 크기 지정
        pygame.display.set_caption("remember") # 파이게임 이름 캡션 설정

        # 게임 루프 돌리기
        while self.run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT: # 게임 종료 이벤트를 받았다면?
                    self.run = False # 게임 실행 여부 FALSE로 설정(While 루프 탈출)
                if event.type == pygame.MOUSEBUTTONUP:
                    self.click_pos = pygame.mouse.get_pos()
                    print(self.click_pos)
                    self.collide(self.click_pos)

            # 화면 검정으로 칠하기
            self.screen.fill(self.BLACK)
            # 스타트 버튼 그리기
            self.screen.blit(self.start_btn, self.start_btn_center)


            pygame.display.update()
            

        pygame.display.update()

        pygame.display.quit()
g1()