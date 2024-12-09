from tkinter import *
import random as rd
import time

class typing:
    def __init__(self):
        self.line = list()
        self.accuracy = 0
        self.acc_group = list()
        self.count = 0
        self.speed = 0
        self.spd_group = list()
        self.score = 0
        self.line1 = ""
        self.line2 = ""
        self.num = 0

        #tkinter 설정1
        self.window = Tk()
        self.window.title("타자연습")
        self.window.geometry("540x200+400+100")
        self.window.resizable(False, False)
        
        #tkinter 설정2
        self.title = Label(self.window, text = "타자연습").place(x = 100, y = 30)
        self.show1 = Label(self.window, textvariable = self.line1, width = 40, anchor='w').place(x = 75, y = 70)
        self.show2 = Label(self.window, textvariable = self.line2, width = 40, anchor='w').place(x = 75, y = 150)
        self.now = Label(self.window, text = "현재 문장 :").place(x = 10, y = 70)
        self.next_line = Label(self.window, text = "다음 문장 :").place(x = 10, y = 150)
        self.accuracy1 = Label(self.window, text = "정확도").place(x = 350, y = 10)
        self.accuracy2 = Label(self.window, textvariable = self.accuracy).place(x = 450, y = 10)
        self.speed1 = Label(self.window, text = "속도").place(x = 350, y = 50)
        self.speed2 = Label(self.window, textvariable = self.speed).place(x = 450, y = 50)
        self.score1 = Label(self.window, text = "점수").place(x = 350, y = 90)7
        self.score2 = Label(self.window, textvariable = self.score).place(x = 450, y = 90)
        self.count1 = Label(self.window, text = "완료한 문장 수").place(x = 350, y = 130)
        self.count2 = Label(self.window, textvariable = self.count).place(x = 450, y = 130)

        self.follow = Entry(self.window, width = 35).place(x = 75, y = 100)

        self.enter = Button(self.window, text = "입력").place(x = 75, y = 123)
        self.new = Button(self.window, text = "새로하기", width = 10).place(x = 350, y = 170)
        self.end = Button(self.window, text = "그만하기", width = 10).place(x = 450, y = 10)

        #파일읽기
        file = open("list.txt", 'r', encoding="UTF8")
        temp = file.readlines()
        for lines in temp:
            line_temp = lines.strip()
            self.line.append(line_temp)
        file.close()

    def play(self):
        self.line1 = self.line[self.num]
        if num < len(self.line):
            self.line2 = self.line[self.num + 1]
        self.acc_group.append(self.accuracy)
        self.spd_group.append(self.speed)
        sta = round(time.time(), 3)
        while True:
            en = self.follow.get("1.0", "end")
            if len(en) != 0:
                count = 0
                for i in range(len(en)) if len(en) < len(line) else range(len(line)):
                    if en[i] == line[i]:
                        count += 1
                now = round(time.time(), 3)
                self.speed = (60 / (sta - now)) * len(en)
                self.accuracy = int(round(count / len(en), 2) * 100)
        self.num += 1

    
num = 0
run = typing()
run.follow.bind("<KEY>", run.play(num))
run.window.mainloop()
            
