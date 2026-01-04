from datetime import datetime, timedelta
import re

# =========================
# DỮ LIỆU
# =========================
from datetime import datetime

reservations = [
    {
        "customer": "Nguyễn Minh Anh",
        "phone": "0713496285",
        "guests": 4,
        "table": "B01",
        "start": datetime(2026, 3, 20, 18, 0),
        "end":   datetime(2026, 3, 20, 20, 0),
        "note": "",
        "status": "Đã đặt trước"
    },
    {
        "customer": "Trần Văn Chiến",
        "phone": "0572896431",
        "guests": 2,
        "table": "B02",
        "start": datetime(2026, 3, 20, 19, 30),
        "end":   datetime(2026, 3, 20, 21, 30),
        "note": "Gần cửa sổ",
        "status": "Đã đặt trước"
    },
    {
        "customer": "Nguyễn Thị Thuỳ Trang",
        "phone": "0357284916",
        "guests": 6,
        "table": "B03",
        "start": datetime(2026, 3, 21, 17, 30),
        "end":   datetime(2026, 3, 21, 19, 30),
        "note": "",
        "status": "Đã đặt trước"
    },
    {
        "customer": "Nguyễn Quang Trường",
        "phone": "0491728563",
        "guests": 3,
        "table": "B04",
        "start": datetime(2026, 3, 21, 18, 45),
        "end":   datetime(2026, 3, 21, 20, 45),
        "note": "",
        "status": "Đã đặt trước"
    },
    {
        "customer": "Phạm Thế Anh",
        "phone": "0967285413",
        "guests": 5,
        "table": "B05",
        "start": datetime(2026, 3, 22, 18, 0),
        "end":   datetime(2026, 3, 22, 20, 0),
        "note": "Sinh nhật",
        "status": "Đã đặt trước"
    },
    {
        "customer": "Trần Văn Nhật",
        "phone": "0938546712",
        "guests": 2,
        "table": "B06",
        "start": datetime(2026, 3, 22, 20, 15),
        "end":   datetime(2026, 3, 22, 22, 15),
        "note": "",
        "status": "Đã đặt trước"
    },
    {
        "customer": "Lê Tuyết Khánh Ly",
        "phone": "0817964325",
        "guests": 4,
        "table": "B07",
        "start": datetime(2026, 3, 23, 17, 0),
        "end":   datetime(2026, 3, 23, 19, 0),
        "note": "",
        "status": "Đã đặt trước"
    },
    {
        "customer": "Hoàng Thanh Bảo Ngọc",
        "phone": "0721365894",
        "guests": 6,
        "table": "B08",
        "start": datetime(2026, 3, 23, 18, 30),
        "end":   datetime(2026, 3, 23, 20, 30),
        "note": "",
        "status": "Đã đặt trước"
    },
    {
        "customer": "Phùng Phú",
        "phone": "0658497312",
        "guests": 2,
        "table": "B09",
        "start": datetime(2026, 3, 24, 19, 0),
        "end":   datetime(2026, 3, 24, 21, 0),
        "note": "",
        "status": "Đã đặt trước"
    },
    {
        "customer": "Hoàng Trung Dũng",
        "phone": "0498365271",
        "guests": 8,
        "table": "B10",
        "start": datetime(2026, 3, 24, 18, 0),
        "end":   datetime(2026, 3, 24, 20, 0),
        "note": "Tiệc công ty",
        "status": "Đã đặt trước"
    },
    {
        "customer": "Phùng Thị Hồng Vi",
        "phone": "0184963725",
        "guests": 3,
        "table": "B11",
        "start": datetime(2026, 3, 25, 17, 45),
        "end":   datetime(2026, 3, 25, 19, 45),
        "note": "",
        "status": "Đã đặt trước"
    },
    {
        "customer": "Đỗ Hoàng Đại",
        "phone": "0415689723",
        "guests": 4,
        "table": "B12",
        "start": datetime(2026, 3, 25, 20, 0),
        "end":   datetime(2026, 3, 25, 22, 0),
        "note": "",
        "status": "Đã đặt trước"
    },
    {
        "customer": "Trương Thị Hồng Ngọc",
        "phone": "0267183495",
        "guests": 2,
        "table": "B13",
        "start": datetime(2026, 3, 26, 18, 15),
        "end":   datetime(2026, 3, 26, 20, 15),
        "note": "",
        "status": "Đã đặt trước"
    },
    {
        "customer": "Lê Phước Đăng Khoa",
        "phone": "0586392714",
        "guests": 5,
        "table": "B14",
        "start": datetime(2026, 3, 26, 19, 30),
        "end":   datetime(2026, 3, 26, 21, 30),
        "note": "",
        "status": "Đã đặt trước"
    },
    {
        "customer": "Hoàng Chiến Thắng",
        "phone": "0925743168",
        "guests": 6,
        "table": "B15",
        "start": datetime(2026, 3, 27, 18, 0),
        "end":   datetime(2026, 3, 27, 20, 0),
        "note": "",
        "status": "Đã đặt trước"
    }
]


