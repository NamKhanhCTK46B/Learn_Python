def cong (a, b):
    return a + b

def chia (a, b):
    return a / b

def luy_thua (a, b):
    return a ** b

a = int (input("a = "))
b = int (input("b = "))

print (f"{a} + {b} = {cong(a, b)}")
print (f"{a} / {b} = {chia(a, b)}")
print (f"{a}^{b} = {luy_thua(a, b)}")