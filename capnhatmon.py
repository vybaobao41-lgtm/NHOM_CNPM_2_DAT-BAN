import json

FILE = "menufinal.json"

# =======================
# TIỆN ÍCH
# =======================
def load_menu():
    try:
        with open(FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        print("⚠ Không đọc được menufinal.json – tạo menu trống")
        return []

def save_menu(menu):
    with open(FILE, "w", encoding="utf-8") as f:
        json.dump(menu, f, ensure_ascii=False, indent=2)

# =======================
# HIỂN THỊ MENU
# =======================
def hien_thi_menu(menu):
    print("\n--- DANH SÁCH THỰC ĐƠN ---")
    if not menu:
        print("📭 Thực đơn trống")
        return

    for i, mon in enumerate(menu, start=1):
        print(
            f"{i}. {mon['ten']} | "
            f"{mon['gia']}đ | "
            f"{mon['danh_muc']} | "
            f"Số lượng: {mon.get('so_luong', 0)} | "
            f"{mon['trang_thai']}"
        )

# =======================
# KIỂM TRA HỢP LỆ
# =======================
def gia_hop_le(gia):
    if not gia.isdigit():
        print("❌ Giá phải là số")
        return None
    gia = int(gia)
    if gia <= 0:
        print("❌ Giá phải lớn hơn 0")
        return None
    return gia

def so_luong_hop_le(sl):
    if not sl.isdigit():
        print("❌ Số lượng phải là số")
        return None
    sl = int(sl)
    if sl < 0:
        print("❌ Số lượng không được âm")
        return None
    return sl

# =======================
# CẬP NHẬT MÓN
# =======================
def cap_nhat_mon(menu):
    hien_thi_menu(menu)
    if not menu:
        return

    try:
        chon = int(input("\nChọn số món cần cập nhật: ")) - 1
        mon = menu[chon]
    except:
        print("❌ Lựa chọn không hợp lệ")
        return

    print("\n--- NHẬP THÔNG TIN MỚI (Enter để giữ nguyên) ---")

    ten_moi = input(f"Tên ({mon['ten']}): ").strip()
    gia_moi = input(f"Giá ({mon['gia']}): ").strip()
    danh_muc_moi = input(f"Danh mục ({mon['danh_muc']}): ").strip()
    so_luong_moi = input(f"Số lượng ({mon.get('so_luong', 0)}): ").strip()
    trang_thai_moi = input(f"Trạng thái ({mon['trang_thai']}): ").strip()

    if ten_moi:
        mon["ten"] = ten_moi

    if gia_moi:
        gia = gia_hop_le(gia_moi)
        if gia is None:
            return
        mon["gia"] = gia

    if danh_muc_moi:
        mon["danh_muc"] = danh_muc_moi

    if so_luong_moi:
        sl = so_luong_hop_le(so_luong_moi)
        if sl is None:
            return
        mon["so_luong"] = sl

    if trang_thai_moi:
        mon["trang_thai"] = trang_thai_moi

    save_menu(menu)
    print("\n✅ Cập nhật món thành công!")

# =======================
# CHƯƠNG TRÌNH CHÍNH
# =======================
def main():
    menu = load_menu()
    while True:
        print("\n===== CẬP NHẬT MÓN ĂN =====")
        print("1. Hiển thị thực đơn")
        print("2. Cập nhật món")
        print("0. Thoát")

        chon = input("Chọn chức năng: ").strip()

        if chon == "1":
            hien_thi_menu(menu)
        elif chon == "2":
            cap_nhat_mon(menu)
        elif chon == "0":
            print("👋 Thoát chương trình")
            break
        else:
            print("❌ Lựa chọn không hợp lệ")

if __name__ == "__main__":
    main()
