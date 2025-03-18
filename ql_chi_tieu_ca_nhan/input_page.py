import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import DateEntry
from database import add_expense


def open_input_form(update_chart):
    input_window = tk.Toplevel()
    input_window.title("Thêm khoản thu/chi")
    input_window.geometry("350x250+600+300")

    ttk.Label(input_window, text="Ngày:").grid(row=0, column=0, padx=10, pady=10, sticky="w")
    date_entry = DateEntry(input_window, width=12, date_pattern='y-mm-dd')
    date_entry.grid(row=0, column=1, padx=10, pady=10, sticky="ew")

    ttk.Label(input_window, text="Danh mục:").grid(row=1, column=0, padx=10, pady=10, sticky="w")
    category_entry = ttk.Entry(input_window)
    category_entry.grid(row=1, column=1, padx=10, pady=10, sticky="ew")

    ttk.Label(input_window, text="Số tiền:").grid(row=2, column=0, padx=10, pady=10, sticky="w")
    amount_entry = ttk.Entry(input_window)
    amount_entry.grid(row=2, column=1, padx=10, pady=10, sticky="ew")

    ttk.Label(input_window, text="Loại:").grid(row=3, column=0, padx=10, pady=10, sticky="w")
    type_var = tk.StringVar(value="Chi")
    ttk.Radiobutton(input_window, text="Thu nhập", variable=type_var, value="Thu").grid(row=3, column=1, padx=10, pady=10, sticky="w")
    ttk.Radiobutton(input_window, text="Chi tiêu", variable=type_var, value="Chi").grid(row=3, column=2, padx=10, pady=10, sticky="w")

    def submit():
        date = date_entry.get()
        category = category_entry.get()
        amount = amount_entry.get()
        exp_type = type_var.get()

        if not category or not amount:
            messagebox.showwarning("Lỗi", "Vui lòng nhập đầy đủ thông tin!")
            return

        try:
            amount = float(amount)
            add_expense(date, category, amount, exp_type)
            messagebox.showinfo("Thành công", "Đã lưu khoản thu/chi!")
            update_chart()
            input_window.destroy()
        except ValueError:
            messagebox.showerror("Lỗi", "Số tiền phải là số hợp lệ!")

    ttk.Button(input_window, text="Thêm", command=submit).grid(row=4, column=1, pady=10, sticky="w")
    ttk.Button(input_window, text="Thoát", command=input_window.destroy).grid(row=4, column=2, pady=10, sticky="w")
