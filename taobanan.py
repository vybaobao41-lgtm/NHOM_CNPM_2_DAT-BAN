
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

