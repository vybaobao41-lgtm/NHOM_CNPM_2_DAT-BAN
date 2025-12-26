class MonAn:
    def __init__(self, ten_mon, gia, loai_mon, mo_ta="", hinh_anh="", dang_ban=True):
        self.ten_mon = ten_mon
        self.gia = gia
        self.loai_mon = loai_mon
        self.mo_ta = mo_ta
        self.hinh_anh = hinh_anh
        self.dang_ban = dang_ban

    def thong_tin(self):
        """Trả về thông tin món ăn"""
        return {
            "ten_mon": self.ten_mon,
            "gia": self.gia,
            "loai_mon": self.loai_mon,
            "mo_ta": self.mo_ta,
            "hinh_anh": self.hinh_anh
        }

# =========================
# AC-01 — HIỂN THỊ THÔNG TIN MÓN
# =========================
def lay_thong_tin_mon(mon_an):
    """
    Lấy thông tin món để hiển thị khi chỉnh sửa
    """
    return mon_an.thong_tin()

# =========================
# AC-02 — KIỂM TRA THÔNG TIN BẮT BUỘC
# =========================
def kiem_tra_thong_tin_bat_buoc(ten_mon, gia, loai_mon):
    if not ten_mon or not loai_mon or gia is None:
        return False, "⚠ Vui lòng nhập đầy đủ thông tin bắt buộc"
    return True, ""

# =========================
# AC-03 — KIỂM TRA GIÁ HỢP LỆ
# =========================
def kiem_tra_gia_hop_le(gia):
    try:
        gia = float(gia)
        if gia <= 0:
            return False, "⚠ Giá phải là số lớn hơn 0"
        return True, ""
    except ValueError:
        return False, "⚠ Giá phải là số lớn hơn 0"
    
    # =========================
# AC-04 — CẬP NHẬT MÓN THÀNH CÔNG
# =========================
def cap_nhat_mon(mon_an, ten_mon, gia, loai_mon, mo_ta="", hinh_anh=""):
    """
    Cập nhật thông tin món ăn
    """
    # Kiểm tra thông tin bắt buộc
    hop_le, thong_bao = kiem_tra_thong_tin_bat_buoc(ten_mon, gia, loai_mon)
    if not hop_le:
        return thong_bao

    # Kiểm tra giá
    hop_le, thong_bao = kiem_tra_gia_hop_le(gia)
    if not hop_le:
        return thong_bao

    # Cập nhật dữ liệu
    mon_an.ten_mon = ten_mon
    mon_an.gia = float(gia)
    mon_an.loai_mon = loai_mon
    mon_an.mo_ta = mo_ta
    mon_an.hinh_anh = hinh_anh

    return "✔ Cập nhật món thành công"
