
from math import sqrt

# --------------------------------------------------------------------

mang = [1, 5, 7, 9, 10, 15, 17, 25, 30, 33]

# --------------------------------------------------------------------

# a) Xuất tất cả các số lẻ không chia hết cho 5
def xuat_so_le_khong_chia_het_5_c1 (arr):
    return [x for x in mang if x % 2 != 0 and x % 5 != 0]

def xuat_so_le_khong_chia_het_5_c2 (arr):
    return list (filter (lambda x: x % 2 != 0 and x % 5 != 0, arr))

# print (xuat_so_le_khong_chia_het_5_c1 (mang))
# print (xuat_so_le_khong_chia_het_5_c2 (mang))

# --------------------------------------------------------------------

# b) Xuất tất cả các số fibonacci
    # Cách 1
def kiem_tra_chinh_phuong (x):
    s = int (sqrt (x))
    return s * s == x

def kiem_tra_fibonacci (n):
    return kiem_tra_chinh_phuong (5 * n**2 + 4) or kiem_tra_chinh_phuong (5 * n**2 - 4)

def xuat_tat_ca_so_fibonacci_c1 (arr):
    return [x for x in mang if kiem_tra_fibonacci (x)]

    # Cách 2
def tao_mang_so_fibo (n):
    fib = [0, 1]

    while fib[-1] <= n:
        fib.append(fib[-1] + fib[-2])
    
    return fib

def xuat_tat_ca_so_fibonacci_c2 (arr):
    fib = tao_mang_so_fibo (max (arr))
    return [x for x in arr if x in fib]

# print (xuat_tat_ca_so_fibonacci_c1 (mang))
# print (xuat_tat_ca_so_fibonacci_c2 (mang))

# --------------------------------------------------------------------

# c) Tìm số nguyên tố lớn nhất
    # Cách 1
def kiem_tra_so_nguyen_to (n):
    if n < 2:
        return False
    
    for i in range (2, int (sqrt (n)) + 1):
        if n % i == 0:
            return False
    
    return True

def tim_so_nguyen_to_lon_nhat_c1 (arr):
    return max ([x for x in arr if kiem_tra_so_nguyen_to (x)])

    # Cách 2
def tim_so_nguyen_to_lon_nhat_c2 (arr):
    #Sắp xếp mảng theo thứ tự giảm dần
    arr.sort (reverse = True)
    for i in arr:
        if kiem_tra_so_nguyen_to (i):
            return i
    
    return None

# print ("Số nguyên tố lớn nhất trong mảng là:", tim_so_nguyen_to_lon_nhat_c1 (mang))
# print ("Số nguyên tố lớn nhất trong mảng là:", tim_so_nguyen_to_lon_nhat_c2 (mang))

# --------------------------------------------------------------------

# d) Tìm số fibonacci bé nhất

def tim_so_fibo_nho_nhat (arr):
    fib = [x for x in arr if kiem_tra_fibonacci (x)]
    return min (fib) if fib else None

print ("Số fibonacci nhỏ nhất trong mảng là:", tim_so_fibo_nho_nhat (mang))