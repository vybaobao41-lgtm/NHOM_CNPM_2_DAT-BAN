# Dữ liệu mô phỏng theo yêu cầu
dat_ban = {
    "DB001": {"trang_thai": "Chưa check-in", "ma_ban": "B10"},
    "DB002": {"trang_thai": "Đã check-in", "ma_ban": "B11"},
    "DB003": {"trang_thai": "Đã hủy", "ma_ban": None}
}

trang_thai_ban = {"B10": "Đã gán", "B11": "Đã gán"}

def xu_ly_huy_ban(ma_don):
    # 1. Kiểm tra đơn tồn tại
    if ma_don not in dat_ban:
        print(f"❌ Không tìm thấy mã đơn: {ma_don}")
        return

    don = dat_ban[ma_don]

    # AC01: Không cho phép hủy khi đã check-in
    if don["trang_thai"] == "Đã check-in":
        print(f"🛑 AC01: Đơn {ma_don} đã CHECK-IN. Không thể hủy!")
        return

    # Kiểm tra nếu đơn đã hủy rồi
    if don["trang_thai"] == "Đã hủy":
        print(f"ℹ️ Đơn {ma_don} đã được hủy trước đó.")
        return

    # AC02: Xác nhận trước khi hủy
    xac_nhan = input(f"❓ Bạn có chắc chắn muốn hủy đơn {ma_don}? (y/n): ")
    
    if xac_nhan.lower() == 'y':
        # Cập nhật trạng thái thành "Đã hủy"
        don["trang_thai"] = "Đã hủy"
        
        # Nếu có gán bàn, chuyển trạng thái bàn về "Trống"
        ma_ban = don["ma_ban"]
        if ma_ban in trang_thai_ban:
            trang_thai_ban[ma_ban] = "Trống"
            print(f"🔓 Bàn {ma_ban} đã được chuyển về trạng thái Trống.")

        # AC03: Thông báo thành công
        print(f"✅ AC03: Hủy đặt bàn {ma_don} THÀNH CÔNG!")
        
        # AC04: Hiển thị danh sách cập nhật
        print(f"📋 AC04 - Danh sách mới: {ma_don} -> {don['trang_thai']}")
    else:
        print("❌ Hủy bỏ thao tác.")

# Chạy thử nghiệm
xu_ly_huy_ban("DB001")