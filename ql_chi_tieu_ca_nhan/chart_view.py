import tkinter as tk
from database import get_expenses_summary
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np

def create_chart(frame):
    fig, ax = plt.subplots(figsize=(10, 6))
    canvas = FigureCanvasTkAgg(fig, master=frame)
    canvas.get_tk_widget().grid(row=0, column=0, sticky="nsew")

    def update_chart(filter_type="all"):
        data = get_expenses_summary(filter_type)

        if not data:
            ax.text(0.5, 0.5, "Không có dữ liệu", fontsize=14, ha="center", va="center", transform=ax.transAxes)
            canvas.draw()
            return


        # if filter_type == "month":
        labels = [row[0] for row in data]
        # else:
        #     labels = [row[0] for row in data]
        incomes = [row[1] for row in data]
        expenses = [row[2] for row in data]

        ax.clear()

        x = np.arange(len(labels)) # Tạo vị trí cột trên trục x
        width = 0.4 

        ax.bar(x - width/4, incomes, width=width/2, label="Thu nhập", color="#00b1f0", alpha=0.7)
        ax.bar(x + width/4, expenses, width=width/2, label="Chi tiêu", color="#89dcf6", alpha=0.7)

        ax.set_title("Thống kê thu/chi (Đơn vị: nghìn đồng)", fontsize=14, pad=20)
        ax.set_xlabel("Thời gian", fontsize=12)
        ax.set_ylabel("Số tiền", fontsize=12)
        ax.set_xticks(x)
        ax.set_xticklabels(labels, rotation=45, ha="right")

        ax.legend()
        
        canvas.draw()

    # Khung chọn bộ lọc
    filter_frame = tk.Frame(frame)
    filter_frame.grid(row=1, column=0, sticky="ew")

    # tk.Button(filter_frame, text="Ngày", command=lambda: update_chart("day")).grid(row=0, column=0, padx=5, pady=5, sticky="ew")
    # tk.Button(filter_frame, text="Tuần", command=lambda: update_chart("week")).grid(row=0, column=1, padx=5, pady=5, sticky="ew")
    # tk.Button(filter_frame, text="Tháng", command=lambda: update_chart("month")).grid(row=0, column=2, padx=5, pady=5, sticky="ew")
    # tk.Button(filter_frame, text="Tất cả", command=lambda: update_chart("all")).grid(row=0, column=3, padx=5, pady=5, sticky="ew")

    filters = [("Ngày", "day"), ("Tuần", "week"), ("Tháng", "month"), ("Tất cả", "all")]
    for i, (text, f_type) in enumerate(filters):
        tk.Button(filter_frame, text=text, command=lambda ft=f_type: update_chart(ft)).grid(row=0, column=i, padx=5, pady=5, sticky="ew")

    frame.grid_rowconfigure(0, weight=1)
    frame.grid_columnconfigure(0, weight=1)
    filter_frame.grid_columnconfigure(0, weight=1)
    filter_frame.grid_columnconfigure(1, weight=1)
    filter_frame.grid_columnconfigure(2, weight=1)
    filter_frame.grid_columnconfigure(3, weight=1)

    update_chart()
    return update_chart
