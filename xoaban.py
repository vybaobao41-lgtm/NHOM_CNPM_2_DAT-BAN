from tkinter import messagebox

# AC-01: Hiển thị giao diện (Hàm này sẽ được gọi từ màn hình quản lý chính)
def hien_thi_giao_dien_xoa():
    print("--- UI: Nút [Xóa bàn] đã sẵn sàng ---")

# AC-02: Logic kiểm tra trạng thái
def kiem_tra_truoc_khi_xoa(id_ban, trang_thai):
    if trang_thai == "Trống":
        return True
    else:
        # Hiển thị thông báo lỗi phù hợp (AC-02)
        messagebox.showerror("Lỗi", f"Không thể xóa bàn {id_ban} vì đang ở trạng thái [{trang_thai}]!")
        return False

# AC-03 & AC-04: Hộp thoại xác nhận
def khi_nhan_nut_xoa(id_ban, trang_thai):
    # Bước 1: Gọi AC-02 để validate
    if kiem_tra_truoc_khi_xoa(id_ban, trang_thai):
        
        # Bước 2: Hiển thị popup xác nhận (AC-03)
        xac_nhan = messagebox.askyesno("Xác nhận xóa", 
                                       f"Bàn {id_ban} đang trống. Bạn có chắc chắn muốn xóa khỏi hệ thống?")
        
        if xac_nhan: # Người dùng chọn "Xác nhận"
            print(f"Hệ thống: Bắt đầu xử lý xóa bàn {id_ban}...")
            # Đây là nơi sẽ viết code cho AC-05 (Xóa Database)
        else: # AC-04: Người dùng chọn "Hủy"
            print("Hành động bị hủy: Popup đóng lại, dữ liệu giữ nguyên.")

if __name__ == "__main__":
    # Test case giả lập để bạn chạy thử file này ngay lập tức
    hien_thi_giao_dien_xoa()
    
    print("\n--- Chạy thử: Bàn đang có khách (AC-02) ---")
    khi_nhan_nut_xoa(101, "Đang phục vụ")
    
    print("\n--- Chạy thử: Bàn trống (AC-03 & AC-04) ---")
    khi_nhan_nut_xoa(102, "Trống")