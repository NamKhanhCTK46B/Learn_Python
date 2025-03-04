
def doi_giay (so_giay):
    
    gio = so_giay // 3600 
    phut = (so_giay % 3600) // 60
    giay = so_giay % 60

    return f"{gio:02}:{phut:02}:{giay:02}"

so_giay = int (input ("Nhập số giây:"))
print (doi_giay(so_giay))  # In ra thời gian đã chuyển đổi