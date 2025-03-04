
def in_tam_giac (m, n):

    for i in range (m):
        for j in range (n):
            if j == 0 or i == j or i == m - 1:
                print('*', end=' ')
            else:
                print(' ', end=' ')
        print()

# Nhập vào số hàng và số cột
while True:
    try:
        m = int(input("Nhập số hàng (phải là số nguyên dương): "))
        n = int(input("Nhập số cột (phải là số nguyên dương): "))
        if m > 0 and n > 0:
            break
        else:
            print("Vui lòng nhập số nguyên dương.")
    except ValueError:
        print("Vui lòng nhập số nguyên hợp lệ.")

in_tam_giac(m, n)
