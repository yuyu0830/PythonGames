from tkinter import *
import math

#변수
TITLE = "계산기"
SIZE = "270x250+400+100"
x = [10, 75, 140, 205]
y = list()
temp = 0

for i in range(8):
    y.append(temp+10)
    temp += 30
    
sign_list = ['+', '-', '*', '/']
number = 0
numbers = list()
signs = list()
memory = 0

#함수
def num_pressed(value):
    global number
    state = 0
    if len(e3.get()) == 0:
        e3.insert(0, value)
        number = value
    else:
        try:
            int(e3.get())
            temp_num = int(e3.get())
            state = 0
        except ValueError:
            temp_num = float(e3.get())
            state = 1
        e3.delete(0, 'end')
        if state == 0:
            number = temp_num * 10 + value
            e3.insert(0, number)
            
def sign_pressed(value):
    global number
    global numbers
    global signs
    global sign_list
    if number != 0:
        e3.delete(0, 'end')
        numbers.append(number)
        signs.append(sign_list[value])
        e1.delete(0, 'end')
        for i in reversed(range(len(numbers))):
            e1.insert(0, signs[i])
            e1.insert(0, numbers[i])
        number = 0
    elif len(signs) != 0:
        e1.delete(0, 'end')
        signs.pop(len(signs) - 1)
        signs.append(sign_list[value])
        for i in reversed(range(len(numbers))):
            e1.insert(0, signs[i])
            e1.insert(0, numbers[i])
        number = 0
    
def button_pressed(value):
    global number
    global numbers
    global signs
    if value == 0:
        number = math.trunc(number / 10)
        e3.delete(0, 'end')
        e3.insert(0, number)
    elif value == 1:
        number = 0
        e3.delete(0, 'end')
    elif value == 2:
        number = 0
        numbers.clear()
        signs.clear()
        e1.delete(0, 'end')
        e3.delete(0, 'end')

def equal():
    global numbers
    global signs
    global number
    i = 0
    result = 0
    e1.delete(0, 'end')
    e3.delete(0, 'end')
    e1.insert(0, number)
    for i in reversed(range(len(numbers))):
        e1.insert(0, signs[i])
        e1.insert(0, numbers[i])
    length = len(signs)
    numbers.append(number)
    while i != length:
        if signs[i] == '*':
            numbers[i] = numbers[i] * numbers[i + 1]
            signs.pop(i)
            numbers.pop(i+1)
            length -= 1
            i = 0
        elif signs[i] == '/':
            numbers[i] = numbers[i] / numbers[i + 1]
            signs.pop(i)
            numbers.pop(i+1)
            length -= 1
            i = 0
        else:
            i += 1
    print(numbers, signs)
    result = numbers[0]
    for i in range(len(signs)):
        if signs[i] == '+':
            result += numbers[i + 1]
        elif signs[i] == '-':
            result -= numbers[i + 1]
    e2.insert(0, result)
    numbers.clear()
    signs.clear()



window = Tk()
window.title(TITLE)
window.geometry(SIZE)
window.resizable(False, False)

e1 = Entry(window, width = 35)
e1.place(x = 10, y = y[0])
e2 = Entry(window, width = 15)
e2.place(x = 10, y = y[1])
e3 = Entry(window, width = 15)
e3.place(x = 150, y = y[1])

m_mc = Button(window, text = "MC", width = 6, command = lambda:memory_pressed(3)).place(x = x[0], y = y[2])
m_mr = Button(window, text = "MR", width = 6, command = lambda:memory_pressed(2)).place(x = x[1], y = y[2])
m_pl = Button(window, text = "M+", width = 6, command = lambda:memory_pressed(1)).place(x = x[2], y = y[2])
m_mi = Button(window, text = "M-", width = 6, command = lambda:memory_pressed(0)).place(x = x[3], y = y[2])
b_ac = Button(window, text = "AC", width = 6, command = lambda:button_pressed(2)).place(x = x[0], y = y[3])
b_cl = Button(window, text = "C", width = 6, command = lambda:button_pressed(1)).place(x = x[1], y = y[3])
b_dl = Button(window, text = "<=", width = 6, command = lambda:button_pressed(0)).place(x = x[2], y = y[3])
b_eq = Button(window, text = "=", width = 6, command = lambda:equal()).place(x = x[3], y = y[7])
s_di = Button(window, text = "/", width = 6, command = lambda:sign_pressed(3)).place(x = x[3], y = y[3])
s_mu = Button(window, text = "*", width = 6, command = lambda:sign_pressed(2)).place(x = x[3], y = y[4])
s_mi = Button(window, text = "-", width = 6, command = lambda:sign_pressed(1)).place(x = x[3], y = y[5])
s_pl = Button(window, text = "+", width = 6, command = lambda:sign_pressed(0)).place(x = x[3], y = y[6])
n_do = Button(window, text = ".", width = 6).place(x = x[2], y = y[7])
n_pm = Button(window, text = "+-", width = 6).place(x = x[0], y = y[7])
n9 = Button(window, text = "9", width = 6, command = lambda:num_pressed(9)).place(x = x[2], y = y[4])
n8 = Button(window, text = "8", width = 6, command = lambda:num_pressed(8)).place(x = x[1], y = y[4])
n7 = Button(window, text = "7", width = 6, command = lambda:num_pressed(7)).place(x = x[0], y = y[4])
n6 = Button(window, text = "6", width = 6, command = lambda:num_pressed(6)).place(x = x[2], y = y[5])
n5 = Button(window, text = "5", width = 6, command = lambda:num_pressed(5)).place(x = x[1], y = y[5])
n4 = Button(window, text = "4", width = 6, command = lambda:num_pressed(4)).place(x = x[0], y = y[5])
n3 = Button(window, text = "3", width = 6, command = lambda:num_pressed(3)).place(x = x[2], y = y[6])
n2 = Button(window, text = "2", width = 6, command = lambda:num_pressed(2)).place(x = x[1], y = y[6])
n1 = Button(window, text = "1", width = 6, command = lambda:num_pressed(1)).place(x = x[0], y = y[6])
n0 = Button(window, text = "0", width = 6, command = lambda:num_pressed(0)).place(x = x[1], y = y[7])
