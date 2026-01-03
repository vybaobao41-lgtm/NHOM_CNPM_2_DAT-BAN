from datetime import datetime

# =========================
# ENTITY
# =========================

class Table:
    def __init__(self, table_id, ngay, gio, so_nguoi, trang_thai):
        self.table_id = table_id
        self.ngay = ngay
        self.gio = gio
        self.so_nguoi = so_nguoi
        self.trang_thai = trang_thai

    def __str__(self):
        return (f"Bàn {self.table_id} | Ngày: {self.ngay} | Giờ: {self.gio} | "
                f"Số người: {self.so_nguoi} | Trạng thái: {self.trang_thai}")


# =========================
# VALIDATION (AC01)
# =========================

def kiem_tra_hop_le(ngay, gio, so_nguoi, trang_thai):
    if not ngay or not gio:
        return False, "Ngày và giờ không được để trống"

    try:
        datetime.strptime(ngay, "%Y-%m-%d")
        datetime.strptime(gio, "%H:%M")
    except ValueError:
        return False, "Sai định dạng ngày (yyyy-mm-dd) hoặc giờ (hh:mm)"

    if so_nguoi <= 0:
        return False, "Số người phải lớn hơn 0"

    if trang_thai not in ["Trống", "Đang sử dụng", "Đã đặt"]:
        return False, "Trạng thái không hợp lệ"

    return True, ""


# =========================
# BUSINESS LOGIC (US-02)
# =========================

def cap_nhat_ban(danh_sach_ban, table_id,
                 ngay_moi, gio_moi,
                 so_nguoi_moi, trang_thai_moi):

    for ban in danh_sach_ban:
        if ban.table_id == table_id:

            hop_le, thong_bao = kiem_tra_hop_le(
                ngay_moi, gio_moi, so_nguoi_moi, trang_thai_moi
            )

            if not hop_le:
                print(f"❌ {thong_bao}")
                return False

            ban.ngay = ngay_moi
            ban.gio = gio_moi
            ban.so_nguoi = so_nguoi_moi
            ban.trang_thai = trang_thai_moi

            print("✅ Cập nhật bàn thành công!")
            print(ban)
            return True

    print("❌ Không tìm thấy bàn")
    return False


# =========================
# UI NHẬP TỪ BÀN PHÍM (US-02)
# =========================

def cap_nhat_thong_tin_ban_tu_ban_phim(danh_sach_ban):
    print("\n=== CẬP NHẬT THÔNG TIN BÀN (US-02) ===")

    # Nhập ID
    try:
        table_id = int(input("Nhập ID bàn: "))
    except ValueError:
        print("❌ ID phải là số")
        return

    ban = next((b for b in danh_sach_ban if b.table_id == table_id), None)
    if not ban:
        print("❌ Không tìm thấy bàn")
        return

    print("\nThông tin hiện tại:")
    print(ban)

    # Xác nhận cập nhật (AC04)
    xac_nhan = input("\nBạn có muốn cập nhật bàn này không? (y/n): ").lower()
    if xac_nhan != "y":
        print("⛔ Đã hủy cập nhật")
        return

    print("\nNhập thông tin mới:")

    ngay_moi = input("Ngày (yyyy-mm-dd): ").strip()
    gio_moi = input("Giờ (hh:mm): ").strip()

    try:
        so_nguoi_moi = int(input("Số người: "))
    except ValueError:
        print("❌ Số người phải là số")
        return

    trang_thai_moi = input("Trạng thái (Trống / Đang sử dụng / Đã đặt): ").strip()

    cap_nhat_ban(
        danh_sach_ban,
        table_id,
        ngay_moi,
        gio_moi,
        so_nguoi_moi,
        trang_thai_moi
    )


# =========================
# DEMO
# =========================

if __name__ == "__main__":
    danh_sach_ban = [
        Table(1, "2026-01-03", "18:00", 4, "Trống"),
        Table(2, "2026-01-03", "19:00", 6, "Đang sử dụng"),
        Table(3, "2026-01-04", "20:00", 2, "Đã đặt")
    ]

    print("=== DANH SÁCH BÀN ===")
    for ban in danh_sach_ban:
        print(ban)

    cap_nhat_thong_tin_ban_tu_ban_phim(danh_sach_ban)

    print("\n=== SAU CẬP NHẬT ===")
    for ban in danh_sach_ban:
        print(ban)
