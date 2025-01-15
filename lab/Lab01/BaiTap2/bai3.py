import math

# Kiểm tra 1 số có phải số nguyên tố không
def kiem_tra_nguyen_to (x):

    if x < 2:
        return False
    
    for i in range (2, int (math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    
    return True

# Tìm kiếm danh sách các số nguyên tố trong khoảng [a, b]
def so_nguyen_to_trong_khoang (a, b):

    kq = []

    for i in range (a, b + 1):
        if kiem_tra_nguyen_to (i):
            kq.append(i)
    
    return kq

a = int (input ("Nhập giá trị bắt đầu cảu khoảng (a): "))
b = int (input ("Nhập giá trị kết thúc của khoảng (b): "))

danh_sach = so_nguyen_to_trong_khoang (a, b)

print (f"Các số nguyên trong khoảng [{a}, {b}] là: ")
print (*danh_sach)