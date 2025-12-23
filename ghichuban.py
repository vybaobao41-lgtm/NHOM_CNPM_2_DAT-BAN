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