from tkinter import Frame, Tk, BOTH, Text, Menu, END
from tkinter.filedialog import askopenfilename

class Example(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.initUI()

    def initUI(self):
        self.parent.title("File Dialog")
        self.pack(fill=BOTH, expand=True)

        menubar = Menu(self.parent)
        self.parent.config(menu=menubar)

        fileMenu = Menu(menubar, tearoff=0)
        fileMenu.add_command(label="Open", command=self.onOpen)
        menubar.add_cascade(label="File", menu=fileMenu)

        self.txt = Text(self)
        self.txt.pack(fill=BOTH, expand=True)

    def onOpen(self):
        ftypes = [('Python files', '*.py'), ('All files', '*')]
        filename = askopenfilename(filetypes=ftypes)
        if filename:
            text = self.readFile(filename)
            self.txt.delete(1.0, END)  # Xóa nội dung cũ trước khi chèn mới
            self.txt.insert(END, text)

    def readFile(self, filename):
        with open(filename, "r", encoding="utf-8") as f:
            return f.read()

root = Tk()
root.geometry("400x300+300+300")
app = Example(root)
root.mainloop()