# =========================
# HÀM HỖ TRỢ
# =========================

def is_valid_phone(phone):
    return re.fullmatch(r"\d{10}", phone) is not None


def is_time_overlap(start1, end1, start2, end2):
    return start1 < end2 and start2 < end1

2
def print_table(headers, rows):
    col_widths = [len(h) for h in headers]
    for row in rows:
        for i, cell in enumerate(row):
            col_widths[i] = max(col_widths[i], len(str(cell)))

    def line():
        print("+" + "+".join("-" * (w + 2) for w in col_widths) + "+")

    def print_row(row):
        print("|" + "|".join(
            f" {str(cell).ljust(col_widths[i])} "
            for i, cell in enumerate(row)
        ) + "|")

    line()
    print_row(headers)
    line()
    for row in rows:
        print_row(row)
        line()


def show_reservations():
    if not reservations:
        print("\n📭 Chưa có đặt bàn nào\n")
        return

    rows = []
    for r in reservations:
        rows.append([
            r["table"],
            r["customer"],
            r["phone"],
            r["guests"],
            r["start"].strftime("%d/%m/%Y %H:%M"),
            r["end"].strftime("%H:%M"),
            r["status"],
            r["note"]
        ])

    print("\n📋 DANH SÁCH ĐẶT BÀN")
    print_table(
        ["Bàn", "Khách", "SĐT", "Số khách", "Bắt đầu", "Kết thúc", "Trạng thái", "Ghi chú"],
        rows
    )


# =========================
# TẠO ĐẶT BÀN (AC-01 → AC-04)
# =========================

def create_reservation():
    print("\n=== TẠO ĐẶT BÀN ===")

    customer = input("Tên khách hàng: ").strip()
    phone = input("Số điện thoại (10 số): ").strip()
    guests = input("Số khách: ").strip()
    table = input("Tên bàn: ").strip()
    time_str = input("Thời gian (dd/mm/yyyy hoặc dd/mm/yyyy HH:MM): ").strip()
    note = input("Ghi chú (có thể bỏ trống): ").strip()

    # ---- AC-02: kiểm tra bắt buộc ----
    if not customer or not phone or not guests or not table or not time_str:
        print("❌ Thiếu thông tin bắt buộc")
        return

    if not is_valid_phone(phone):
        print("❌ Số điện thoại không hợp lệ")
        return

    try:
        if len(time_str) == 10:
            start_time = datetime.strptime(time_str, "%d/%m/%Y")
            start_time = start_time.replace(hour=18, minute=0)
        else:
            start_time = datetime.strptime(time_str, "%d/%m/%Y %H:%M")
    except ValueError:
        print("❌ Sai định dạng thời gian")
        return

    now = datetime.now()
    if start_time < now:
        print("❌ Không thể đặt thời gian đã qua")
        return

    if start_time > now + timedelta(days=100):
        print("❌ Không thể đặt quá 100 ngày")
        return

    end_time = start_time + timedelta(hours=2)

    # ---- AC-01: hạn chế trùng tên bàn ----
    for r in reservations:
        if r["table"].lower() == table.lower():
            if is_time_overlap(start_time, end_time, r["start"], r["end"]):
                print("❌ Bàn đã được đặt trong thời gian này")
                return

    # Tạo đặt bàn
    reservation = {
        "customer": customer,
        "phone": phone,
        "guests": guests,
        "table": table,
        "start": start_time,
        "end": end_time,
        "note": note,
        "status": "Đã đặt trước"
    }

    reservations.append(reservation)

    print("✅ Tạo đặt bàn thành công! Thông tin bàn vừa tạo:")

    # In ra bảng 1 dòng
    headers = ["Bàn", "Khách", "SĐT", "Số khách", "Bắt đầu", "Kết thúc", "Trạng thái", "Ghi chú"]
    row = [[
        reservation["table"],
        reservation["customer"],
        reservation["phone"],
        reservation["guests"],
        reservation["start"].strftime("%d/%m/%Y %H:%M"),
        reservation["end"].strftime("%H:%M"),
        reservation["status"],
        reservation["note"]
    ]]
    print_table(headers, row)


# =========================
# MENU CHÍNH
# =========================

def main_menu():
    while True:
        print("""
========= MENU =========
1. Tạo đặt bàn
2. Xem danh sách đặt bàn
0. Thoát
========================
        """)

        choice = input("👉 Chọn chức năng: ")

        if choice == "1":
            create_reservation()
        elif choice == "2":
            show_reservations()
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
