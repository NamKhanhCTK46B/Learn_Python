import tkinter as tk
from tkinter.ttk import Frame, Label, Scale, Style

class ScaleApp(Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.initUI()

    def initUI(self):
        """Khởi tạo giao diện chính"""
        self.parent.title("Scale")
        self.style = Style()
        self.style.theme_use("default")

        self.pack(fill=tk.BOTH, expand=True)

        # Thanh trượt Scale
        scale = Scale(self, from_=0, to=100, command=self.onScale)
        scale.pack(side=tk.LEFT, padx=15)

        # Biến IntVar để cập nhật giá trị
        self.var = tk.IntVar()
        self.label = Label(self, textvariable=self.var)
        self.label.pack(side=tk.LEFT)

    def onScale(self, val):
        """Hàm xử lý khi thanh trượt thay đổi giá trị"""
        self.var.set(int(float(val)))

root = tk.Tk()
app = ScaleApp(root)
root.geometry("250x100+300+300")  # Đặt kích thước cửa sổ
root.mainloop()
