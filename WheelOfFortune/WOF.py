
from cProfile import label
from tkinter import *
import random
from tkinter.font import BOLD
from turtle import right

def nextpress():
    global Content
    Content = random.choice(data)
    T.delete("1.0",END)
    T.insert(END,Content)
    return

datab = open("C:\\Users\\nayan\\Documents\\Python programs\\Personal Use\\WheelOfFortune\\Database\\ListOfPrizes.txt",'r')
data = datab.readlines()
datab.close()

#Driver Code
if __name__=="__main__":

    #Configuring Main Window
    gui=Tk()
    gui.configure(background="powder blue")
    gui.title("Wheel Of F")
    gui.geometry("620x300")

    #The buttons and widgets
    l = Label(gui, text="Result", bg="powder blue", fg="navy blue")
    l.config(font=("Courier", 14, BOLD))
    l.pack(pady=30)

    T = Text(gui, bg="light green", height=5, width=52)
    T.pack()

    Content = random.choice(data)

    Next=Button(gui, text="Next", fg="blue", command=nextpress).pack(pady=20)

    Close=Button(gui, text="Close", fg="red", command=gui.destroy).pack()

    T.insert(END,Content)
    gui.mainloop()
