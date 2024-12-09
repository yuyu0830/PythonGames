from tkinter import *
import time

#변수
line = list()
sta = 0
acc = 0
spd = 0
num = 0
acc_group = list()
spd_group = list()
accA = 0
spdA = 0
scr = 0
timer = 0
snt = ""
acc_group = list()
spd_group = list()
TITLE = "타자연습"
SIZE = "540x200+400+100"

#함수
def setting():
    global num
    global snt
    global sta
    snt = line[num]
    show1.delete(0, 'end')
    show1.insert(0, line[num])
    show2.delete(0, 'end')
    show2.insert(0, line[num+1])
    sta = round(time.time(), 3)

def end(event):
    global num
    global snt
    global sta
    count = 0
    en = ent.get()
    now = round(time.time(), 3)
    spd = int((60 / (now - sta)) * len(en))
    for i in range(len(en)) if len(en) < len(snt) else range(len(snt)):
        if en[i] == snt[i]:
            count += 1
    acc = int(round(count / len(en), 2) * 100)
    acc_group.append(acc)
    spd_group.append(spd)
    count = 0
    for i in acc_group:
        count += i
        accA = int(count / len(acc_group))
    count = 0
    for i in spd_group:
        count += i
        spdA = int(count / len(spd_group))
    accV.delete(0, 'end')
    accV.insert(0, acc)
    spdV.delete(0, 'end')
    spdV.insert(0, spd)
    accAV.delete(0, 'end')
    accAV.insert(0, accA)
    spdAV.delete(0, 'end')
    spdAV.insert(0, spdA)
    num += 1
    ent.delete(0, 'end')
    show1.delete(0, 'end')
    show1.insert(0, line[num])
    show2.delete(0, 'end')
    show2.insert(0, line[num+1])
    snt = line[num]
    sta = round(time.time(), 3)

#tkinter 설정
window = Tk()
window.title(TITLE)
window.geometry(SIZE)
window.resizable(False, False)

title = Label(window, text = "타자연습").place(x = 100, y = 30)
now = Label(window, text = "현재 문장 :").place(x = 10, y = 70)
nex = Label(window, text = "다음 문장 :").place(x = 10, y = 150)
accT = Label(window, text = "정확도").place(x = 350, y = 10)
spdT = Label(window, text = "속도").place(x = 350, y = 50)
accAT = Label(window, text = "평균 정확도").place(x = 350, y = 90)
spdAT = Label(window, text = "평균 속도").place(x = 350, y = 130)

show1 = Entry(window, width = 35)
show1.place(x = 75, y = 70)
show2 = Entry(window, width = 35)
show2.place(x = 75, y = 150)
ent = Entry(window, width = 35)
ent.place(x = 75, y = 100)
accV = Entry(window, width = 5)
accV.place(x = 450, y = 10)
spdV = Entry(window, width = 5)
spdV.place(x = 450, y = 50)
accAV = Entry(window, width = 5)
accAV.place(x = 450, y = 90)
spdAV = Entry(window, width = 5)
spdAV.place(x = 450, y = 130)

start = Button(window, text = "시작", command = lambda:setting())
start.place(x = 75, y = 122)
inp = Button(window, text = "입력", command = lambda:end(1))
inp.place(x = 125, y = 122)
new = Button(window, text = "새로하기", width = 10).place(x = 350, y = 170)
esc = Button(window, text = "그만하기", width = 10).place(x = 450, y = 170)

#파일 읽기
file = open("list.txt", 'r', encoding="UTF8")
temp = file.readlines()
for lines in temp:
    line_temp = lines.strip()
    line.append(line_temp)
file.close()

window.bind("<Return>", end)
window.mainloop()
