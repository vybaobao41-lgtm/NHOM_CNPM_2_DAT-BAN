import json
import os

# Đường dẫn đến file dữ liệu
DB_FILE = 'menufinal.json' 

def doc_thuc_don():
    """Đọc dữ liệu từ file JSON"""
    if not os.path.exists(DB_FILE):
        print(f"❌ Lỗi: Không tìm thấy file {DB_FILE}")
        return []
    with open(DB_FILE, 'r', encoding='utf-8') as f:
        return json.load(f)

# Đơn hàng hiện tại của bàn (Mã món: Số lượng)
order_hien_tai = {}

def them_mon_vao_order(ma_mon_nhap):
    """
    Thực hiện chức năng thêm món vào đơn hàng dựa trên ID.
    Tuân thủ các tiêu chí chấp nhận (AC).
    """
    thuc_don = doc_thuc_don()
    
    # Tìm thông tin chi tiết của món dựa trên ID
    mon_tim_thay = next((item for item in thuc_don if item['id'] == ma_mon_nhap), None)

    # --- KIỂM TRA ĐIỀU KIỆN ---

    # 1. Kiểm tra mã món tồn tại trong thực đơn
    if not mon_tim_thay:
        print(f"❌ Lỗi: Mã món '{ma_mon_nhap}' không tồn tại trong hệ thống.")
        return

    # 2. AC-03: Không cho phép thêm món có trạng thái là "Hết hàng"
    if mon_tim_thay["trang_thai"] == "Hết hàng":
        print(f"🚫 AC-03: Món '{mon_tim_thay['ten']}' hiện đang hết hàng. Không thể thêm vào đơn!")
        return

    # --- XỬ LÝ LOGIC THÊM MÓN ---

    if ma_mon_nhap in order_hien_tai:
        # AC-02: Nếu món đã có trong đơn hàng, tăng số lượng lên 1
        order_hien_tai[ma_mon_nhap] += 1
        print(f"🔄 AC-02: Tăng số lượng '{mon_tim_thay['ten']}' lên: {order_hien_tai[ma_mon_nhap]}")
    else:
        # AC-01: Nếu món chưa có, thêm mới vào đơn hàng với số lượng mặc định là 1
        order_hien_tai[ma_mon_nhap] = 1
        print(f"✅ AC-01: Đã thêm mới món '{mon_tim_thay['ten']}' vào đơn hàng.")

    # --- KẾT QUẢ ---
    print(f"📊 Đơn hàng hiện tại (Mã: SL): {order_hien_tai}")

def hoan_thanh_order():
    """Hiển thị danh sách cuối cùng sau khi hoàn thành chọn món"""
    print("\n" + "="*30)
    print("✨ ĐÃ HOÀN THÀNH ORDER ✨")
    if not order_hien_tai:
        print("Đơn hàng chưa có món nào.")
    else:
        thuc_don = doc_thuc_don()
        for ma_mon, so_luong in order_hien_tai.items():
            mon = next((m for m in thuc_don if m['id'] == ma_mon), None)
            print(f"- {mon['ten']} (Mã: {ma_mon}): {so_luong} món")
    print("="*30)

# --- CHẠY THỬ NGHIỆM ---
if __name__ == "__main__":
    print("--- QUY TRÌNH THÊM MÓN VÀO ĐƠN HÀNG ---")
    
    # Thử nghiệm các kịch bản theo AC
    while True:
        cmd = input("\nNhập mã món (VD: TM002, MC002) hoặc 'DONE' để hoàn thành: ").upper()
        
        if cmd == 'DONE':
            hoan_thanh_order()
            break
        else:
            them_mon_vao_order(cmd)