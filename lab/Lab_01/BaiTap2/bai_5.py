
# Tìm số fibonacci thứ n dùng đệ quy
def fibonacci_de_quy (n):
    if n <= 0:
        return "Không hợp lệ"
    if n == 1:
        return 0
    if n == 2:
        return 1
    
    return fibonacci_de_quy(n - 1) + fibonacci_de_quy (n - 2)

#Tìm số fibonacci thứ n dùng vòng lặp
def fibonacci_vong_lap (n):
    if n <= 0:
        return "Không hợp lệ"
    if n == 1:
        return 0
    if n == 2:
        return 1
    
    a, b = 0, 1
    for _ in range (2, n):
        c = a
        a = b
        b = c + b
    
    return b

n = int (input (" n = "))
print (f"Số fibonacci thứ {n} là:", fibonacci_de_quy(n))
print (f"Số fibonacci thứ {n} là:", fibonacci_vong_lap(n))