from datetime import datetime, timedelta

class BookingService:
    def __init__(self):
        self.LATE_THRESHOLD = 30  # Ngưỡng trễ 30 phút (AC-09)

    def execute_checkin(self, booking, table):
        now = datetime.now()

        # AC-02: Given Đặt bàn Đã hủy -> Then Thông báo lỗi
        if booking['status'] == "Đã hủy":
            return False, "Đặt bàn đã bị hủy"

        # AC-03: Given Đã check-in -> Then Từ chối thao tác
        if booking['status'] == "Đã check-in":
            return False, "Khách đã check-in"

        # AC-06: Given Bàn đang phục vụ -> Then Không cho phép check-in
        if table['status'] == "Đang phục vụ":
            return False, "Bàn hiện không khả dụng"

        # AC-08 & AC-09: Xử lý cảnh báo thời gian
        message = "Check-in thành công"
        if now < booking['scheduled_time']:
            message = "Check-in thành công (Khách đến sớm)"
        elif now > (booking['scheduled_time'] + timedelta(minutes=self.LATE_THRESHOLD)):
            message = "Cảnh báo: Khách đến trễ quá thời gian cho phép"

        # AC-01, 04, 05, 07: Cập nhật dữ liệu hệ thống
        booking['status'] = "Đã check-in"
        booking['check_in_time'] = now.strftime("%H:%M:%S")
        table['status'] = "Đang phục vụ"
        
        return True, message

# --- MÔ PHỎNG KIỂM THỬ (GIVEN - WHEN - THEN) ---
if __name__ == "__main__":
    service = BookingService()

    print("=== TEST AC-01: CHECK-IN THÀNH CÔNG ===")
    # GIVEN: Đặt bàn 'Đã đặt', bàn 'Trống'
    booking_data = {"status": "Đã đặt", "scheduled_time": datetime.now()}
    table_data = {"status": "Trống"}
    
    # WHEN: Thực hiện check-in
    success, msg = service.execute_checkin(booking_data, table_data)

    # THEN: Kiểm tra kết quả
    print(f"Kết quả: {msg} | Trạng thái bàn: {table_data['status']}")
    