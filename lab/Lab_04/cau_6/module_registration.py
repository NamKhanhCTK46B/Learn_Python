import tkinter as tk
from tkinter import ttk, messagebox
import pandas as pd
import os
import re

def validate_id (id):
    return id.isdigit and len(id) == 7

def validate_phone (phone):
    return phone.isdigit() and len(phone) == 10

def validate_email (email):
    return re.match(r"[^@]+@[^@]+\.[^@]+", email) is not None

def validate_semester (semester):
    return semester in ['1', '2', '3']

def validate_dob (dob):
    return re.match (r"\d{2}/\d{2}/\d{4}", dob) is not None

def save_to_excel ():
    id = ety_id.get ()
    name = ety_name.get ()
    dob = ety_dob.get ()
    email = ety_email.get ()
    phone = ety_phone.get ()
    semester = ety_semester.get ()
    academic_year = cbo_academic_year.get ()
    course = [subject.get () for subject in checkboxes if subject.get ()]

    if not validate_id(id):
        messagebox.showerror ("Error", "Mã số sinh viên phải có 7 chữ số.")
        return
    if not name:
        messagebox.showerror ("Error", "Tên sinh viên không được để trống.")
        return
    if not validate_dob(dob):
        messagebox.showerror ("Error", "Ngày sinh phải có định dạng dd/mm/yyyy.")
        return
    if not validate_email(email):
        messagebox.showerror ("Error", "Địa chỉ email không hợp lệ.")
        return
    if not validate_phone(phone):
        messagebox.showerror ("Error", "Số điện thoại phải có 10 chữ số.")
        return
    if not validate_semester(semester):
        messagebox.showerror ("Error", "Số học kỳ phải là 1, 2 hoặc 3.")
        return
    if not academic_year:
        messagebox.showerror ("Error", "Năm học không được để trống.")
        return
    if not course:
        messagebox.showerror ("Error", "Xin hãy chọn ít nhất một môn học.")
        return
    
    file_path = "D:/university/python/lab/Lab_04/cau_6/example.xlsx"
    new_data = pd.DataFrame ([[id,name,dob,email,phone,semester,academic_year,subject] for subject in course],
                         columns=["MSSV","Họ tên","Ngày sinh","Email","Số điện thoại","Học kỳ","Năm học","Môn học"])
    
    if os.path.exists(file_path):
        existing_data = pd.read_excel (file_path)
        updated_data = pd.concat ([existing_data,new_data], ignore_index=True)
    else:
        updated_data = new_data
    
    updated_data.to_excel (file_path, index=False)
    
    messagebox.showinfo("Thành công", "Đăng ký thành công")
    root.quit ()

root = tk.Tk ()
root.title ("Đăng ký học phần")
root.geometry ("400x550+600+150")

heading = tk.Label (root, text="THÔNG TIN ĐĂNG KÝ HỌC PHẦN", 
                    font=("Arial", 16, "bold"),
                    bg="light green", fg="red", pady=10)
heading.pack (fill=tk.X)

frame_info = tk.Frame (root)
frame_info.pack (pady=10)

frame_subjects = tk.Frame (root)
frame_subjects.pack (pady=10)

frame_buttons = tk.Frame (root)
frame_buttons.pack (pady=10)

tk.Label (frame_info, text="MSSV: ").grid (row=0, column=0, sticky="e", padx=5, pady=5)
ety_id = tk.Entry (frame_info)
ety_id.grid (row=0, column=1, padx=5, pady=5)

tk.Label (frame_info, text="Họ tên: ").grid (row=1, column=0, sticky="e", padx=5, pady=5)
ety_name = tk.Entry (frame_info)
ety_name.grid (row=1, column=1, padx=5, pady=5)

tk.Label (frame_info, text="Ngày sinh: ").grid (row=2, column=0, sticky="e", padx=5, pady=5)
ety_dob = tk.Entry (frame_info)
ety_dob.grid (row=2, column=1, padx=5, pady=5)

tk.Label (frame_info, text="Email: ").grid (row=3, column=0, sticky="e", padx=5, pady=5)
ety_email = tk.Entry (frame_info)
ety_email.grid (row=3, column=1, padx=5, pady=5)

tk.Label (frame_info, text="Số điện thoại: ").grid (row=4, column=0, sticky="e", padx=5, pady=5)
ety_phone = tk.Entry (frame_info)
ety_phone.grid (row=4, column=1, padx=5, pady=5)

tk.Label (frame_info, text="Học kỳ (1-3): ").grid (row=5, column=0,sticky="e", padx=5, pady=5)
ety_semester = tk.Entry (frame_info)
ety_semester.grid (row=5, column=1, padx=5, pady=5)

tk.Label (frame_info, text="Năm học: ").grid (row=6, column=0, sticky="e", padx=5, pady=5)
n = tk.StringVar ()
cbo_academic_year = ttk.Combobox (frame_info, textvariable = n) # type: ignore
cbo_academic_year['values'] = ('2022-2023', '2023-2024', '2024-2025')
cbo_academic_year.current(0)
cbo_academic_year.grid (row=6, column=1, padx=5, pady=5)

tk.Label (frame_subjects, text="Môn học: ").grid (row=0, column=0, sticky="w", padx=5, pady=5)
subjects = ["Lập trình Python", "Công nghệ phần mềm", "Lập trình Java", "Phát triển ứng dụng web"]
checkboxes = []
for i, subject in enumerate(subjects):
    var = tk.StringVar ()
    chk = tk.Checkbutton (frame_subjects, text=subject, variable=var, onvalue=subject, offvalue="")
    chk.grid (row=i+1, column=0, sticky="w", padx=5, pady=5)
    checkboxes.append (var)

btn_submit = tk.Button (frame_buttons, text="Đăng ký", command=save_to_excel)
btn_submit.grid (row=0, column=0, padx=5, pady=5)

btn_exit = tk.Button (frame_buttons, text="Thoát", command=root.quit)
btn_exit.grid (row=0, column=1, padx=5, pady=5)

root.mainloop ()