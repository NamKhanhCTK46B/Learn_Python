import tkinter as tk
from tkinter import BooleanVar

class CheckButtonApp(tk.Frame):
    
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.initUI()

    def initUI(self):
        self.parent.title("Checkbutton")
        self.pack(fill=tk.BOTH, expand=True)

        # Biến Boolean để kiểm soát trạng thái của checkbox
        self.var = BooleanVar()

        # Tạo Checkbutton
        cb = tk.Checkbutton(self, text="Show Title", variable=self.var, command=self.onClick)
        cb.select()  # Mặc định được chọn
        cb.place(x=50, y=50)

    def onClick(self):
        """Hàm xử lý khi checkbox được click"""
        if self.var.get():
            self.parent.title("Checkbutton")  # Hiển thị tiêu đề
        else:
            self.parent.title("")  # Xóa tiêu đề

root = tk.Tk()
root.geometry("250x150+650+300")  # Kích thước cửa sổ
app = CheckButtonApp(root)
root.mainloop()