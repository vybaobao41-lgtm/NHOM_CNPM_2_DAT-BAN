# =========================
# Dữ liệu chung lưu thông tin bàn
# =========================
dat_ban = {}  # so_ban : {"trang_thai": "trống/đặt", "khach_hang": "", "sdt": "", "so_nguoi": 0}

# Khởi tạo bàn mặc định
for i in range(1, 101):
    dat_ban[i] = {"trang_thai": "trống", "khach_hang": "", "sdt": "", "so_nguoi": 0}

# =========================
# AC-01: Thêm bàn thành công, không trùng số bàn
# =========================
def ac01_them_ban():
    print("\n--- AC-01: Thêm bàn ---")
    
    so_ban_input = input("Nhập số bàn: ").strip()
    
    try:
        so_ban = int(so_ban_input)
        if so_ban <= 0:
            print("❌ Số bàn phải > 0!")
            return
    except ValueError:
        print("❌ Số bàn phải là số hợp lệ!")
        return
    
    if so_ban in dat_ban:
        print(f"⚠ Bàn số {so_ban} đã tồn tại!")
        return
    
    dat_ban[so_ban] = {"trang_thai": "trống", "khach_hang": "", "sdt": "", "so_nguoi": 0}
    print(f"✔ Thêm bàn số {so_ban} thành công!")
    hien_thi_so_do_ban()

# =========================
# AC-02/AC-03: Đặt bàn cho khách với kiểm tra dữ liệu
# =========================
def ac02_03_dat_ban_khach():
    print("\n--- AC-02/AC-03: Đặt bàn cho khách ---")
    
    so_ban_input = input("Nhập số bàn: ").strip()
    ten_khach = input("Nhập tên khách: ").strip()
    sdt_khach = input("Nhập SĐT khách: ").strip()
    so_nguoi_input = input("Nhập số khách: ").strip()
    
    # Kiểm tra bắt buộc
    if so_ban_input == "" or ten_khach == "" or sdt_khach == "" or so_nguoi_input == "":
        print("❌ Vui lòng nhập đầy đủ thông tin!")
        return
    
    # Kiểm tra số bàn, số điện thoại, số khách hợp lệ
    if not so_ban_input.isdigit():
        print("❌ Số bàn phải là số!")
        return
    if not sdt_khach.isdigit():
        print("❌ Số điện thoại phải là số!")
        return
    if not so_nguoi_input.isdigit() or int(so_nguoi_input) <= 0:
        print("❌ Số khách không hợp lệ!")
        return
    
    so_ban = int(so_ban_input)
    so_nguoi = int(so_nguoi_input)
    
    if so_ban <= 0:
        print("❌ Số bàn phải > 0!")
        return
    
    if so_ban in dat_ban and dat_ban[so_ban]["trang_thai"] == "đặt":
        print(f"⚠ Bàn số {so_ban} đã được đặt trước!")
        return
    
    dat_ban[so_ban] = {"trang_thai": "đặt", "khach_hang": ten_khach, "sdt": sdt_khach, "so_nguoi": so_nguoi}
    print(f"✔ Đặt bàn số {so_ban} cho {ten_khach} ({so_nguoi} khách) thành công!")
    hien_thi_so_do_ban()

# =========================
# AC-04: Hiển thị sơ đồ bàn tự động
# =========================
def ac04_hien_thi_so_do():
    print("\n--- AC-04: Hiển thị sơ đồ bàn ---")
    if not dat_ban:
        print("⚠ Chưa có bàn nào!")
        return
    hien_thi_so_do_ban()

# =========================
# Hàm hiển thị chung (gọn)
# =========================
def hien_thi_so_do_ban():
    if not dat_ban:
        print("⚠ Chưa có bàn nào!")
        return
    
    # Phân loại bàn
    trong = [so_ban for so_ban, info in dat_ban.items() if info["trang_thai"] == "trống"]
    dat = [(so_ban, info["khach_hang"], info["sdt"], info["so_nguoi"]) for so_ban, info in dat_ban.items() if info["trang_thai"] == "đặt"]
    
    # Hiển thị tổng số bàn
    print("\n📌 Sơ đồ bàn hiện tại:")
    print(f"🔹 Số bàn trống: {len(trong)}")
    print(f"🔹 Số bàn đã đặt: {len(dat)}")
    
    # Chỉ hiển thị bàn đã đặt chi tiết
    if dat:
        print("Bàn đã đặt:")
        for b, khach, sdt, so_nguoi in dat:
            print(f" - Bàn số {b}: Khách: {khach} - SĐT: {sdt} - Số khách: {so_nguoi}")

# =========================
# Menu test trực tiếp
# =========================
if __name__ == "__main__":
    while True:
        print("\n===== TEST US-01: Tạo đặt bàn =====")
        print("1. AC-01: Thêm bàn")
        print("2. AC-02/AC-03: Đặt bàn cho khách")
        print("3. AC-04: Hiển thị sơ đồ bàn")
        print("0. Thoát")

        choice = input("Chọn chức năng: ").strip()

        if choice == "1":
            ac01_them_ban()
        elif choice == "2":
            ac02_03_dat_ban_khach()
        elif choice == "3":
            ac04_hien_thi_so_do()
        elif choice == "0":
            print("👋 Tạm biệt!")
            break
        else:
            print("❌ Lựa chọn không hợp lệ!")
