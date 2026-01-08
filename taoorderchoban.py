import datetime

class Order:
    def __init__(self, ma_ban):
        # AC-04: Gán đúng thông tin bàn cho order
        self.ma_ban = ma_ban
        # AC-05: Thời điểm bắt đầu order
        self.thoi_gian_bat_dau = datetime.datetime.now()
        # AC-06: Order mới ở trạng thái ban đầu
        self.trang_thai = "Mới tạo"
        self.ma_don_hang = f"DH-{ma_ban}-{self.thoi_gian_bat_dau.strftime('%H%M%S')}"

class OrderSystem:
    def __init__(self):
        # Dữ liệu mẫu để phục vụ demo các AC
        self.danh_sach_ban = {
            "1": "Trống",          # Demo AC-01
            "2": "Đã đặt trước",   # Demo AC-02
            "3": "Đang ngồi"       # Demo AC-03
        }
        self.active_orders = {}

    # --- CÁC HÀM XỬ LÝ THEO TỪNG AC ---

    def ac01_tao_order_ban_trong(self, ma_ban):
        """Tạo order thành công cho bàn trống"""
        if self.danh_sach_ban.get(ma_ban) == "Trống":
            self.thuc_thi_tao_order(ma_ban)
            return f"✅ [AC-01] Thành công: Đã tạo order cho bàn trống số {ma_ban}."
        return "❌ [AC-01] Thất bại: Bàn không phải bàn trống."

    def ac02_tao_order_ban_dat_truoc(self, ma_ban):
        """Tạo order cho bàn đã đặt trước"""
        if self.danh_sach_ban.get(ma_ban) == "Đã đặt trước":
            self.thuc_thi_tao_order(ma_ban)
            return f"✅ [AC-02] Thành công: Đã tạo order cho bàn đặt trước số {ma_ban}."
        return "❌ [AC-02] Thất bại: Bàn không ở trạng thái đặt trước."

    def ac03_kiem_tra_order_trung(self, ma_ban):
        """Không cho phép tạo nhiều order đồng thời"""
        if self.danh_sach_ban.get(ma_ban) == "Đang ngồi":
            return f"❌ [AC-03] Lỗi: Bàn {ma_ban} đang có khách, không thể tạo thêm order!"
        return "ℹ️ [AC-03] Bàn này có thể tạo order."

    def ac07_hien_thi_order(self, ma_ban):
        """Hiển thị order trên hệ thống"""
        order = self.active_orders.get(ma_ban)
        if order:
            print(f"\n--- [AC-07] HIỂN THỊ THÔNG TIN ORDER ---")
            print(f"Mã đơn: {order.ma_don_hang}")
            print(f"Bàn: {order.ma_ban} (AC-04)")
            print(f"Bắt đầu: {order.thoi_gian_bat_dau.strftime('%H:%M:%S')} (AC-05)")
            print(f"Trạng thái: {order.trang_thai} (AC-06)")
            return "✅ [AC-07] Đã hiển thị."
        return "❌ [AC-07] Không tìm thấy order để hiển thị."

    def ac08_xu_ly_loi_he_thong(self, ma_ban):
        """Xử lý lỗi hệ thống (nhập sai bàn)"""
        if ma_ban not in self.danh_sach_ban:
            return f"❌ [AC-08] LỖI HỆ THỐNG: Bàn số {ma_ban} không tồn tại!"
        return "✅ [AC-08] Mã bàn hợp lệ."

    def thuc_thi_tao_order(self, ma_ban):
        """Hàm dùng chung để khởi tạo đối tượng Order"""
        moi_don = Order(ma_ban)
        self.active_orders[ma_ban] = moi_don
        self.danh_sach_ban[ma_ban] = "Đang ngồi"

# --- GIAO DIỆN ĐIỀU KHIỂN (MENU 8 MỤC) ---
def menu():
    he_thong = OrderSystem()
    
    while True:
        print("\n" + "="*50)
        print(f"{'QUẢN LÝ TẠO ORDER - 8 AC':^50}")
        print("="*50)
        print(f"Trạng thái bàn: {he_thong.danh_sach_ban}")
        print("-" * 50)
        print("1. Tạo order cho bàn TRỐNG")
        print("2. Tạo order cho bàn ĐÃ ĐẶT TRƯỚC")
        print("3. Kiểm tra lỗi tạo nhiều order đồng thời")
        print("4. Kiểm tra Gán đúng mã bàn cho order")
        print("5. Kiểm tra Thời điểm bắt đầu (Giờ hệ thống)")
        print("6. Kiểm tra Trạng thái ban đầu (Mới tạo)")
        print("7. Hiển thị chi tiết order lên hệ thống")
        print("8. Kiểm tra Xử lý lỗi hệ thống (Mã bàn sai)")
        print("0. Thoát")
        
        lua_chon = input("\nChọn mục kiểm tra (0-8): ").strip()

        if lua_chon == "1":
            ma = input("Nhập mã bàn trống (Gợi ý: 1): ")
            print(he_thong.ac01_tao_order_ban_trong(ma))
        
        elif lua_chon == "2":
            ma = input("Nhập mã bàn đặt trước (Gợi ý: 2): ")
            print(he_thong.ac02_tao_order_ban_dat_truoc(ma))
        
        elif lua_chon == "3":
            ma = input("Nhập mã bàn đang ngồi (Gợi ý: 3): ")
            print(he_thong.ac03_kiem_tra_order_trung(ma))
            
        elif lua_chon in ["4", "5", "6", "7"]:
            ma = input("Nhập mã bàn đã có order để xem chi tiết: ")
            print(he_thong.ac07_hien_thi_order(ma))
            print(f"(Mục {lua_chon} đã được tích hợp hiển thị ở trên)")
            
        elif lua_chon == "8":
            ma = input("Nhập mã bàn không tồn tại (Ví dụ: 99): ")
            print(he_thong.ac08_xu_ly_loi_he_thong(ma))
            
        elif lua_chon == "0":
            break
        else:
            print("Lựa chọn không hợp lệ!")

if __name__ == "__main__":
    menu()