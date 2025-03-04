import tkinter as tk

root = tk.Tk();

root.geometry("250x100+600+300")

name_var = tk.StringVar()
passw_var = tk.StringVar()

def submit ():
    name =name_var.get()
    password = passw_var.get()

    print ("The name is: " + name)
    print ("The password is: " + password)

    name_var.set ("")
    passw_var.set ("")

name_label = tk.Label (root, text="Username", font=('Times New Roman', 12, 'bold'))
name_entry = tk.Entry (root, textvariable=name_var, font=('Times New Roman', 12, 'normal'))

passr_lable = tk.Label (root, text='Password', font=('Times New Roman', 12, 'bold'))
passr_entry = tk.Entry (root, textvariable=passw_var, font=('Times New Roman', 12, 'normal'))

sub_btn = tk.Button (root, text= 'Submit', command=submit (), font=('Times New Roman', 12, 'bold'))

name_label.grid (row=0, column=0)
name_entry.grid (row=0, column=1)
passr_lable.grid (row=1, column=0)
passr_entry.grid (row=1, column=1)
sub_btn.grid (row=2, column=1)

root.mainloop()