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
