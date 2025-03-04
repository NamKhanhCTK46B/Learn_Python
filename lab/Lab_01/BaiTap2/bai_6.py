
# Cách tính tổng của n số fibonacci dùng vòng lặp
def tinh_tong_vong_lap (n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    
    # Tạo mảng để lưu các số Fibonacci
    fib = [0, 1]

    for i in range(2, n):
        fib.append(fib[i-1] + fib[i-2])

    return sum(fib)

# Cách tính tổng của n số fibonacci dùng đệ quy
def tinh_tong_de_quy (n, a = 0, b = 1, total = 0):
    if n == 0:
        return total
    return tinh_tong_de_quy (n - 1, b, a + b, total + a)
        


# Ví dụ sử dụng hàm
n = int (input ("Nhập số n: "))
print (f"Tổng {n} số Fibonacci đầu tiên là: {tinh_tong_vong_lap(n)}")
print (f"Tổng {n} số Fibonacci đầu tiên là: {tinh_tong_de_quy(n)}")