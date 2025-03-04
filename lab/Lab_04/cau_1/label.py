import tkinter as tk
from PIL import Image, ImageTk

class ImageLabelApp(tk.Frame):

    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.initUI()

    def initUI(self):
        self.parent.title("Label")

        # Mở ảnh
        self.img = Image.open("D:/university/python/images/forest.jpg")
        forest = ImageTk.PhotoImage(self.img)

        # Tạo Label chứa ảnh
        label = tk.Label(self, image=forest)
        label.image = forest  # Giữ tham chiếu để tránh bị xóa
        label.pack()

        self.pack()

    def setGeometry(self):
        """Cập nhật kích thước cửa sổ dựa trên ảnh"""
        w, h = self.img.size
        self.parent.geometry(f"{w}x{h}+300+300")


root = tk.Tk()
app = ImageLabelApp(root)
app.setGeometry()
root.mainloop()
