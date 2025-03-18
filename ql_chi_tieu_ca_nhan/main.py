import tkinter as tk
from tkinter import ttk
from input_page import open_input_form
from chart_view import create_chart

root = tk.Tk()
root.title("Quản lý chi tiêu cá nhân")
root.state("zoomed")

# Adjust padding and layout
frame_chart = ttk.Frame(root, padding=(20, 10))
frame_chart.grid(row=0, column=1, sticky="nsew", padx=(10, 20), pady=10)

frame_buttons = ttk.Frame(root, padding=(20, 10))
frame_buttons.grid(row=0, column=0, sticky="nsew", padx=(20, 10), pady=10)

update_chart = create_chart(frame_chart)

ttk.Button(frame_buttons, text="Thêm khoản thu/chi", command=lambda: open_input_form(update_chart), width=30).pack(pady=10)

root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=4)

root.mainloop()