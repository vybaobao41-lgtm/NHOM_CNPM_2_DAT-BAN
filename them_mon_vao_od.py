import json
import os

DB_FILE = 'menufinal.json'
ORDER_FILE = 'order.json'

# --- đọc menu ---
def doc_thuc_don():
    if not os.path.exists(DB_FILE):
        print(f"❌ Không tìm thấy file {DB_FILE}")
        return []
    with open(DB_FILE, 'r', encoding='utf-8') as f:
        return json.load(f)

# --- đọc order ---
def doc_order():
    if not os.path.exists(ORDER_FILE):
        return {}
    with open(ORDER_FILE, 'r', encoding='utf-8') as f:
        data = json.load(f)
        if isinstance(data, list):
            return {}
        return data

# --- ghi order ---
def ghi_order(order):
    with open(ORDER_FILE, 'w', encoding='utf-8') as f:
        json.dump(order, f, ensure_ascii=False, indent=4)

# --- thêm món ---
def them_mon(ma_mon):
    thuc_don = doc_thuc_don()
    order = doc_order()

    mon = next((m for m in thuc_don if m['id'] == ma_mon), None)
    if not mon:
        print(f"❌ Mã món {ma_mon} không tồn tại")
        return
    if mon['trang_thai'] == "Hết hàng":
        print(f"🚫 Món {mon['ten']} hiện hết hàng")
        return

    if ma_mon in order:
        order[ma_mon]['so_luong'] += 1
        print(f"🔄 Tăng số lượng {mon['ten']} lên {order[ma_mon]['so_luong']}")
    else:
        order[ma_mon] = {
            "ten": mon['ten'],
            "gia": mon['gia'],
            "so_luong": 1
        }
        print(f"✅ Thêm món {mon['ten']} vào order")

    ghi_order(order)

# --- hiển thị order ---
def hien_thi_order():
    order = doc_order()
    if not order:
        print("🛒 Order trống")
        return
    print("\n=== Order hiện tại ===")
    for ma_mon, chi_tiet in order.items():
        print(f"- ID: {ma_mon} | Tên món: {chi_tiet['ten']} | Giá: {chi_tiet['gia']} | SL: {chi_tiet['so_luong']}")
    print("=====================")

# --- chạy thử ---
if __name__ == "__main__":
    while True:
        cmd = input("Nhập mã món (hoặc DONE để kết thúc): ").upper()
        if cmd == "DONE":
            hien_thi_order()
            break
        them_mon(cmd)
