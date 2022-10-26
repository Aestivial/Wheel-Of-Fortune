from cProfile import label
from itertools import count
from time import sleep
from tkinter import *
import random
from tkinter.font import BOLD
from turtle import left

def nextpress():
    global count
    if count==250:
        count=0
        flash(T)
        return
    else:
        global Content
        Content = random.choice(data)
        T.delete("1.0",END)
        T.insert(END,Content)
        count=count+25
        T.after(count, nextpress)

def flash(self):
    bg = self.cget("background")
    fg = self.cget("foreground")
    self.configure(background=fg, foreground=bg)

def addwindow():
    aw = Toplevel(gui)
    aw.title("Adding new items:")
    aw.geometry("400x200")
    l=Label(aw, text="Enter the new items to add to the list", font=("Courier", 10, BOLD))
    l.pack()
    t=Text(aw, height=5, width=50, bg="powder blue").pack()
    add = Button(aw, text = 'Add To List', command = addtolist).pack(pady=5)
    close=Button(aw, text="Close", fg="red", command=aw.destroy).pack(pady=5)

def addtolist():
    global t
    txt = t.get(1.0, "end-1c")
    print(txt)

datab = open("Database\\ListOfPrizes.txt",'r')
data = datab.readlines()
datab.close()

#Driver Code
if __name__=="__main__":

    #Configuring Main Window
    gui=Tk()
    gui.configure(background="powder blue")
    gui.title("Wheel Of Fortune")
    gui.geometry("620x300")

    #The buttons and widgets
    l = Label(gui, text="Result", bg="powder blue", fg="navy blue")
    l.config(font=("Courier", 14, BOLD))
    l.pack(pady=30)

    T = Text(gui, bg="#06283D", fg="#9CFF2E", height=3, width=52, font=14)
    T.pack()

    Content = random.choice(data)
    count=0

    next=Button(gui, text="Start", fg="blue", command=nextpress).pack(pady=5)
    close=Button(gui, text="Close", fg="red", command=gui.destroy).pack(pady=5)
    add=Button(gui, text = 'Add New Items', command = addwindow).pack(pady=5)
    
    T.insert(END,Content)
    gui.mainloop()