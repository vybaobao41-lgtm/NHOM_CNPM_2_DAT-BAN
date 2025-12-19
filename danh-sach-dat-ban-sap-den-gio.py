from datetime import datetime, timedelta

# =========================
# DỮ LIỆU GIẢ LẬP
# =========================

reservations = [
    {
        "customer": "Nguyen Van A",
        "phone": "0901234567",
        "guests": 4,
        "table": "B1",
        "start": datetime.now() + timedelta(minutes=10),
        "end": datetime.now() + timedelta(hours=2, minutes=10),
        "note": "Sinh nhật, cần trang trí",
        "status": "Chưa đến"
    },
    {
        "customer": "Tran Van B",
        "phone": "0911111111",
        "guests": 2,
        "table": "B2",
        "start": datetime.now() + timedelta(minutes=40),
        "end": datetime.now() + timedelta(hours=2, minutes=40),
        "note": "",
        "status": "Chưa đến"
    },
    {
        "customer": "Le Thi C",
        "phone": "0922222222",
        "guests": 3,
        "table": "B3",
        "start": datetime.now() + timedelta(minutes=20),
        "end": datetime.now() + timedelta(hours=2, minutes=20),
        "note": "Yêu cầu món chay",
        "status": "Đã check-in"
    }
]


# =========================
# HÀM HIỂN THỊ ĐẶT BÀN SẮP ĐẾN
# =========================

def get_upcoming_reservations(minutes=30):
    """
    Trả về danh sách đặt bàn sắp đến trong 'minutes' phút tới
    AC-01: Hiển thị danh sách sắp đến
    AC-04: Sắp xếp theo thời gian đến
    AC-05: Loại trừ đặt bàn không hợp lệ
    """
    now = datetime.now()
    end_window = now + timedelta(minutes=minutes)

    upcoming = [
        r for r in reservations
        if r["status"] == "Chưa đến" and now <= r["start"] <= end_window
    ]

    # AC-04: sắp xếp theo thời gian đến
    upcoming.sort(key=lambda x: x["start"])

    return upcoming


# =========================
# HÀM HIỂN THỊ DANH SÁCH
# =========================

def show_upcoming_reservations(minutes=30):
    """
        Hiển thị danh sách đặt bàn sắp đến trong 'minutes' phút tới
        AC-01 → AC-06
    """
    upcoming = get_upcoming_reservations(minutes)

    # AC-08: trường hợp không có đặt bàn
    if not upcoming:
        print("❌ Không có đặt bàn sắp đến giờ")
        return

    print(f"--- DANH SÁCH ĐẶT BÀN SẮP ĐẾN ({minutes} phút) ---")
    for r in upcoming:
        # AC-02: thông tin hiển thị đầy đủ
        print(f"Bàn: {r['table']}")
        print(f"Khách: {r['customer']} | SĐT: {r['phone']} | Số khách: {r['guests']}")
        print(f"Thời gian đến: {r['start'].strftime('%H:%M')} - {r['end'].strftime('%H:%M')}")
        print(f"Trạng thái: {r['status']}")
        print(f"Ghi chú: {r['note']}")
        print("---------------------------")


# =========================
# AC-07: Truy cập nhanh chi tiết đặt bàn
# =========================

def show_reservation_detail(reservation):
    print("=== CHI TIẾT ĐẶT BÀN ===")
    for key, value in reservation.items():
        if isinstance(value, datetime):
            print(f"{key}: {value.strftime('%Y-%m-%d %H:%M')}")
        else:
            print(f"{key}: {value}")
    print("=========================")


# =========================
# Demo / test (không bắt buộc, để sinh viên hiểu)
# =========================
if __name__ == "__main__":
    show_upcoming_reservations()  # AC-01 → AC-06
    print("\nChi tiết bàn đầu tiên (AC-07):")
    upcoming = get_upcoming_reservations()
    if upcoming:
        show_reservation_detail(upcoming[0])
