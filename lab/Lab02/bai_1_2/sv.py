from datetime import datetime

class SinhVien:
    truong = "Đại học Đà Lạt"

    def __init__ (self, maSo: int, hoten: str, ngaySinh) -> None: 
        self.__maSo = maSo
        self.__hoTen = hoten
        self.__ngaySinh = ngaySinh

    @property
    def maSo (self):
        return self.__maSo
    
    @maSo.setter
    def maSo (self, maSo):
        if self.laMaSoHopLe (maSo):
            self.__maSo = maSo

    @staticmethod
    def laMaSoHopLe (maso: int):
        return len (str(maso) == 7)
    
    @classmethod
    def doiTenTruong (self, tenmoi):
        self.truong = tenmoi

    def __str__(self) -> str:
        return f"{self.__maSo:<10}{self.__hoTen:<30}{self.__ngaySinh.strftime('%d/%m/%Y'):<12}"
    
    def xuat (self):
        print (f"{self.__maSo:<10}{self.__hoTen:<30}{self.__ngaySinh.strftime('%d/%m/%Y'):<12}")

class DanhSachSv:

    def __init__(self) -> None:
        self.dssv = []
    
    def themSinhVien (self, sv: SinhVien):
        self.dssv.append(sv)

    def xuat(self):
        print (f"Danh sách sinh viên")
        print (f"{'Mã số':<10}{'Họ tên':<30}{'Ngày sinh':<12}")
        for sv in self.dssv:
            sv.xuat()
    
    def timSvTheoMssv (self, mssv: int):
        return [sv for sv in self.dssv if sv.mssv == mssv]
    
    def timVTSvTheoMssv (self, mssv: int):
        for i in range (len(self.dssv)):
            if self.dssv[i].mssv == mssv:
                return i
            
        return -1
    
    def xoaSvTheoMssv (self, maSo: int) -> bool:
        vt = self.timVTSvTheoMssv(maSo)
        if vt != -1:
            del self.dssv[vt]
            return True
        else:
            return False
    
    def timSvTheoTen (self, ten: str):
        return [sv for sv in self.dssv if sv.hoTen == ten]
    
    def timSvSinhTruocNgay (self, ngay):
        return [sv for sv in self.dssv.ngaySinh < ngay]
    
    def docFileTxt (self, duongDan):
        try:
            with open (duongDan, 'r', encoding='utf-8') as tapTin:
                for dong in tapTin:
                    dong = dong.strip()

                    if dong:
                        duLieu = dong.split('*')

                        if len(duLieu) == 3:
                            ma_sv, ho_ten, ngay_sinh = duLieu
                            sinh_vien = SinhVien (int(ma_sv.strip()), ho_ten, datetime.strptime(ngay_sinh,"%Y-%m-%d"))
                            self.dssv.append(sinh_vien)
        except FileNotFoundError:
            print (f"Không tìm thấy file: {duongDan}")
        except Exception as e:
            print (f"Đã xảy ra lỗi: {e}")
    
    def sxTangTheoTen (self):
        return sorted (self.dssv, key=lambda sv: sv.hoTen)
    
    def sxGiamTheoTen (self):
        return sorted (self.dssv, key=lambda sv: sv.hoTen, reverse=True)
        


ds_sinhvien = DanhSachSv()

ds_sinhvien.docFileTxt("Lab02\\bai_1_2\\ds_sinhvien.txt")
ds_sinhvien.xuat()

ds_sap_xep = DanhSachSv()
ds_sap_xep = ds_sinhvien.sxTangTheoTen
ds_sap_xep.xuat()