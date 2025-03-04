import tkinter as tk
from tkinter import W, E
from tkinter.ttk import Frame, Button, Style, Entry

class Calculator(Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.initUI()

    def initUI(self):
        self.parent.title("Calculator")
        self.style = Style()
        self.style.configure("TButton", padding=(0, 5, 0, 5), font='serif 10')

        # Cấu hình lưới
        for i in range(4):
            self.columnconfigure(i, pad=3)
        for i in range(6):
            self.rowconfigure(i, pad=3)

        # Ô nhập dữ liệu
        self.entry = Entry(self)
        self.entry.grid(row=0, column=0, columnspan=4, sticky=W+E)

        # Hàng 1
        Button(self, text="Cls").grid(row=1, column=0)
        Button(self, text="Back").grid(row=1, column=1)
        Button(self).grid(row=1, column=2)  # Nút trống
        Button(self, text="Close", command=self.parent.quit).grid(row=1, column=3)

        # Hàng 2
        Button(self, text="7").grid(row=2, column=0)
        Button(self, text="8").grid(row=2, column=1)
        Button(self, text="9").grid(row=2, column=2)
        Button(self, text="/").grid(row=2, column=3)

        # Hàng 3
        Button(self, text="4").grid(row=3, column=0)
        Button(self, text="5").grid(row=3, column=1)
        Button(self, text="6").grid(row=3, column=2)
        Button(self, text="*").grid(row=3, column=3)

        # Hàng 4
        Button(self, text="1").grid(row=4, column=0)
        Button(self, text="2").grid(row=4, column=1)
        Button(self, text="3").grid(row=4, column=2)
        Button(self, text="-").grid(row=4, column=3)

        # Hàng 5
        Button(self, text="0").grid(row=5, column=0)
        Button(self, text=".").grid(row=5, column=1)
        Button(self, text="=").grid(row=5, column=2)
        Button(self, text="+").grid(row=5, column=3)

        self.pack()

if __name__ == "__main__":
    root = tk.Tk()
    app = Calculator(root)
    root.mainloop()
