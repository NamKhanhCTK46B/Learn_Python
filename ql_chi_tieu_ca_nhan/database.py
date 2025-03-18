import sqlite3
from datetime import datetime, timedelta
import random

DB_NAME = "expenses.db"

def connect_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS expenses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date TEXT,
            category TEXT,
            amount REAL,
            type TEXT
        )
    """)
    conn.commit()
    return conn

def get_all_expenses():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM expenses")
    data = cursor.fetchall()
    conn.close()
    return data

def add_expense(date, category, amount, exp_type):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO expenses (date, category, amount, type) VALUES (?, ?, ?, ?)", 
                   (date, category, amount, exp_type))
    conn.commit()
    conn.close()

def get_expenses_summary(filter_type="all"):
    conn = connect_db()
    cursor = conn.cursor()

    if filter_type == "day":
        cursor.execute("""
            SELECT date, SUM(CASE WHEN type='Thu' THEN amount ELSE 0 END) AS total_income,
                         SUM(CASE WHEN type='Chi' THEN amount ELSE 0 END) AS total_expense
            FROM expenses
            WHERE date = DATE('now')
            GROUP BY date
        """)
    elif filter_type == "week":
        cursor.execute("""
            SELECT date, SUM(CASE WHEN type='Thu' THEN amount ELSE 0 END) AS total_income,
                         SUM(CASE WHEN type='Chi' THEN amount ELSE 0 END) AS total_expense
            FROM expenses
            WHERE date >= DATE('now', '-7 days')
            GROUP BY date
        """)
    elif filter_type == "month":
        cursor.execute("""
            SELECT strftime('%Y-%m', date) AS month, 
                   SUM(CASE WHEN type='Thu' THEN amount ELSE 0 END) AS total_income,
                   SUM(CASE WHEN type='Chi' THEN amount ELSE 0 END) AS total_expense
            FROM expenses
            WHERE date >= DATE('now', '-30 days')
            GROUP BY month
        """)
    else:
        cursor.execute("""
            SELECT date, SUM(CASE WHEN type='Thu' THEN amount ELSE 0 END) AS total_income,
                         SUM(CASE WHEN type='Chi' THEN amount ELSE 0 END) AS total_expense
            FROM expenses
            GROUP BY date
        """)

    data = cursor.fetchall()
    conn.close()
    return data

def get_filtered_expenses(from_date, to_date, exp_type):
    conn = connect_db()
    cursor = conn.cursor()

    if exp_type == "Tất cả":
        cursor.execute("""
            SELECT * FROM expenses
            WHERE date BETWEEN ? AND ?
        """, (from_date, to_date))
    else:
        cursor.execute("""
            SELECT * FROM expenses
            WHERE date BETWEEN ? AND ? AND type = ?
        """, (from_date, to_date, exp_type))

    data = cursor.fetchall()
    conn.close()
    return data

def check_data_exists():
    # Kiểm tra xem có dữ liệu trong bảng chưa
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM expenses")
    count = cursor.fetchone()[0]
    conn.close()
    return count > 0

def insert_sample_data():

    if check_data_exists():
        return

    conn = connect_db()
    cursor = conn.cursor()

    categories = ["Ăn uống", "Giải trí", "Mua sắm", "Tiền điện", "Tiền nước", "Lương", "Thưởng"]
    # types = ["Chi", "Thu"]

    start_date = datetime.now() - timedelta(days=30)  # Tạo dữ liệu trong 30 ngày gần nhất

    for i in range(100):  # Tạo 100 giao dịch ngẫu nhiên
        date = start_date + timedelta(days=random.randint(0, 30))
        category = random.choice(categories)
        amount = round(random.uniform(10, 500), 2)  # Số tiền ngẫu nhiên từ 50 đến 500
        exp_type = "Thu" if category in ["Lương", "Thưởng"] else "Chi"

        cursor.execute("INSERT INTO expenses (date, category, amount, type) VALUES (?, ?, ?, ?)", 
                       (date.strftime('%Y-%m-%d'), category, amount, exp_type))

    conn.commit()
    conn.close()

# Chạy để tạo dữ liệu mẫu
insert_sample_data()
