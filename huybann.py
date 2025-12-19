# Khai báo dữ liệu mẫu để kiểm tra
dat_ban = {
    "DB001": "Đã đặt",
    "DB002": "Đã check-in"
}

def kiem_tra_hien_thi_nut_huy(ma_dat_ban):
    trang_thai = dat_ban.get(ma_dat_ban)
    
    # AC-01 & AC-02: Kiểm tra điều kiện hiển thị
    if trang_thai == "Đã check-in":
        print(f"[{ma_dat_ban}] Trạng thái: {trang_thai}")
        print("KẾT QUẢ: Nút 'Hủy đặt bàn' bị ẨN/VÔ HIỆU HÓA.")
        print("THÔNG BÁO: Không thể hủy đặt bàn đã check-in.")
        return False
    else:
        print(f"[{ma_dat_ban}] Trạng thái: {trang_thai}")
        print("KẾT QUẢ: Nút 'Hủy đặt bàn' HIỂN THỊ và có thể nhấn.")
        return True

def xac_nhan_huy():
    # AC-03: Yêu cầu xác nhận khi nhấn nút
    print("\n--- HỘP THOẠI XÁC NHẬN ---")
    print("Bạn có chắc chắn muốn hủy không?")
    print("1. Xác nhận")
    print("2. Hủy bỏ")
    lua_chon = input("Chọn (1/2): ")
    
    if lua_chon == "1":
        print("Hệ thống: Đang chuyển sang bước tiếp theo...")
        return True
    else:
        print("Hệ thống: Chưa có thay đổi dữ liệu nào xảy ra.")
        return False

# Chạy thử
if __name__ == "__main__":
    ma_id = "DB001" # Thử thay bằng DB002 để xem AC-02
    if kiem_tra_hien_thi_nut_huy(ma_id):
        xac_nhan_huy()