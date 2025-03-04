# Chuương trình tính tổng căn bậc 2 của n số nguyên đầu tiên

import math
from math import sqrt

def tinh_tong_can_bac_2 (n):

    tong = 0

    for i in range (1, n + 1):
        tong += sqrt(abs(i))

    return tong

n = int(input("Nhập số n: "))
print ("Tổng căn bậc 2 của", n , "số nguyên đầu tiên là: ", tinh_tong_can_bac_2(n))