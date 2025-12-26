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