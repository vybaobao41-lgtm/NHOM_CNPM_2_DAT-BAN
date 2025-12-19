import re
from datetime import datetime

# ===============================
# US07 — CHỈNH SỬA ĐẶT BÀN
# AC-01, AC-02, AC-03
# ===============================

# Dữ liệu đặt bàn (nhập ban đầu)
bookings = []

# ===============================
# HÀM HỖ TRỢ
# ===============================

def valid_phone(phone: str) -> bool:
    """AC-02.1: Kiểm tra định dạng SĐT (0xxxxxxxxx)"""
    return bool(re.fullmatch(r"0\d{9}", phone))


def parse_time(time_str: str):
    """Parse thời gian YYYY-MM-DD HH:MM"""
    try:
        return datetime.strptime(time_str, "%Y-%m-%d %H:%M")
    except ValueError:
        return None


def duplicate_customer(booking_id, phone, time_str) -> bool:
    """AC-02.2: Không trùng khách – giờ"""
    for b in bookings:
        if b["id"] != booking_id and b["phone"] == phone and b["time"] == time_str:
            return True
    return False


def duplicate_table(booking_id, table, time_str) -> bool:
    """AC-02.3: Không trùng bàn – giờ"""
    for b in bookings:
        if b["id"] != booking_id and b["table"] == table and b["time"] == time_str:
            return True
    return False


# ===============================
# NHẬP DỮ LIỆU BAN ĐẦU
# ===============================

def input_initial_bookings():
    print("📥 NHẬP DANH SÁCH ĐẶT BÀN BAN ĐẦU")
    n = int(input("Số lượng đặt bàn: "))

    for i in range(1, n + 1):
        print(f"\n➡️ Đặt bàn #{i}")
        booking = {
            "id": i,
            "customer_name": input("Tên khách: "),
            "phone": input("SĐT: "),
            "guests": int(input("Số khách: ")),
            "time": input("Thời gian (YYYY-MM-DD HH:MM): "),
            "table": input("Tên bàn: "),
            "note": input("Ghi chú: ")
        }
        bookings.append(booking)


# ===============================
# AC-01 + AC-02 + AC-03
# ===============================

def edit_booking():
    print("\n📋 DANH SÁCH ĐẶT BÀN")
    for b in bookings:
        print(f"ID {b['id']} | {b['customer_name']} | {b['time']} | {b['table']}")

    booking_id = int(input("\nNhập ID cần chỉnh sửa: "))
    booking = next((b for b in bookings if b["id"] == booking_id), None)

    if not booking:
        print("❌ Không tìm thấy đặt bàn.")
        return

    print("\n✏️ Nhập thông tin mới (Enter để giữ nguyên)")
    name = input(f"Tên khách [{booking['customer_name']}]: ") or booking["customer_name"]
    phone = input(f"SĐT [{booking['phone']}]: ") or booking["phone"]
    guests = input(f"Số khách [{booking['guests']}]: ") or booking["guests"]
    time = input(f"Thời gian [{booking['time']}]: ") or booking["time"]
    table = input(f"Tên bàn [{booking['table']}]: ") or booking["table"]
    note = input(f"Ghi chú [{booking['note']}]: ") or booking["note"]

    # AC-02.1 — SĐT hợp lệ
    if not valid_phone(phone):
        print("❌ Số điện thoại không hợp lệ.")
        return

    # AC-02.4 — Thời gian hợp lệ
    parsed_time = parse_time(time)
    if not parsed_time or parsed_time < datetime.now():
        print("❌ Thời gian không hợp lệ hoặc đã qua.")
        return

    # AC-02.2 — Trùng khách – giờ
    if duplicate_customer(booking_id, phone, time):
        print("❌ Khách đã có đặt bàn trong thời gian này.")
        return

    # AC-02.3 — Trùng bàn – giờ
    if duplicate_table(booking_id, table, time):
        print("❌ Bàn đã được đặt trong thời gian này.")
        return

    # AC-01 + AC-03 — Lưu cập nhật
    booking.update({
        "customer_name": name,
        "phone": phone,
        "guests": int(guests),
        "time": time,
        "table": table,
        "note": note
    })

    print("\n✅ CẬP NHẬT THÀNH CÔNG")
    print("📌 Thông tin mới:")
    print(booking)


# ===============================
# CHẠY CHƯƠNG TRÌNH
# ===============================

if __name__ == "__main__":
    input_initial_bookings()
    edit_booking()
