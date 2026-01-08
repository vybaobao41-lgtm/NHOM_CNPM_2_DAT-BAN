import json

FILE = "menufinal.json"

# =======================
# HÀM TIỆN ÍCH
# =======================
def load_menu():
    try:
        with open(FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        print(f"⚠ File {FILE} bị lỗi hoặc chưa tồn tại. Tạo menu trống...")
        return []

def save_menu(menu):
    with open(FILE, "w", encoding="utf-8") as f:
        json.dump(menu, f, ensure_ascii=False, indent=2)

def is_valid_input(ten_mon, gia, danh_muc):
    if not ten_mon.strip():
        return False, "❌ Tên món không được để trống"
    if not gia.strip():
        return False, "❌ Giá không được để trống"
    if not danh_muc.strip():
        return False, "❌ Danh mục không được để trống"
    return True, ""

def is_valid_price(gia):
    if not gia.isdigit():
        return False, "❌ Giá phải là số"
    if int(gia) <= 0:
        return False, "❌ Giá phải lớn hơn 0"
    return True, ""

# =======================
# CHỨC NĂNG
# =======================
def them_mon(menu):
    print("\n--- THÊM MÓN MỚI ---")
    
    # Nhập số lượng món muốn thêm
    so_luong = input("Nhập số lượng món muốn thêm: ").strip()
    if not so_luong.isdigit() or int(so_luong) <= 0:
        print("❌ Số lượng phải là số nguyên lớn hơn 0")
        return
    so_luong = int(so_luong)
    
    for _ in range(so_luong):
        ten_mon = input("Nhập tên món: ")
        gia = input("Nhập giá: ")
        danh_muc = input("Nhập danh mục: ")

        hop_le, thong_bao = is_valid_input(ten_mon, gia, danh_muc)
        if not hop_le:
            print(thong_bao)
            continue

        hop_le, thong_bao = is_valid_price(gia)
        if not hop_le:
            print(thong_bao)
            continue

        # Tạo ID tự động
        last_id = max([int(m['id'][2:]) for m in menu if m['id'][2:].isdigit()], default=0)
        prefix = danh_muc[:2].upper()  # Lấy 2 chữ cái đầu danh mục làm prefix
        ma_mon = f"{prefix}{str(last_id+1).zfill(3)}"

        mon_moi = {
            "id": ma_mon,
            "ten": ten_mon,
            "gia": int(gia),
            "danh_muc": danh_muc,
            "trang_thai": "Còn hàng"
        }
        menu.append(mon_moi)
        print(f"✔ Thêm món thành công: {ten_mon} ({ma_mon})")

    save_menu(menu)

def hien_thi_menu(menu):
    print("\n--- DANH SÁCH MÓN ĂN ---")
    if not menu:
        print("📭 Menu hiện đang trống")
        return
    for i, mon in enumerate(menu, start=1):
        print(f"{i}. {mon['ten']} - {mon['gia']}đ - {mon['danh_muc']} - {mon['trang_thai']}")

# =======================
# MENU CHÍNH
# =======================
def main():
    menu = load_menu()
    while True:
        print("\n===== QUẢN LÝ THỰC ĐƠN =====")
        print("1. Thêm món mới")
        print("2. Hiển thị thực đơn")
        print("0. Thoát")
        chon = input("Chọn chức năng: ").strip()

        if chon == "1":
            them_mon(menu)
        elif chon == "2":
            hien_thi_menu(menu)
        elif chon == "0":
            print("👋 Thoát chương trình.")
            break
        else:
            print("❌ Lựa chọn không hợp lệ.")

if __name__ == "__main__":
    main()
