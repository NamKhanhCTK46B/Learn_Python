import math

# Tính diện tích hình chữ nhật có đường tròn nội tiếp: dài + rộng = 2r (dài = rộng)
def tinh_dien_tich_hcn (r):
    dai = r
    rong = r
    dien_tich = dai * rong
    return dien_tich

# Tính diện tích hình chữ nhật có đường tròn ngoại tiếp: dài^2 + rộng^2 = (2r)^2
def tinh_dien_tich_hcn_1 (r, tl):
    duong_cheo = 2 * r
    rong_binh_phuong = duong_cheo**2 / (1 + tl**2)
    rong = math.sqrt(rong_binh_phuong)
    dai = tl * rong
    dien_tich = dai * rong

    return dai, rong, dien_tich

r = float (input ("Nhập bán kính: "))
tl = float(input("Nhập tỉ lệ giữa chiều dài và chiều rộng (dài/rộng): "))

dien_tich = tinh_dien_tich_hcn(r)
print(f"Diện tích hình chữ nhật (đường tròn nội tiếp): {dien_tich}")

dai, rong, dien_tich = tinh_dien_tich_hcn_1(r, tl)
print(f"Diện tích hình chữ nhật (đường tròn ngoại tiếp) có chiều dài {dai:.2f}, chiều rộng {rong:.2f}: {dien_tich:.2f}")