
from math import gcd

class PhanSo:

    def __init__(self, tu = 1, mau = 1) -> None:
        if mau == 0:
            raise ValueError("Mẫu không thể bằng 0")

        self.tu = tu
        self.mau = mau
    
    def rutGon (self):
        ucln = gcd (abs (self.tu), abs (self.mau))
        self.tu //= ucln
        self.mau //= ucln
    
    def __str__(self) -> str:
        return f"{self.tu}/{self.mau}"
    
    def tim_mau_chung (mau1, mau2):
        return mau1 * mau2 // gcd (mau1, mau2)
    
    # Ghi đè các toán tử +, - , * , / và các phép so sánh
    def __add__(self, other):
        mau_chung = PhanSo.tim_mau_chung (self.mau, other.mau)
        tu_moi = self.tu * mau_chung // self.mau + other.tu * mau_chung // other.mau

        return PhanSo (tu_moi, mau_chung)
    
    def __sub__(self, other):
        mau_chung = PhanSo.tim_mau_chung(self.mau, other.mau)
        tu_moi = self.tu * mau_chung // self.mau - other.tu * mau_chung // other.mau

        return PhanSo (tu_moi, mau_chung)
    
    def __mul__(self, other):
        tu_moi = self.tu * other.tu
        mau_moi = self.mau * other.mau

        return PhanSo (tu_moi, mau_moi)
    
    def __truediv__ (self, other):
        tu_moi = self.tu * other.mau
        mau_moi = self.mau * other.tu

        return PhanSo (tu_moi, mau_moi)
    
    # toán tử ==
    def __eq__(self, other):
        return self.tu * other.mau == self.mau * other.tu
    
    # toán tử !=
    def __ne__(self, other):
        return not self.__eq__(other)
    
    # toán tử <
    def __lt__(self, other):
        return self.tu * other.mau < self.mau * other.tu
    
    # toán tử <=
    def __le__(self, other):
        return self.__lt__(other) or self.__eq__(other)
    
    # toán tử >
    def __gt__(self, other):
        return not self <= other 
    
    # toán tử >=
    def __ge__(self, other):
        return not self < other

# a = PhanSo()
# a.tu = 2
# a.mau = 3
# b = PhanSo (3,5)

# print (f"{a} + {b} = {a + b}")