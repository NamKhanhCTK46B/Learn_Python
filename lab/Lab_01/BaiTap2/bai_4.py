
''' 
        Xác định số fibonacci
    Số n là số Fibonacic nếu và chỉ nếu một trong hai biểu thức dưới là số chính phương 
    5(n^2) + 4 hoặc 5(n^2) - 4
'''

import math

def kiem_tra_chinh_phuong (x):
    s = int (math.sqrt(x))
    return s * s == x

def kiem_tra_fibonacci (n):
    return kiem_tra_chinh_phuong (5 * n ** 2 + 4 ) or kiem_tra_chinh_phuong (5 * n ** 2 - 4)

n = int (input ("Nhập số cần kiểm tra: "))

if kiem_tra_fibonacci (n):
    print (f" {n} là số fibonacci")
else:
    print (f"{n} không phải là số fibonacci")