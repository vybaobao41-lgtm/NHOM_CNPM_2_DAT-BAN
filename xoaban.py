# AC-01: Hiển thị nút Xóa và gắn sự kiện click
def hien_thi_giao_dien_xoa():
    print("--- UI: Đang hiển thị nút [Xóa bàn] trên màn hình quản lý ---")

def khi_nhan_nut_xoa(id_ban):
    print(f"--- Event: Quản lý đã nhấn vào nút xóa bàn số {id_ban} ---")

if __name__ == "__main__":
    # Giả lập chạy tính năng
    hien_thi_giao_dien_xoa()
    khi_nhan_nut_xoa(101)
    # Kế thừa AC-01: Hiển thị giao diện
def hien_thi_giao_dien_xoa():
    print("--- UI: Đang hiển thị nút [Xóa bàn] trên màn hình quản lý ---")

# AC-02: Logic kiểm tra trạng thái (Business Rule)
def kiem_tra_truoc_khi_xoa(id_ban, trang_thai):
    print(f"Hệ thống đang kiểm tra trạng thái bàn số {id_ban}...")
    
    # Chỉ cho phép xóa nếu bàn ở trạng thái "Trống"
    if trang_thai == "Trống":
        print(f"Hợp lệ: Bàn {id_ban} đang Trống. Bạn có thể xóa.")
        return True
    else:
        # Hiển thị thông báo lỗi phù hợp như yêu cầu AC-02
        print(f"Lỗi: Không thể xóa bàn {id_ban} vì đang ở trạng thái [{trang_thai}]!")
        return False

if __name__ == "__main__":
    hien_thi_giao_dien_xoa()
    
    # Giả lập 2 trường hợp để test logic AC-02
    print("\n--- Test case 1: Bàn đang có khách ---")
    kiem_tra_truoc_khi_xoa(101, "Đang phục vụ")
    
    print("\n--- Test case 2: Bàn đang trống ---")
    kiem_tra_truoc_khi_xoa(102, "Trống")
    