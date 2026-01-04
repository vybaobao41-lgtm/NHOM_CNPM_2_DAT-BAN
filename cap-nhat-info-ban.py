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


# =========================
# REALTIME (AC02)
# =========================

subscribers = []

def dang_ky_realtime(ten_client):
    subscribers.append(ten_client)

def thong_bao_realtime(ban):
    for client in subscribers:
        print(f"🔔 [Realtime → {client}] "
              f"Bàn B{ban.table_id} cập nhật → {ban.trang_thai}")


# =========================
# HIỂN THỊ BẢNG (UI)
# =========================

def in_bang_ban(danh_sach_ban, tieu_de="DANH SÁCH BÀN"):
    print(f"\n=== {tieu_de} ===")
    print("+------+------------+-------+----------+---------------+")
    print("| ID   |    Ngày    |  Giờ  | Số người |   Trạng thái  |")
    print("+------+------------+-------+----------+---------------+")

    for b in danh_sach_ban:
        print(f"| B{b.table_id:<3} "
              f"| {b.ngay:<10} "
              f"| {b.gio:<5} "
              f"| {b.so_nguoi:^8} "
              f"| {b.trang_thai:<13} |")
        print("+------+------------+-------+----------+---------------+")


# =========================
# VALIDATION (AC01)
# =========================

def kiem_tra_hop_le(ngay, gio, so_nguoi, trang_thai):
    if not ngay or not gio:
        return False, "Ngày và giờ không được để trống"

    try:
        datetime.strptime(ngay, "%d/%m/%Y")
    except ValueError:
        return False, "Sai định dạng ngày (dd/mm/yyyy) hoặc giờ (hh:mm)"
        datetime.strptime(gio, "%H:%M")

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
                return None

            ban.ngay = ngay_moi
            ban.gio = gio_moi
            ban.so_nguoi = so_nguoi_moi
            ban.trang_thai = trang_thai_moi

            print("✅ Cập nhật bàn thành công!")
            thong_bao_realtime(ban)

            return ban

    print("❌ Không tìm thấy bàn")
    return None


# =========================
# UI CẬP NHẬT 1 BÀN
# =========================

def cap_nhat_1_ban(danh_sach_ban):
    raw_id = input("Nhập ID bàn: ").strip().upper()

    if not raw_id.startswith("B") or not raw_id[1:].isdigit():
        print("❌ ID không hợp lệ")
        return

    table_id = int(raw_id[1:])
    ban = next((b for b in danh_sach_ban if b.table_id == table_id), None)

    if not ban:
        print("❌ Không tìm thấy bàn")
        return

    in_bang_ban([ban], "THÔNG TIN HIỆN TẠI")

    xac_nhan = input("Bạn có muốn cập nhật bàn này không? (y/n): ").lower()
    if xac_nhan != "y":
        print("⛔ Đã hủy cập nhật")
        return

    ngay_moi = input("Ngày (dd/mm/yyyy): ").strip()
    gio_moi = input("Giờ (hh:mm): ").strip()

    try:
        so_nguoi_moi = int(input("Số người: "))
    except ValueError:
        print("❌ Số người phải là số")
        return

    trang_thai_moi = input("Trạng thái (Trống / Đang sử dụng / Đã đặt): ").strip()

    ban_moi = cap_nhat_ban(
        danh_sach_ban,
        table_id,
        ngay_moi,
        gio_moi,
        so_nguoi_moi,
        trang_thai_moi
    )

    if ban_moi:
        in_bang_ban([ban_moi], "BÀN VỪA CẬP NHẬT")


# =========================
# MENU ĐIỀU KHIỂN
# =========================

def menu(danh_sach_ban):
    while True:
        print("\n===== MENU =====")
        print("1. Cập nhật bàn")
        print("2. In toàn bộ danh sách bàn")
        print("0. Thoát")

        chon = input("Chọn chức năng: ").strip()

        if chon == "1":
            cap_nhat_1_ban(danh_sach_ban)
        elif chon == "2":
            in_bang_ban(danh_sach_ban)
        elif chon == "0":
            print("👋 Thoát chương trình")
            break
        else:
            print("❌ Lựa chọn không hợp lệ")


# =========================
# DEMO
# =========================

if __name__ == "__main__":

    dang_ky_realtime("Quầy lễ tân")
    dang_ky_realtime("Màn hình quản lý")

    danh_sach_ban = [
        Table(1, "02/01/2026", "17:15", 2, "Trống"),
        Table(2, "05/01/2026", "18:40", 4, "Đã đặt"),
        Table(3, "08/01/2026", "19:25", 6, "Đang sử dụng"),
        Table(4, "12/01/2026", "11:35", 2, "Trống"),
        Table(5, "15/01/2026", "18:10", 8, "Đã đặt"),
        Table(6, "19/01/2026", "20:05", 2, "Đang sử dụng"),
        Table(7, "22/01/2026", "17:50", 2, "Trống"),
        Table(8, "24/01/2026", "19:15", 4, "Đã đặt"),
        Table(9, "29/01/2026", "20:45", 10, "Đang sử dụng"),
        Table(10, "02/02/2026", "16:40", 2, "Trống"),
        Table(11, "05/02/2026", "18:25", 5, "Đã đặt"),
        Table(12, "10/02/2026", "19:55", 4, "Đang sử dụng"),
        Table(13, "14/02/2026", "17:20", 2, "Trống"),
        Table(14, "18/02/2026", "18:50", 4, "Đã đặt"),
        Table(15, "22/02/2026", "21:10", 6, "Đang sử dụng"),
    ]

    menu(danh_sach_ban)
