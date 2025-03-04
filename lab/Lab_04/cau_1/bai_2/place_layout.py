from PIL import Image, ImageTk
from tkinter import Frame, Tk, Label, BOTH
from tkinter.ttk import Style
import os

class Example (Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent)

        self.parent = parent
        self.intiUI()
    
    def intiUI (self): 
        self.parent.title("Absolute positioning")
        self.pack (fill=BOTH, expand=1)

        Style().configure ("TFrame", background="#333")

        brad = Image.open ("D:/university/python/images/bardejov.jpg")
        brad = brad.resize ( (100, 100) )
        bradjov = ImageTk.PhotoImage (brad)
        lable1 = Label (self, image=bradjov)
        lable1.image = bradjov
        lable1.place (x=20, y=20)

        rot = Image.open ("D:/university/python/images/rotunda.jpg")
        rot = rot.resize ( (100, 100) )
        rotunda = ImageTk.PhotoImage (rot)
        lable2 = Label (self, image=rotunda)
        lable2.image = rotunda
        lable2.place (x=40, y=160)

        minc = Image.open ("D:/university/python/images/mincol.jpg")
        minc = minc.resize ( (100, 100) )
        mincol = ImageTk.PhotoImage (minc)
        lable3 = Label (self, image=mincol)
        lable3.image = mincol
        lable3.place (x=170, y=50)

root = Tk()
root.geometry("300x280+650+300")
app = Example(root)
root.mainloop()