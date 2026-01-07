# HỆ THỐNG QUẢN LÝ BÀN ĂN
# US-01 + US-02

# DỮ LIỆU GIẢ LẬP

tables = []
subscribers = []  # giả lập realtime
next_table_id = 1


# =========================
# REALTIME (GIẢ LẬP)
# =========================

def notify_realtime():
    for sub in subscribers:
        sub()


def realtime_listener():
    print("🔄 Dữ liệu bàn đã được cập nhật realtime!")


subscribers.append(realtime_listener)


# =========================
# HÀM TIỆN ÍCH
# =========================

def show_tables():
    if not tables:
        print("\n📭 Chưa có bàn nào trong hệ thống\n")
        return

    print("\n--- DANH SÁCH BÀN ---")
    for t in tables:
        print(
            f"ID: {t['id']} | {t['name']} | "
            f"Số chỗ: {t['seats']} | Trạng thái: {t['status']}"
        )
    print("--------------------\n")


def find_table_by_id(table_id):
    for table in tables:
        if table["id"] == table_id:
            return table
    return None


def is_duplicate_table_name(name, exclude_id=None):
    for table in tables:
        if table["name"] == name:
            if exclude_id is None or table["id"] != exclude_id:
                return True
    return False


# =========================
# US-01 — TẠO BÀN
# =========================

def create_table(name, seats):
    global next_table_id

    if not name or not name.strip():
        return "❌ Tên bàn không được để trống"

    if not isinstance(seats, int) or seats <= 0:
        return "❌ Số chỗ ngồi phải là số nguyên dương"

    if is_duplicate_table_name(name.strip()):
        return "❌ Tên bàn đã tồn tại"

    table = {
        "id": next_table_id,
        "name": name.strip(),
        "seats": seats,
        "status": "Trống"
    }

    tables.append(table)
    next_table_id += 1

    notify_realtime()
    return "✅ Tạo bàn thành công"


# =========================
# US-02 — CẬP NHẬT BÀN
# =========================

def update_table(table_id, new_name, new_seats):
    table = find_table_by_id(table_id)
    if not table:
        return "❌ Bàn không tồn tại"

    if not new_name or not new_name.strip():
        return "❌ Tên bàn không được để trống"

    if not isinstance(new_seats, int) or new_seats <= 0:
        return "❌ Số chỗ ngồi phải là số nguyên dương"

    if is_duplicate_table_name(new_name.strip(), table_id):
        return "❌ Tên bàn đã tồn tại"

    table["name"] = new_name.strip()
    table["seats"] = new_seats

    notify_realtime()
    return "✅ Cập nhật thông tin bàn thành công"


# =========================
# NHẬP DỮ LIỆU TỪ BÀN PHÍM
# =========================

def input_create_table():
    print("\n=== TẠO BÀN MỚI ===")
    name = input("Nhập tên bàn: ")

    try:
        seats = int(input("Nhập số chỗ ngồi: "))
    except ValueError:
        print("❌ Số chỗ ngồi phải là số nguyên")
        return

    print(create_table(name, seats))


def input_update_table():
    if not tables:
        print("❌ Không có bàn nào để cập nhật")
        return

    show_tables()

    print("=== CẬP NHẬT THÔNG TIN BÀN ===")
    try:
        table_id = int(input("Nhập ID bàn: "))
    except ValueError:
        print("❌ ID bàn phải là số")
        return

    new_name = input("Nhập tên bàn mới: ")

    try:
        new_seats = int(input("Nhập số chỗ ngồi mới: "))
    except ValueError:
        print("❌ Số chỗ ngồi phải là số")
        return

    print(update_table(table_id, new_name, new_seats))


# =========================
# MENU CHÍNH
# =========================

def main_menu():
    while True:
        print("📋 MENU QUẢN LÝ BÀN")
        print("1. Tạo bàn mới")
        print("2. Cập nhật thông tin bàn")
        print("0. Thoát")

        choice = input("Chọn chức năng: ")

        if choice == "1":
            input_create_table()
        elif choice == "2":
            input_update_table()
        elif choice == "0":
            print("👋 Thoát chương trình")
            break
        else:
            print("❌ Lựa chọn không hợp lệ")


# =========================
# CHẠY CHƯƠNG TRÌNH
# =========================

if __name__ == "__main__":
    main_menu()
