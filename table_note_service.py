from datetime import datetime

class TableNoteService:
    def __init__(self):
        # AC-06: Giới hạn độ dài ghi chú (Khai báo trước để dùng bên dưới)
        self.MAX_NOTE_LENGTH = 200

    def execute_workflow(self, table, note_input):
        print(f"\n--- Thực hiện thao tác với Bàn {table['id']} ---")

        # AC-01: Thêm ghi chú & AC-03: Chỉnh sửa ghi chú
        # (Hai hành động này thực tế là một thao tác ghi đè nội dung)
        if note_input and 0 < len(note_input) <= self.MAX_NOTE_LENGTH:
            table['note'] = note_input.strip()
            print(f"[AC-01/03] Hệ thống đã lưu ghi chú: {table['note']}")

        # AC-04: Xóa ghi chú
        elif note_input == "":
            table['note'] = ""
            print("[AC-04] Ghi chú đã được xóa khỏi bàn")

        # AC-05: Không bắt buộc nhập ghi chú
        elif note_input is None:
            print("[AC-05] Không nhập ghi chú, hệ thống tiếp tục các thao tác khác")

        # AC-06: Giới hạn độ dài (Trường hợp vi phạm)
        if note_input and len(note_input) > self.MAX_NOTE_LENGTH:
            return False, f"[AC-06] Lỗi: Ghi chú vượt quá {self.MAX_NOTE_LENGTH} ký tự"

        # AC-02: Hiển thị ghi chú
        # (Logic này mô phỏng việc hệ thống trả dữ liệu ra màn hình)
        if table['note']:
            print(f"[AC-02] HIỂN THỊ: Ghi chú '{table['note']}' hiện rõ trên sơ đồ bàn")
        
        return True, "Thao tác hoàn tất"

    def checkout(self, amount):
        # AC-07: Ghi chú không ảnh hưởng đến hóa đơn
        print(f"[AC-07] Thanh toán: {amount}đ (Ghi chú không làm thay đổi giá tiền)")
        return amount

# --- MÔ PHỎNG KIỂM THỬ THEO THỨ TỰ AC ---
if __name__ == "__main__":
    service = TableNoteService()
    my_table = {"id": "05", "note": ""}

    # Test AC-01
    service.execute_workflow(my_table, "Khách ngồi chờ bạn")
    
    # Test AC-03
    service.execute_workflow(my_table, "Cập nhật: Khách muốn thêm đá")
    
    # Test AC-04
    service.execute_workflow(my_table, "")
    
    # Test AC-06
    success, error_msg = service.execute_workflow(my_table, "A" * 260)
    if not success: print(error_msg)
    
    # Test AC-07
    service.checkout(250000)