from tkinter import messagebox
import table_manager # Thêm để kết nối AC-05 và AC-06

# AC-01: Hiển thị giao diện
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

# AC-03, AC-04, AC-05 & AC-06
def khi_nhan_nut_xoa(id_ban, trang_thai):
    # Bước 1: Gọi AC-02 để validate
    if kiem_tra_truoc_khi_xoa(id_ban, trang_thai):
        
        # Bước 2: Hiển thị popup xác nhận (AC-03)
        xac_nhan = messagebox.askyesno("Xác nhận xóa", 
                                       f"Bàn {id_ban} đang trống. Bạn có chắc chắn muốn xóa khỏi hệ thống?")
        
        if xac_nhan: # Người dùng chọn "Xác nhận"
            print(f"Hệ thống: Bắt đầu xử lý xóa bàn {id_ban}...")
            
            # --- THỰC HIỆN AC-05: Xóa Database ---
            if table_manager.xoa_ban_khoi_db(id_ban):
                
                # --- THỰC HIỆN AC-06: Ghi Log ---
                table_manager.ghi_log_he_thong(id_ban, "Admin")
                
                print(f"Thành công: Bàn {id_ban} đã bị xóa và ghi log.")
                messagebox.showinfo("Thành công", f"Đã xóa bàn {id_ban} thành công!")
            else:
                messagebox.showerror("Lỗi", "Không thể xóa bàn khỏi cơ sở dữ liệu.")
                
        else: # AC-04: Người dùng chọn "Hủy"
            print("Hành động bị hủy: Popup đóng lại, dữ liệu giữ nguyên.")

if __name__ == "__main__":
    hien_thi_giao_dien_xoa()
    
    # Chạy thử bàn trống để kiểm tra luồng AC-03 -> AC-06
    khi_nhan_nut_xoa(102, "Trống")