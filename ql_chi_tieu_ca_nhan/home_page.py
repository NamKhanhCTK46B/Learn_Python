import tkinter as tk
import database as db
from tkinter import ttk
from tkcalendar import DateEntry
from chart_view import create_chart
from input_page import open_input_form


def home_page():
    
    root = tk.Tk()
    root.title("Quản lý chi tiêu cá nhân")
    root.state("zoomed")  # Fullscreen

    # Main layout
    root.columnconfigure(0, weight=1)
    root.columnconfigure(1, weight=2)
    root.rowconfigure(0, weight=1)

    # Left frame for chart and filters
    left_frame = tk.Frame(root, padx=10, pady=10)
    left_frame.grid(row=0, column=0, sticky="nsew")
    update_chart = create_chart(left_frame)

    # Right frame for Treeview and controls
    right_frame = tk.Frame(root, padx=10, pady=10)
    right_frame.grid(row=0, column=1, sticky="nsew")

    # Filters above Treeview
    filter_frame = tk.Frame(right_frame)
    filter_frame.pack(fill="x", pady=5)

    ttk.Label(filter_frame, text="Từ ngày:").grid(row=0, column=0, padx=5, pady=5, sticky="w")
    from_date = DateEntry(filter_frame, width=12, date_pattern="y-mm-dd")
    from_date.grid(row=0, column=1, padx=5, pady=5, sticky="ew")

    ttk.Label(filter_frame, text="Đến ngày:").grid(row=0, column=2, padx=5, pady=5, sticky="w")
    to_date = DateEntry(filter_frame, width=12, date_pattern="y-mm-dd")
    to_date.grid(row=0, column=3, padx=5, pady=5, sticky="ew")

    ttk.Label(filter_frame, text="Loại:").grid(row=0, column=4, padx=5, pady=5, sticky="w")
    type_filter = ttk.Combobox(filter_frame, values=["Tất cả", "Thu", "Chi"], state="readonly")
    type_filter.set("Tất cả")
    type_filter.grid(row=0, column=5, padx=5, pady=5, sticky="ew")

    # Add search button
    ttk.Button(filter_frame, text="Tìm kiếm", command=lambda: search_expenses()).grid(row=0, column=6, padx=5, pady=5, sticky="ew")

    # Treeview for displaying expenses
    tree = ttk.Treeview(right_frame, columns=("date", "category", "amount", "type"), show="headings")
    tree.heading("date", text="Ngày")
    tree.heading("category", text="Danh mục")
    tree.heading("amount", text="Số tiền")
    tree.heading("type", text="Loại")
    tree.pack(fill="both", expand=True, pady=5)

    # Buttons below Treeview
    button_frame = tk.Frame(right_frame)
    button_frame.pack(fill="x", pady=5)

    ttk.Button(button_frame, text="Thêm khoản thu/chi", command=lambda: open_input_form(update_chart, display_expenses)).pack(side="left", padx=5)
    ttk.Button(button_frame, text="Tải lại danh sách", command=lambda: display_expenses(db.get_all_expenses())).pack(side="left", padx=5)

    def search_expenses():
        from_date_value = from_date.get_date().strftime("%Y-%m-%d")
        to_date_value = to_date.get_date().strftime("%Y-%m-%d")
        selected_type = type_filter.get()

        # Fetch filtered data from the database
        filtered_expenses = db.get_filtered_expenses(from_date_value, to_date_value, selected_type)
        display_expenses(filtered_expenses)

    def display_expenses(expenses_list):
        # Sort expenses by date in ascending order
        sorted_expenses = sorted(expenses_list, key=lambda x: x[1])  # Assuming x[1] is the date field
        tree.delete(*tree.get_children())

        for expense in sorted_expenses:
            formatted_amount = f"{expense[3] * 1000:,.0f}"  # Format amount as 10,000
            format_row = (expense[1], expense[2], formatted_amount, expense[4])
            tree.insert("", "end", values=format_row)

    # Load all data initially
    expenses = db.get_all_expenses()
    display_expenses(expenses)

    root.mainloop()
