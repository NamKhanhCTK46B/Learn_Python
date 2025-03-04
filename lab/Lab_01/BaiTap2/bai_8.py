# Chương trình giải phương trình bậc 2

from math import sqrt

# Hàm tính delta của phương trình
def tinh_delta (a, b, c): 
    return b**2 - 4*a*c

def giai_phuong_trinh (a, b, c):

    delta = tinh_delta (a, b, c)

    if delta < 0:
        print (f"Phương trình {a}x^2 + {b}x + {c} = 0 vô nghiệm")
    elif delta == 0:
        x = -b / (2 * a)
        print (f"Phương trình {a}x^2 + {b}x + c = 0 có một nghiệm duy nhất: x = {x}")
    else:
        x = (-b + sqrt(delta)) / (2 * a)
        x1 = (-b - sqrt(delta)) / (2 * a)
        print (f"Phương trình {a}x^2 + {b}x + c = 0 có 2 nghiệm: x1 = {x}; x2 = {x1}")

a = int (input ("a = "))
b = int (input ("b = "))
c = int (input ("c = "))
giai_phuong_trinh (a, b, c)