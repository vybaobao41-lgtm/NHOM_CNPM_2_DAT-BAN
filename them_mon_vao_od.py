# Dữ liệu mẫu đại diện cho Menu và Order hiện tại
menu = {
    "M01": {"ten": "Phở Bò", "gia": 50000, "trang_thai": "con_hang"},
    "M02": {"ten": "Cà Phê Muối", "gia": 35000, "trang_thai": "het_mon"},  # Món bị hết/ẩn
    "M03": {"ten": "Trà Chanh", "gia": 20000, "trang_thai": "con_hang"}
}

# Đơn hàng hiện tại của bàn (Mã món: Số lượng)
order_hien_tai = {
    "M01": 1  # Đã có sẵn 1 Phở Bò trong order
}

def them_mon_vao_order(ma_mon):
    # Lấy thông tin món từ menu
    mon = menu.get(ma_mon)

    # 1. Kiểm tra món có tồn tại không
    if not mon:
        print(f"❌ Lỗi: Mã món {ma_mon} không tồn tại trong hệ thống.")
        return

    # AC-03: Không cho phép thêm món đang bị ẩn/hết món
    if mon["trang_thai"] == "het_mon":
        print(f"🚫 AC-03: Không thể thêm '{mon['ten']}'. Lý do: Món đã hết hoặc bị ẩn.")
        return

    # 2. Xử lý logic thêm món
    if ma_mon in order_hien_tai:
        # AC-02: Nếu món đã tồn tại thì tăng số lượng
        order_hien_tai[ma_mon] += 1
        print(f"🔄 AC-02: Món '{mon['ten']}' đã có. Tăng số lượng lên: {order_hien_tai[ma_mon]}")
    else:
        # AC-01: Thêm món mới với số lượng mặc định là 1
        order_hien_tai[ma_mon] = 1
        print(f"✅ AC-01: Đã thêm mới món '{mon['ten']}' vào đơn hàng.")

    # Hiển thị lại đơn hàng sau khi cập nhật
    print(f"📊 Đơn hàng hiện tại: {order_hien_tai}")

# --- CHẠY THỬ NGHIỆM ĐỂ KIỂM TRA CHECKLIST ---
print("--- THỬ NGHIỆM TÍNH NĂNG THÊM MÓN ---")

# Thử thêm món mới hoàn toàn (Trà Chanh)
them_mon_vao_order("M03") 

# Thử thêm món đã có sẵn để xem số lượng tăng (Phở Bò)
them_mon_vao_order("M01") 

# Thử thêm món đã hết hàng/bị ẩn (Cà Phê Muối)
them_mon_vao_order("M02")