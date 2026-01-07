# =========================
# MODEL MÓN ĂN
# =========================
class MonAn:
    def __init__(self, ten, gia, loai):
        self.ten = ten
        self.gia = gia
        self.loai = loai

    def hien_thi(self):
        return f"{self.ten} | {self.gia} | {self.loai}"


# =========================
# DỮ LIỆU THỰC ĐƠN GIẢ LẬP
# =========================
thuc_don = [
    MonAn("Cơm gà", 35000, "Món chính"),
    MonAn("Bún bò", 40000, "Món chính")
]


# =========================
# AC-01 — HIỂN THỊ THÔNG TIN MÓN
# =========================
def hien_thi_thuc_don():
    print("\n📋 DANH SÁCH THỰC ĐƠN")
    for i, mon in enumerate(thuc_don, start=1):
        print(f"{i}. {mon.hien_thi()}")


# =========================
# AC-02 — KIỂM TRA THÔNG TIN BẮT BUỘC
# =========================
def kiem_tra_bat_buoc(ten, gia, loai):
    if not ten or not gia or not loai:
        print("❌ Không được để trống tên, giá hoặc loại món")
        return False
    return True


# =========================
# AC-03 — KIỂM TRA GIÁ HỢP LỆ
# =========================
def kiem_tra_gia(gia):
    try:
        gia = float(gia)
        if gia <= 0:
            print("❌ Giá phải là số lớn hơn 0")
            return False
        return True
    except ValueError:
        print("❌ Giá phải là số lớn hơn 0")
        return False


# =========================
# AC-04 — CẬP NHẬT MÓN THÀNH CÔNG
# =========================
def cap_nhat_mon():
    hien_thi_thuc_don()

    chon = input("\nChọn món cần chỉnh sửa (số): ").strip()
    if not chon.isdigit():
        print("❌ Lựa chọn không hợp lệ")
        return

    mon = thuc_don[int(chon) - 1]

    print("\n✏ THÔNG TIN HIỆN TẠI")
    print(mon.hien_thi())

    ten_moi = input("Tên món mới: ").strip()
    gia_moi = input("Giá mới: ").strip()
    loai_moi = input("Loại món mới: ").strip()

    # AC-02
    if not kiem_tra_bat_buoc(ten_moi, gia_moi, loai_moi):
        return

    # AC-03
    if not kiem_tra_gia(gia_moi):
        return

    # AC-04
    mon.ten = ten_moi
    mon.gia = float(gia_moi)
    mon.loai = loai_moi

    print("✔ Cập nhật món thành công")


# =========================
# AC-05 — DANH SÁCH ĐƯỢC CẬP NHẬT
# =========================
def chay_chuong_trinh():
    while True:
        print("\n===== QUẢN LÝ THỰC ĐƠN =====")
        print("1. Hiển thị thực đơn")
        print("2. Cập nhật món")
        print("0. Thoát")

        chon = input("Chọn chức năng: ")

        if chon == "1":
            hien_thi_thuc_don()
        elif chon == "2":
            cap_nhat_mon()
            hien_thi_thuc_don()  # AC-05
        elif chon == "0":
            break
        else:
            print("❌ Lựa chọn không hợp lệ")


# =========================
# CHẠY CHƯƠNG TRÌNH
# =========================
chay_chuong_trinh()
