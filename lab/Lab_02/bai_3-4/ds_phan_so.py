from phan_so import PhanSo

class DanhSachPhanSo:

    def __init__(self):
        self.dsps = []
    
    def them_phan_so(self, ps):
        if isinstance (ps, PhanSo):
            self.dsps.append(ps)
        else:
            raise ValueError ("Đối tượng thêm vào không phải là phân số")
    
    def xuat (self):
        for ps in self.dsps:
            print(ps, end=" ")

    def dem_phan_so_am (self):
        return sum (1 for ps in self.dsps if ps.tu * ps.mau < 0 )
    
    def tim_ps_duong_nho_nhat (self):
        ps_duong = [ps for ps in self.dsps if ps.tu * ps.mau >= 0]
        return min (ps_duong)
    
    def tim_vi_tri_ps (self, x):
        vt = []

        for i in range (len (self.dsps)):
            if self.dsps[i] == x:
                vt.append (i)
        
        return vt
    
    def tong_cac_ps_am (self):
        tong = PhanSo(0)

        for ps in self.dsps:
            if ps.tu * ps.mau < 0:
                tong += ps

        return tong
    
    def xoa_ps_x (self, ps):
        self.dsps.remove(ps)

    def xoa_tat_ca_ps_theo_tu (self, x):
        self.dsps = [ps for ps in self.dsps if ps.tu != x]

    def sx_tang (self):
        self.dsps.sort()

    def sx_giam (self):
        self.dsps.sort( reverse=True)

    
ds = DanhSachPhanSo()

ds.them_phan_so (PhanSo(2, 3))
ds.them_phan_so (PhanSo(-1, 2))
ds.them_phan_so (PhanSo(1, 3))
ds.them_phan_so (PhanSo(-1, 2))

ds.sx_giam()
ds.xuat()

# tu = int (input ("Nhập tử của phân số: "))
# mau = int (input ("Nhập mẫu của phân số: "))
# ps = PhanSo (tu, mau)

# ds.xoa_ps_x(ps)
# print (f"Xoá phân số {ps} trong ds thành công")
# ds.xuat()

# ds.xoa_tat_ca_ps_theo_tu(tu)
# print (f"Xoá phân số có tử là {tu} trong ds thành công")
# ds.xuat()

# print ("Số phân số âm trong ds: ", ds.dem_phan_so_am())
# print ("Phân số dương nhỏ nhất trong ds: ", ds.tim_ps_duong_nho_nhat())
# print ("Các vị trí của phân số cần tìm trong danh sách: ", ds.tim_vi_tri_ps (ps))
# print ("Tổng các phân số âm trong danh sách: ", ds.tong_cac_ps_am())