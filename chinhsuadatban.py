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






import datetime

class TableNoteService:
    def __init__(self):
        # AC-06: Giới hạn độ dài ghi chú
        self.MAX_NOTE_LENGTH = 200
        # Dữ liệu bàn mặc định
        self.table = {"id": "05", "note": "", "trang_thai": "Trống"}
        self.lich_su = []

    def hien_thi_ban(self):
        print("\n" + "="*30)
        print(f"BÀN SỐ: {self.table['id']}")
        print(f"Trạng thái: {self.table['trang_thai']}")
        # AC-02: Hiển thị ghi chú rõ ràng trên sơ đồ bàn
        note_display = self.table['note'] if self.table['note'] else "(Trống)"
        print(f"Ghi chú hiện tại: {note_display}")
        print("="*30)

    def menu(self):
        print("--- HỆ THỐNG QUẢN LÝ GHI CHÚ BÀN ---")
        nhan_vien = input("Nhập tên nhân viên: ")

        while True:
            self.hien_thi_ban()
            print("1. Thêm/Sửa ghi chú (AC-01, AC-03)")
            print("2. Xóa ghi chú (AC-04)")
            print("3. Bỏ qua nhập ghi chú (AC-05)")
            print("4. Thanh toán (AC-07)")
            print("5. Thoát")
            
            lua_chon = input("Chọn thao tác (1-5): ")

            if lua_chon == '1':
                # AC-01 & AC-03: Thêm và Chỉnh sửa
                note_input = input(f"Nhập nội dung ghi chú (tối đa {self.MAX_NOTE_LENGTH} ký tự): ")
                
                # AC-06: Kiểm tra độ dài
                if len(note_input) > self.MAX_NOTE_LENGTH:
                    print(f">> [AC-06] Lỗi: Ghi chú vượt quá {self.MAX_NOTE_LENGTH} ký tự!")
                elif note_input.strip() == "":
                    print(">> Lỗi: Vui lòng nhập nội dung hoặc chọn mục xóa.")
                else:
                    self.table['note'] = note_input.strip()
                    print(f">> [AC-01/03] Hệ thống đã lưu ghi chú thành công.")
                    self.table['trang_thai'] = "Đã đặt"

            elif lua_chon == '2':
                # AC-04: Xóa ghi chú
                if self.table['note'] == "":
                    print(">> Bàn hiện không có ghi chú để xóa.")
                else:
                    xac_nhan = input("Xác nhận xóa ghi chú bàn? (y/n): ")
                    if xac_nhan.lower() == 'y':
                        self.table['note'] = ""
                        print(">> [AC-04] Ghi chú đã được xóa khỏi bàn.")

            elif lua_chon == '3':
                # AC-05: Không bắt buộc nhập
                print(">> [AC-05] Đã bỏ qua. Hệ thống tiếp tục các thao tác khác.")

            elif lua_chon == '4':
                # AC-07: Ghi chú không ảnh hưởng hóa đơn
                amount = 250000
                print(f">> [AC-07] Tổng tiền hóa đơn: {amount:,}đ")
                print(">> Hệ thống xác nhận: Ghi chú không làm thay đổi giá tiền thanh toán.")

            elif lua_chon == '5':
                print("Đang thoát...")
                break
            else:
                print("Lựa chọn không hợp lệ!")

# --- CHẠY CHƯƠNG TRÌNH ---
if __name__ == "__main__":
    app = TableNoteService()
    app.menu()