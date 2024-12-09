from tkinter import*

class t:
    def __init__(self):
        self.win = Tk() #Tk()를 window 라는 변수명으로 불러온다
        self.win.geometry("600x200")
        Label(self.win,text="화1씨").grid(row=0,column=0)
        Label(self.win,text="섭씨").grid(row=1,column=0)
        self.e1 = Entry(self.win)
        self.e1.grid(row=0,column=1)
        self.e2 = Entry(self.win)
        self.e2.grid(row=1,column=1)
        self.button=Button(self.win,text="화씨-> 섭씨", command=self.tk)
        self.button.grid(row=3,column=0,columnspan=2)

    def tk (self):
        tf = float(self.e1.get())
        tc = (tf-32.0)*5.0/9.0
        self.e2.delete(0,END)
        self.e2.insert(0,str(tc))

a = t()
a.win.mainloop()

# Label(win,text="화씨").grid(row=0,column=0)
# Label(win,text="섭씨").grid(row=1,column=0)
# e1 = Entry(win).grid(row=0,column=1)
# e2 = Entry(win).grid(row=1,column=1)
# button=Button(win,text="화씨-> 섭씨", command=tk)
# button.grid(row=3,column=0,columnspan=2)
# win.mainloop()