import datetime

class TableNoteService:
    def __init__(self):
        # AC-06: Giới hạn độ dài ghi chú
        self.MAX_NOTE_LENGTH = 200
        # Dữ liệu bàn mặc định
        self.table = {"id": "05", "note": "", "trang_thai": "Trống"}

    def hien_thi_ban(self):
        print("\n" + "="*35)
        print(f"BÀN SỐ: {self.table['id']} | Trạng thái: {self.table['trang_thai']}")
        # AC-02: Hiển thị ghi chú (Nếu trống thì hiện thông báo)
        note_display = self.table['note'] if self.table['note'] else "(Không có ghi chú)"
        print(f"Ghi chú: {note_display}")
        print("="*35)

    def menu(self):
        print("--- HỆ THỐNG QUẢN LÝ GHI CHÚ BÀN ---")
        while True:
            self.hien_thi_ban()
            print("1. Thêm/Sửa ghi chú (AC-01/03)")
            print("2. Xóa ghi chú (AC-04)")
            print("3. Bỏ qua nhập ghi chú (AC-05)")
            print("4. Thanh toán (Kiểm tra AC-07)")
            print("5. Thoát")
            
            lua_chon = input("Chọn thao tác (1-5): ")

            if lua_chon == '1':
                # AC-01 & AC-03: Thêm và Chỉnh sửa
                print(f"Nhập nội dung (Tối đa {self.MAX_NOTE_LENGTH} ký tự):")
                note_input = input("> ")
                
                # AC-06: Kiểm tra độ dài
                if len(note_input) > self.MAX_NOTE_LENGTH:
                    print(f"!! LỖI: Ghi chú vượt quá {self.MAX_NOTE_LENGTH} ký tự.")
                else:
                    # Cập nhật ghi chú và loại bỏ khoảng trắng thừa ở 2 đầu
                    self.table['note'] = note_input.strip()
                    print(">> Hệ thống đã lưu ghi chú thành công.")

            elif lua_chon == '2':
                # AC-04: Xóa ghi chú
                if not self.table['note']:
                    print(">> Bàn hiện không có ghi chú để xóa.")
                else:
                    xac_nhan = input("Xác nhận xóa ghi chú? (y/n): ")
                    if xac_nhan.lower() == 'y':
                        self.table['note'] = ""
                        print(">> Đã xóa ghi chú.")

            elif lua_chon == '3':
                # AC-05: Không bắt buộc nhập ghi chú
                print(">> Đã bỏ qua phần ghi chú.")

            elif lua_chon == '4':
                # AC-07: Ghi chú không ảnh hưởng hóa đơn
                total = 250000
                print(f">> Hóa đơn bàn {self.table['id']}: {total:,}đ")
                print(">> Ghi chú không làm thay đổi giá tiền.")

            elif lua_chon == '5':
                break
            else:
                print("Lựa chọn không hợp lệ!")

if __name__ == "__main__":
    app = TableNoteService()
    app.menu()