# Chương trình tính n!

def tinh_giai_thua (n):
    
    kq = 1

    for i in range (1, n + 1):
        kq *= i
    
    return kq

n = int (input ("n = "))
print (f"{n}! = {tinh_giai_thua(n)}")