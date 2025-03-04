import tkinter as tk
from tkinter.ttk import Frame, Label

class ListboxApp(Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.initUI()

    def initUI(self):
        """Khởi tạo giao diện chính"""
        self.parent.title("Listbox")
        self.pack(fill=tk.BOTH, expand=True)

        # Danh sách diễn viên
        acts = ["Scarlett Johansson", "Rachel Weisz", "Natalie Portman", "Jessica Alba"]

        # Listbox hiển thị danh sách
        self.lb = tk.Listbox(self)
        for name in acts:
            self.lb.insert(tk.END, name)

        # Bắt sự kiện khi chọn mục trong Listbox
        self.lb.bind("<<ListboxSelect>>", self.onSelect)
        self.lb.pack(pady=15)

        # Nhãn hiển thị giá trị đã chọn
        self.var = tk.StringVar()
        self.label = Label(self, textvariable=self.var)
        self.label.pack()

    def onSelect(self, event):
        """Xử lý khi chọn một mục trong Listbox"""
        sender = event.widget
        idx = sender.curselection()
        if idx:  # Kiểm tra xem có mục nào được chọn không
            value = sender.get(idx[0])
            self.var.set(value)

root = tk.Tk()
app = ListboxApp(root)
root.geometry("300x250+300+300")  # Đặt kích thước cửa sổ
root.mainloop()
