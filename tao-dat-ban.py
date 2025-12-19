from datetime import datetime, timedelta
import re
import threading
import time

# =========================
# DỮ LIỆU GIẢ LẬP
# =========================

reservations = []       # danh sách đặt bàn
subscribers = []        # giả lập realtime (AC-03)

# =========================
# HÀM HỖ TRỢ
# =========================

def is_valid_phone(phone):
    """AC-02.1: kiểm tra số điện thoại"""
    return re.fullmatch(r"\d{10}", phone) is not None


def is_time_overlap(start1, end1, start2, end2):
    """Kiểm tra trùng thời gian"""
    return start1 < end2 and start2 < end1


def notify_realtime():
    """AC-03: giả lập realtime refresh"""
    for sub in subscribers:
        sub()


def show_reservations():
    print("\n--- DANH SÁCH ĐẶT BÀN ---")
    for r in reservations:
        print(
            f"{r['table']} | {r['customer']} | {r['phone']} | "
            f"{r['start']} - {r['end']} | {r['status']}"
        )
    print("-------------------------\n")


# =========================
# AC-01 + AC-02 + AC-04
# =========================

def create_reservation(customer, phone, guests, table, start_time, note=""):
    now = datetime.now()

    # ---- AC-02.1: kiểm tra số điện thoại ----
    if not is_valid_phone(phone):
        return "❌ Số điện thoại không hợp lệ"

    # ---- AC-02.4: kiểm tra thời gian ----
    if start_time < now:
        return "❌ Không thể đặt thời gian đã qua"

    if start_time > now + timedelta(days=30):
        return "❌ Không thể đặt quá 30 ngày"

    end_time = start_time + timedelta(hours=2)  # mặc định 1 ca 2 tiếng

    # ---- AC-02.2: không trùng bàn – cùng khung giờ ----
    for r in reservations:
        if r["table"] == table:
            if is_time_overlap(start_time, end_time, r["start"], r["end"]):
                return "❌ Bàn đã được đặt trong thời gian này"

    # ---- AC-02.3: không trùng khách – cùng thời gian ----
    for r in reservations:
        if r["phone"] == phone:
            if is_time_overlap(start_time, end_time, r["start"], r["end"]):
                return "❌ Khách đã có đặt bàn trong thời gian này"

    # ---- AC-01: tạo đặt bàn thành công ----
    reservation = {
        "customer": customer,
        "phone": phone,
        "guests": guests,
        "table": table,
        "start": start_time,
        "end": end_time,
        "note": note,              # AC-04
        "status": "Đã đặt trước"
    }

    reservations.append(reservation)

    # ---- AC-03: cập nhật realtime ----
    notify_realtime()

    return "✅ Tạo đặt bàn thành công"


# =========================
# GIẢ LẬP REALTIME (AC-03)
# =========================

def realtime_listener():
    print("🔄 Danh sách đặt bàn đã được cập nhật realtime!")
    show_reservations()


subscribers.append(realtime_listener)
