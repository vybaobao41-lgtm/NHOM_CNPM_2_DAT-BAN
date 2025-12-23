# =========================
# US-02 — CẬP NHẬT THÔNG TIN BÀN
# =========================

# =========================
# DỮ LIỆU GIẢ LẬP
# =========================

tables = [
    {
        "id": 1,
        "name": "Bàn 01",
        "seats": 4,
        "status": "Trống"
    },
    {
        "id": 2,
        "name": "Bàn 02",
        "seats": 6,
        "status": "Đang phục vụ"
    }
]

subscribers = []  # giả lập realtime


# =========================
# HÀM HỖ TRỢ
# =========================

def notify_realtime():
    """AC-02: đồng bộ realtime"""
    for sub in subscribers:
        sub()


def find_table_by_id(table_id):
    """Tìm bàn theo ID"""
    for table in tables:
        if table["id"] == table_id:
            return table
    return None


def is_duplicate_table_name(name, exclude_id):
    """AC-01: kiểm tra trùng tên bàn"""
    for table in tables:
        if table["name"] == name and table["id"] != exclude_id:
            return True
    return False


def show_tables():
    print("\n--- DANH SÁCH BÀN ---")
    for t in tables:
        print(
            f"ID: {t['id']} | {t['name']} | "
            f"Số chỗ: {t['seats']} | Trạng thái: {t['status']}"
        )
    print("--------------------\n")


# =========================
# US-02 — CẬP NHẬT THÔNG TIN BÀN
# =========================

def update_table(table_id, new_name, new_seats):
    """
    AC-01: Kiểm tra tính hợp lệ
    AC-02: Cập nhật khi đang sử dụng + realtime
    AC-03: Cập nhật thành công
    AC-04: Hủy (không xử lý trong function, do UI xử lý)
    """

    # ---- AC-01: bàn tồn tại ----
    table = find_table_by_id(table_id)
    if not table:
        return "❌ Bàn không tồn tại"

    # ---- AC-01: validate tên bàn ----
    if not new_name or not new_name.strip():
        return "❌ Tên bàn không được để trống"

    # ---- AC-01: validate số chỗ ngồi ----
    if not isinstance(new_seats, int):
        return "❌ Số chỗ ngồi phải là số"
    if new_seats <= 0:
        return "❌ Số chỗ ngồi phải là số nguyên dương"

    # ---- AC-01: trùng tên bàn ----
    if is_duplicate_table_name(new_name.strip(), table_id):
        return "❌ Tên bàn đã tồn tại"

    # ---- AC-02: cập nhật khi đang phục vụ ----
    # KHÔNG đổi trạng thái
    # KHÔNG ảnh hưởng order / đặt bàn

    table["name"] = new_name.strip()
    table["seats"] = new_seats

    # ---- AC-02: realtime sync ----
    notify_realtime()

    # ---- AC-03: thành công ----
    return "✅ Cập nhật thông tin bàn thành công"


# =========================
# GIẢ LẬP REALTIME LISTENER
# =========================

def realtime_listener():
    print("🔄 Dữ liệu bàn đã được cập nhật realtime!")
    show_tables()


subscribers.append(realtime_listener)


# =========================
# TEST THỦ CÔNG (CÓ THỂ XÓA KHI PUSH)
# =========================

if __name__ == "__main__":
    show_tables()

    print(update_table(2, "Bàn VIP", 8))
    print(update_table(1, "Bàn VIP", 4))     # trùng tên
    print(update_table(1, "", 4))            # lỗi tên
    print(update_table(1, "Bàn 01A", -1))    # lỗi số chỗ
    print(update_table(99, "Bàn 99", 4))     # không tồn tại
