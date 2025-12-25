import datetime

class DonHang:
    def __init__(self, ma_ban):
        # AC-04, AC-05, AC-06: Khởi tạo thông tin Đơn hàng (Order)
        self.ma_don_hang = f"DH-{ma_ban}-{datetime.datetime.now().strftime('%H%M%S')}"
        self.ma_ban = ma_ban
        self.thoi_gian_bat_dau = datetime.datetime.now()
        self.trang_thai = "Mới tạo"  # Trạng thái ban đầu

    def hien_thi_thong_tin(self):
        # AC-07: Hiển thị thông tin đơn hàng lên hệ thống
        print(f"  + Mã đơn: {self.ma_don_hang}")
        print(f"  + Bắt đầu lúc: {self.thoi_gian_bat_dau.strftime('%H:%M:%S %d/%m/%Y')}")
        print(f"  + Trạng thái đơn: {self.trang_thai}")

class BanAn:
    def __init__(self, ma_ban, trang_thai_dau="Trống"):
        self.ma_ban = ma_ban
        self.trang_thai = trang_thai_dau  # Trống, Đã đặt, Đang ngồi
        self.don_hang_hien_tai = None

class QuanLyNhaHang:
    def __init__(self):
        # Khởi tạo danh sách bàn theo yêu cầu của bạn (Tiếng Việt hoàn toàn)
        self.danh_sach_ban = {
            "1": BanAn("1", "Trống"),
            "2": BanAn("2", "Đã đặt"),
            "3": BanAn("3", "Đang ngồi") # Bàn này để test trường hợp đã có khách
        }

    def tao_don_hang(self):
        print("\n--- [CHỨC NĂNG TẠO ORDER MỚI] ---")
        ma_so_ban = input("Nhập số bàn muốn phục vụ: ").strip()

        # AC-08: Kiểm tra lỗi nhập liệu hoặc bàn không tồn tại
        if ma_so_ban not in self.danh_sach_ban:
            print(f"❌ LỖI: Bàn số {ma_so_ban} không tồn tại!")
            return

        ban_dang_chon = self.danh_sach_ban[ma_so_ban]

        # AC-03: Mỗi bàn chỉ có một đơn hàng đang mở
        if ban_dang_chon.trang_thai == "Đang ngồi":
            print(f"❌ LỖI: Bàn {ma_so_ban} đang có khách và đơn hàng chưa đóng!")
            return

        # Thực hiện tạo đơn (Xử lý AC-01, AC-02)
        try:
            moi_don = DonHang(ma_so_ban)
            ban_dang_chon.don_hang_hien_tai = moi_don
            ban_dang_chon.trang_thai = "Đang ngồi"
            
            print("✅ TẠO ĐƠN HÀNG THÀNH CÔNG!")
            moi_don.hien_thi_thong_tin() # AC-07
        except Exception as e:
            print(f"❌ LỖI HỆ THỐNG: {e}") # AC-08

    def menu_chinh(self):
        while True:
            print("\n" + "="*35)
            print("   HỆ THỐNG QUẢN LÝ ĐẶT BÀN")
            print("="*35)
            print("1. Xem danh sách và trạng thái bàn")
            print("2. Tạo đơn hàng mới (Order)")
            print("3. Thoát chương trình")
            lua_chon = input("Mời chọn chức năng (1-3): ")

            if lua_chon == "1":
                print("\nTRẠNG THÁI CÁC BÀN HIỆN TẠI:")
                for ma, ban in self.danh_sach_ban.items():
                    print(f"  - Bàn {ma}: {ban.trang_thai}")
            elif lua_chon == "2":
                self.tao_don_hang()
            elif lua_chon == "3":
                print("👋 Đang đóng hệ thống... Tạm biệt!")
                break
            else:
                print("⚠️ Lựa chọn không hợp lệ, vui lòng nhập lại!")

if __name__ == "__main__":
    ung_dung = QuanLyNhaHang()
    ung_dung.menu_chinh()