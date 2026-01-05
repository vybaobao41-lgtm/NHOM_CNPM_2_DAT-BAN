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
# =========================
# AC-02 + AC-03: ẨN MÓN & LƯU TRẠNG THÁI
# =========================
def an_mon_khi_het_hang():
    ten_mon = input("Nhập tên món đã hết hàng: ").strip()
    mon = tim_mon(ten_mon)

    if not mon:
        print("❌ Món không tồn tại!")
        return

    if not mon.dang_ban:
        print("⚠ Món đã được ẩn trước đó!")
        return

    mon.an_mon()
    print(f"✔ Đã ẩn món '{mon.ten}' (Hết hàng)")
    # =========================
# AC-04: HIỂN THỊ THEO VAI TRÒ
# =========================
def hien_thi_cho_phuc_vu():
    print("\n--- THỰC ĐƠN PHỤC VỤ ---")
    for mon in thuc_don:
        mon.hien_thi()


def hien_thi_cho_bep():
    print("\n--- QUẢN LÝ THỰC ĐƠN (BẾP) ---")
    for mon in thuc_don:
        trang_thai = "Còn hàng" if mon.dang_ban else "Hết hàng"
        print(f"{mon.ten} - {trang_thai}")


# =========================
# MENU TEST
# =========================
def menu():
    while True:
        print("\n===== US: ẨN MÓN KHI HẾT HÀNG =====")
        print("1. Bếp: Ẩn món hết hàng")
        print("2. Phục vụ: Xem thực đơn")
        print("3. Bếp: Xem danh sách quản lý món")
        print("0. Thoát")

        chon = input("Chọn chức năng: ").strip()

        if chon == "1":
            an_mon_khi_het_hang()
        elif chon == "2":
            hien_thi_cho_phuc_vu()
        elif chon == "3":
            hien_thi_cho_bep()
        elif chon == "0":
            print("👋 Thoát chương trình")
            break
        else:
            print("❌ Lựa chọn không hợp lệ!")


if __name__ == "__main__":
    menu()