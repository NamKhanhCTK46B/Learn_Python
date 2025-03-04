from tkinter import Tk, Frame, Button, BOTH, SUNKEN
from tkinter.colorchooser import askcolor

class Example(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)

        self.parent = parent
        self.initUI()

    def initUI(self):
        self.parent.title("Color Chooser")
        self.pack(fill=BOTH, expand=True)

        self.btn = Button(self, text="Choose Color", command=self.onChoose)
        self.btn.grid(row=0, column=0, padx=20, pady=20)

        self.frame = Frame(self, border=1, relief=SUNKEN, width=100, height=100)
        self.frame.grid(row=0, column=1, padx=20, pady=20)

    def onChoose(self):
        color = askcolor()
        if color[1]:  # Kiểm tra nếu có màu được chọn
            self.frame.config(bg=color[1])

root = Tk()
root.geometry("300x150+600+300")
app = Example(root)
root.mainloop()
