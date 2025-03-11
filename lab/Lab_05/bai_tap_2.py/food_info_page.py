import tkinter as tk
from tkinter import ttk, messagebox
import db_connect as dbc

class FoodForm(tk.Toplevel):
    def __init__(self, parent, mode, food_id=None, callback=None):
        super().__init__(parent)
        self.mode = mode
        self.food_id = food_id
        self.callback = callback

        self.food_types = dbc.get_all_food_types()

        self.title("Thông tin món ăn")
        self.geometry("300x220+600+300")

        self.create_widgets()

        if self.mode == "edit" and self.food_id:
            self.load_food_info()

    def create_widgets(self):
        self.lbl_name = tk.Label(self, text="Tên món ăn")
        self.lbl_name.grid(row=0, column=0, padx=10, pady=10, sticky=tk.E)
        self.txt_name = tk.Entry(self)
        self.txt_name.grid(row=0, column=1, padx=10, pady=10, sticky=tk.W)

        self.lbl_unit = tk.Label(self, text="Đơn vị tính")
        self.lbl_unit.grid(row=1, column=0, padx=10, pady=10, sticky=tk.E)
        self.txt_unit = tk.Entry(self)
        self.txt_unit.grid(row=1, column=1, padx=10, pady=10, sticky=tk.W)

        self.lbl_price = tk.Label(self, text="Đơn giá")
        self.lbl_price.grid(row=2, column=0, padx=10, pady=10, sticky=tk.E)
        self.txt_price = tk.Entry(self)
        self.txt_price.grid(row=2, column=1, padx=10, pady=10, sticky=tk.W)

        self.lbl_food_type = tk.Label(self, text="Nhóm")
        self.lbl_food_type.grid(row=3, column=0, padx=10, pady=10, sticky=tk.E)
        self.cbo_food_type = ttk.Combobox(self, values=[row[1] for row in self.food_types])
        self.cbo_food_type.grid(row=3, column=1, padx=10, pady=10, sticky=tk.W)

        self.btn_save = tk.Button(self, text="Lưu", command=self.save_food)
        self.btn_save.grid(row=4, column=0, columnspan=2, pady=10)
        self.btn_exit = tk.Button(self, text="Thoát", command=self.destroy)
        self.btn_exit.grid(row=4, column=1, columnspan=2, pady=10)

    def load_food_info(self):
        food = dbc.get_food_by_id(self.food_id)
        if food:
            self.txt_name.insert(0, food[1])
            self.txt_unit.insert(0, food[2])
            self.txt_price.insert(0, food[3])

            food_type_id = food[4]

            food_type = next ((row[1] for row in self.food_types if row[0] == food_type_id), None)

            # Set the food type in the combobox
            if food_type in self.cbo_food_type['values']:
                index = self.cbo_food_type['values'].index(food_type)
                self.cbo_food_type.current(index)

    def save_food(self):
        ten = self.txt_name.get()
        dvt = self.txt_unit.get()
        gia = self.txt_price.get()
        nhom = self.cbo_food_type.current() + 1

        if self.mode == "add":
            success = dbc.add_update_delete_food(None, ten, dvt, gia, nhom, 0)
        elif self.mode == "edit":
            success = dbc.add_update_delete_food(self.food_id, ten, dvt, gia, nhom, 1)

        if success:
            messagebox.showinfo("Thông báo", "Lưu món ăn thành công")
            if self.callback:
                self.callback()
            self.destroy()
        else:
            messagebox.showerror("Thông báo", "Lưu món ăn thất bại")
