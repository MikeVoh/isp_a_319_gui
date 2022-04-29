
from tkinter import *

def fopen():
    fname = entry.get()
    f = open(fname)
    Text.delete(1.0 , END)
    Text.insert(1.0 , f.read())

def fsave():
    fname = entry.get()
    f = open(fname, 'x')
    f.write(Text.get (1.0 ,END))
    Text.delete(1.0 , END)

root = Tk()

f1 = Frame()
f1.pack()
entry = Entry(f1 , width=20)
entry.pack(side = LEFT)
    