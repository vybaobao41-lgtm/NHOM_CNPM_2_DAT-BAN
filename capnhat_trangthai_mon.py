# Danh sách món ăn trong một đơn hàng mẫu
order_items = {
    "Phở Bò": "Chờ",
    "Cà Phê Muối": "Chờ"
}

def cap_nhat_che_bien(ten_mon, trang_thai_moi):
    if ten_mon in order_items:
        order_items[ten_mon] = trang_thai_moi
        # AC03: Thông báo trạng thái
        print(f"👨‍🍳 BẾP: Món '{ten_mon}' hiện có trạng thái: {trang_thai_moi}")
    else:
        print(f"❌ Không tìm thấy món '{ten_mon}' trong order.")

# --- CHẠY THỬ ---
# AC01: Bắt đầu làm món
cap_nhat_che_bien("Phở Bò", "Đang chuẩn bị")

# AC02: Nấu xong món
cap_nhat_che_bien("Phở Bò", "Đã xong")

print(f"📊 Danh sách order hiện tại: {order_items}")