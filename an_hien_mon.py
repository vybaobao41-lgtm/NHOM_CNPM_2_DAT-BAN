# -------------------------
# CLASS MÓN ĂN
# -------------------------
class MonAn:
    def __init__(self, ten_mon, gia, loai_mon, dang_ban=True):
        self.ten_mon = ten_mon      # Tên món
        self.gia = gia              # Giá món
        self.loai_mon = loai_mon    # Loại món (Món chính, Đồ uống...)
        self.dang_ban = dang_ban    # True = đang bán, False = ngừng bán

    def trang_thai(self):
        """Trả về trạng thái món ăn"""
        return "Đang bán" if self.dang_ban else "Ngừng bán"
    
# -------------------------
# AC-01 — ẨN MÓN
# -------------------------
def an_mon(mon_an):
    """
    Ẩn món: đổi trạng thái sang Ngừng bán
    AC-03 cũng được đảm bảo vì không xóa dữ liệu
    """
    if not mon_an.dang_ban:
        return "⚠ Món đã ngừng bán"
    mon_an.dang_ban = False
    return f"✔ Ẩn món '{mon_an.ten_mon}' thành công"

# -------------------------
# AC-02 — HIỆN MÓN
# -------------------------
def hien_mon(mon_an):
    """Hiện món: đổi trạng thái sang Đang bán"""
    if mon_an.dang_ban:
        return "⚠ Món đang được bán"
    mon_an.dang_ban = True
    return f"✔ Hiện món '{mon_an.ten_mon}' thành công"

# AC-03 — KHÔNG XÓA DỮ LIỆU KHI ẨN
# Logic đã đảm bảo trong an_mon/hien_mon

# -------------------------
# AC-04 — HIỂN THỊ DANH SÁCH MÓN
# -------------------------
def hien_thi_danh_sach(danh_sach_mon):
    """Hiển thị danh sách món ăn kèm trạng thái"""
    print("\nDANH SÁCH THỰC ĐƠN")
    for i, mon in enumerate(danh_sach_mon, start=1):
        print(f"{i}. {mon.ten_mon} | {mon.gia} | {mon.loai_mon} | {mon.trang_thai()}")

        # -------------------------
# HÀM DÙNG CHUNG CHO US KHÁC
# -------------------------
def lay_mon_dang_ban(danh_sach_mon):
    """Trả về danh sách món đang bán, dùng cho gọi món / order"""
    return [mon for mon in danh_sach_mon if mon.dang_ban]


# -------------------------
# HÀM NHẬP SỐ AN TOÀN
# -------------------------
def nhap_so(prompt):
    while True:
        val = input(prompt)
        try:
            val_float = float(val)
            if val_float <= 0:
                print("⚠ Giá phải lớn hơn 0")
                continue
            return val_float
        except ValueError:
            print("⚠ Nhập số hợp lệ")

# -------------------------
# NHẬP MÓN TỪ BÀN PHÍM
# -------------------------
def nhap_mon_tu_ban_phim():
    ten = input("Nhập tên món: ")
    gia = nhap_so("Nhập giá món: ")
    loai = input("Nhập loại món: ")
    return MonAn(ten, gia, loai)

def chon_mon_tu_danh_sach(danh_sach_mon):
    hien_thi_danh_sach(danh_sach_mon)
    if not danh_sach_mon:
        return None
    while True:
        try:
            idx = int(input("Chọn số món: "))
            if 1 <= idx <= len(danh_sach_mon):
                return danh_sach_mon[idx - 1]
            print("⚠ Số món không hợp lệ")
        except ValueError:
            print("⚠ Nhập số nguyên hợp lệ")

# -------------------------
# DEMO CHẠY AN TOÀN
# -------------------------
if __name__ == "__main__":
    ds_mon = []

    so_luong = 2
    for _ in range(so_luong):
        print("\n--- Thêm món mới ---")
        ds_mon.append(nhap_mon_tu_ban_phim())

    print("\n--- Ẩn món ---")
    mon = chon_mon_tu_danh_sach(ds_mon)
    if mon:
        print(an_mon(mon))

    print("\n--- Hiện món ---")
    mon = chon_mon_tu_danh_sach(ds_mon)
    if mon:
        print(hien_mon(mon))

    hien_thi_danh_sach(ds_mon)