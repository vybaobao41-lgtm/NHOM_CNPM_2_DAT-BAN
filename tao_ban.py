# =========================
# Dữ liệu chung lưu thông tin bàn
# =========================
dat_ban = {}  # so_ban : {"trang_thai": "trống/đặt", "khach_hang": "", "sdt": "", "so_nguoi": 0}

# Khởi tạo bàn mặc định 1-100
for i in range(1, 101):
    dat_ban[i] = {"trang_thai": "trống", "khach_hang": "", "sdt": "", "so_nguoi": 0}

# =========================
# AC-01: Thêm bàn
# =========================
def ac01_them_ban():
    print("\n--- AC-01: Thêm bàn ---")
    
    # Tìm bàn trống nhỏ nhất chưa sử dụng
    for i in range(1, 1000):
        if i not in dat_ban:
            suggested_ban = i
            break
    else:
        print("❌ Không còn bàn trống để thêm!")
        return
    
    print(f"💡 Gợi ý số bàn mới: {suggested_ban}")
    so_ban_input = input(f"Nhập số bàn (Enter để dùng {suggested_ban}): ").strip()
    
    if so_ban_input == "":
        so_ban = suggested_ban
    else:
        # validate số bàn
        if not so_ban_input.isdigit():
            print("❌ Số bàn phải là số hợp lệ!")
            return
        so_ban = int(so_ban_input)
        if so_ban <= 0 or so_ban in dat_ban:
            print("❌ Số bàn không hợp lệ hoặc đã tồn tại!")
            return
    
    # Thêm bàn
    dat_ban[so_ban] = {"trang_thai": "trống", "khach_hang": "", "sdt": "", "so_nguoi": 0}
    print(f"✔ Thêm bàn số {so_ban} thành công!")
# =========================
# AC-02/03: Đặt bàn cho khách
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
    
    if so_ban in dat_ban and dat_ban[so_ban]["trang_thai"] == "đặt":
        print(f"⚠ Bàn số {so_ban} đã được đặt trước!")
        return
    
    dat_ban[so_ban] = {"trang_thai": "đặt", "khach_hang": ten_khach, "sdt": sdt_khach, "so_nguoi": so_nguoi}
    print(f"✔ Đặt bàn số {so_ban} cho {ten_khach} ({so_nguoi} khách) thành công!")
# =========================
# AC-04: Hiển thị sơ đồ bàn
# =========================
def hien_thi_so_do_ban():
    print("\n📌 Sơ đồ bàn hiện tại:")
    trong = [so_ban for so_ban, info in dat_ban.items() if info["trang_thai"] == "trống"]
    dat = [(so_ban, info) for so_ban, info in dat_ban.items() if info["trang_thai"] == "đặt"]
    
    if trong:
        print("🔹 Bàn trống:", ", ".join(map(str, trong)))
    else:
        print("🔹 Không còn bàn trống")
    
    if dat:
        print("🔸 Bàn đã đặt:")
        for b, info in dat:
            print(f" - Bàn {b}: Khách: {info['khach_hang']}, SĐT: {info['sdt']}, Số khách: {info['so_nguoi']}")
