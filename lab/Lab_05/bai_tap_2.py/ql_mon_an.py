import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import db_connect as dbc
from food_info_page import FoodForm

food_types = dbc.get_all_food_types()
foods = dbc.get_all_food()

def display_foods(food_list):
    tv_food.delete(*tv_food.get_children())
    food_types_dirct = {row[0]: row[1] for row in food_types}

    for food in food_list:
        group_name = food_types_dirct.get(food[4], 'Unknown')
        format_row = (food[0], food[1], food[2], f'{food[3]}', group_name)
        tv_food.insert("", "end", values=format_row)

def on_food_type_selected(event):
    selected_index = cbo_food_type.current()

    if selected_index >= 0:
        ma_nhom = food_types[selected_index][0]
        foods = dbc.get_food_by_type(ma_nhom)
        display_foods(foods)

def delete_food():
    selected_food = tv_food.selection()
    if not selected_food:
        messagebox.showerror("Thông báo", "Vui lòng chọn một món ăn để xóa")
        return
    
    confirm = messagebox.askyesno("Xác nhận", "Bạn có chắc chắn muốn xóa món ăn này không?")
    if confirm:
        food_id = tv_food.item(selected_food, "values")[0]
        success = dbc.add_update_delete_food(food_id, None, None, None, None, 2)

        if success:
            messagebox.showinfo("Thông báo", "Đã xóa món ăn thành công")
            foods = dbc.get_all_food()
            display_foods(foods)

def show_popup_menu(event):
    selected_food = tv_food.identify_row(event.y)
    tv_food.selection_set(selected_food)
    popup_menu.post(event.x_root, event.y_root)

def edit_food():
    selected_food = tv_food.selection()
    if selected_food:
        food_id = tv_food.item(selected_food, "values")[0]
        FoodForm(root, "edit", food_id, callback=refresh_food_list)
    else:
        messagebox.showerror("Thông báo", "Vui lòng chọn một món ăn để sửa")

def refresh_food_list():
    foods = dbc.get_all_food()
    display_foods(foods)

# tạo giao diện
root = tk.Tk()
root.title("Quản lý món ăn")
root.geometry("575x325+500+200")

frame = ttk.Frame(root)
frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

lbl_food_group = tk.Label(frame, text="Chọn nhóm món ăn")
lbl_food_group.grid(row=0, column=0, padx=5, pady=5, sticky=tk.E)

cbo_food_type = ttk.Combobox(frame)
cbo_food_type['values'] = [row[1] for row in food_types]
cbo_food_type.grid(row=0, column=1, padx=5, pady=5, sticky=tk.W)
cbo_food_type.bind("<<ComboboxSelected>>", on_food_type_selected)

columns = ("Mã món ăn", "Tên món ăn", "Đơn vị tính", "Đơn giá", "Nhóm")
tv_food = ttk.Treeview(frame, columns=columns, show="headings")

for col in columns:
    tv_food.heading(col, text=col)

tv_food.column("Mã món ăn", width=100, anchor="center")
tv_food.column("Tên món ăn", width=150)
tv_food.column("Đơn vị tính", width=100, anchor="center")
tv_food.column("Đơn giá", width=100, anchor="e")
tv_food.column("Nhóm", width=125, anchor="center")

tv_food.grid(row=1, column=0, columnspan=2, sticky=tk.NSEW, pady=10)

popup_menu = tk.Menu(root, tearoff=0)
popup_menu.add_command(label="Thêm món ăn", command=lambda: FoodForm(root, "add", callback=refresh_food_list))
popup_menu.add_command(label="Sửa món ăn", command=edit_food)
popup_menu.add_command(label="Xóa món ăn", command=delete_food)

tv_food.bind("<Button-3>", show_popup_menu)

display_foods(foods)

root.mainloop()