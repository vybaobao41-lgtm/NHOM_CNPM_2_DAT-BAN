import json

FILE = "menufinal.json" 

# =======================
# HÀM TIỆN ÍCH
# =======================
def get_value(item, *keys):
    for k in keys:
        if k in item:
            return item[k]
    return None

def is_con_hang(item):
    # Kiểm tra nếu món còn hàng
    value = get_value(item, "trang_thai", "status", "available")
    return value == "Còn hàng"

def set_het_hang(item):
    # Cập nhật món thành Hết hàng
    if "trang_thai" in item:
        item["trang_thai"] = "Hết hàng"
    elif "status" in item:
        item["status"] = "Hết hàng"
    else:
        item["trang_thai"] = "Hết hàng"

# =======================
# ĐỌC / GHI FILE
# =======================
def load_menu():
    try:
        with open(FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        print(f"⚠ File {FILE} bị lỗi JSON. Tạo menu trống...")
        return []

def save_menu(menu):
    with open(FILE, "w", encoding="utf-8") as f:
        json.dump(menu, f, ensure_ascii=False, indent=2)

# =======================
# 1. BẾP: CẬP NHẬT MÓN HẾT
# =======================
def bep_cap_nhat_mon_het(menu):
    print("\n--- BẾP CẬP NHẬT MÓN HẾT HÀNG ---\n")
    con_hang = [m for m in menu if is_con_hang(m)]
    if not con_hang:
        print("⚠ Không còn món nào đang CÒN HÀNG.")
        return
    for m in con_hang:
        print(f'{get_value(m,"id")} - {get_value(m,"ten")} ({get_value(m,"danh_muc")})')
    ids = input("\nNhập ID các món hết hoặc Enter: ").strip()
    if not ids:
        print("✔ Không cập nhật món nào.")
        return
    ids = [i.strip() for i in ids.split(",")]
    for m in menu:
        if get_value(m,"id") in ids and is_con_hang(m):
            set_het_hang(m)
            print(f"✔ Đã ẩn: {get_value(m,'ten')}")
    save_menu(menu)

# =======================
# 2. PHỤC VỤ: XEM THỰC ĐƠN
# =======================
def phuc_vu_xem_thuc_don(menu):
    print("\n--- THỰC ĐƠN PHỤC VỤ ---\n")
    if not menu:
        print("⚠ Menu đang trống. Vui lòng kiểm tra menufinal.json")
        return
    for m in menu:
        if is_con_hang(m):
            print(f'{get_value(m,"ten")} - {get_value(m,"gia")}đ')

# =======================
# 3. BẾP: XEM QUẢN LÝ
# =======================
def bep_xem_quan_ly(menu):
    print("\n--- QUẢN LÝ THỰC ĐƠN (BẾP) ---\n")
    if not menu:
        print("⚠ Menu đang trống. Vui lòng kiểm tra menufinal.json")
        return
    for m in menu:
        trang_thai = "Còn hàng" if is_con_hang(m) else "Hết hàng"
        print(f'{get_value(m,"id")} - {get_value(m,"ten")} : {trang_thai}')

# =======================
# MENU CHÍNH
# =======================
def main():
    menu = load_menu()
    while True:
        print("\n===== HỆ THỐNG QUẢN LÝ THỰC ĐƠN =====")
        print("1. Bếp: Cập nhật món hết hàng")
        print("2. Phục vụ: Xem thực đơn")
        print("3. Bếp: Xem danh sách quản lý món")
        print("0. Thoát")
        chon = input("Chọn chức năng: ").strip()
        if chon=="1":
            bep_cap_nhat_mon_het(menu)
        elif chon=="2":
            phuc_vu_xem_thuc_don(menu)
        elif chon=="3":
            bep_xem_quan_ly(menu)
        elif chon=="0":
            print("👋 Thoát chương trình.")
            break
        else:
            print("❌ Lựa chọn không hợp lệ.")

if __name__=="__main__":
    main()
