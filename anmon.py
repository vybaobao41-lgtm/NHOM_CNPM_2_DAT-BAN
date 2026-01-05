# =========================
# MÔ HÌNH MÓN ĂN
# =========================
class MonAn:
    def __init__(self, ten, gia, loai):
        self.ten = ten
        self.gia = gia
        self.loai = loai
        self.dang_ban = True  # True = còn hàng, False = hết hàng (ẩn)

    def an_mon(self):
        self.dang_ban = False

    def hien_thi(self):
        if self.dang_ban:
            print(f"{self.ten} - {self.gia}đ ({self.loai})")


# =========================
# DANH SÁCH THỰC ĐƠN (AC-01)
# =========================
thuc_don = [
    MonAn("Cơm gà", 35000, "Món chính"),
    MonAn("Bún bò", 40000, "Món chính"),
    MonAn("Phở bò", 45000, "Món chính"),
    MonAn("Trà đá", 5000, "Nước uống"),
    MonAn("Trà đào", 25000, "Nước uống"),
]


# =========================
# AC-01: PHÁT HIỆN MÓN HẾT HÀNG
# =========================
def tim_mon(ten_mon):
    for mon in thuc_don:
        if mon.ten.lower() == ten_mon.lower():
            return mon
    return None
