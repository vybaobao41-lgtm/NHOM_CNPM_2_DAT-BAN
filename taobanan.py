
# =========================
# DỮ LIỆU BÀN ĂN (giả lập ban đầu: đã hết bàn trống)
# =========================
ban_an = {
    1: {"trang_thai": "đặt", "khach": "Vy", "so_nguoi": 4},
    2: {"trang_thai": "đặt", "khach": "Thi", "so_nguoi": 2},
    3: {"trang_thai": "đặt", "khach": "Chi", "so_nguoi": 6},
}

# =========================
# AC-01: Tạo bàn mới khi đã hết bàn
# =========================
def kiem_tra_het_ban():
    for info in ban_an.values():
        if info["trang_thai"] == "trống":
            return False
    return True


def hoi_them_ban_khi_het():
    if kiem_tra_het_ban():
        print("⚠ Hiện tại đã hết bàn trống!")
        chon = input("Bạn có muốn thêm bàn mới không? (Y/N): ").strip().lower()
        if chon == "y":
            return True
        else:
            print("❌ Không thêm bàn mới")
            return False
    return True

# =========================
# AC-02: Kiểm tra thông tin khách hợp lệ
# =========================
def kiem_tra_thong_tin_khach(ten_khach, so_nguoi):
    if ten_khach.strip() == "":
        return False, "❌ Tên khách không được để trống"

    if not so_nguoi.isdigit():
        return False, "❌ Số người phải là số"

    if int(so_nguoi) <= 0:
        return False, "❌ Số người phải lớn hơn 0"

    return True, ""

# =========================
# AC-03: Thêm bàn ăn thành công
# =========================
def them_ban_moi(ten_khach, so_nguoi):
    so_ban_moi = max(ban_an.keys()) + 1

    ban_an[so_ban_moi] = {
        "trang_thai": "đặt",
        "khach": ten_khach,
        "so_nguoi": int(so_nguoi)
    }

    print(f"✔ Thêm bàn {so_ban_moi} cho {ten_khach} ({so_nguoi} khách) thành công!")

