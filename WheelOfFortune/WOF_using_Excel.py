from cProfile import label
from itertools import count
from time import sleep
from tkinter import *
import random
from tkinter.font import BOLD
import pandas as pd

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

data = pd.read_excel('Database\\ListOfItems.xlsx',sheet_name='Prizes')
data = data['Prizes'].tolist()

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

    T = Text(gui, bg="#06283D", fg="#9CFF2E", height=5, width=52, font=14)
    T.pack()

    Content = random.choice(data)
    count=0
    Next=Button(gui, text="Next", fg="blue", command=nextpress).pack(pady=20)

    Close=Button(gui, text="Close", fg="red", command=gui.destroy).pack()

    T.insert(END,Content)
    gui.mainloop()