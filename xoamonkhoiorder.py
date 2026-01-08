import json
import os

ORDER_FILE = 'order.json'

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

# --- xóa món ---
def xoa_mon(ma_mon):
    order = doc_order()
    if ma_mon not in order:
        print(f"❌ Mã món {ma_mon} không tồn tại trong order")
        return

    if order[ma_mon]['so_luong'] > 1:
        order[ma_mon]['so_luong'] -= 1
        print(f"🔽 Giảm 1 số lượng {order[ma_mon]['ten']} xuống {order[ma_mon]['so_luong']}")
    else:
        print(f"🗑️ Xóa món {order[ma_mon]['ten']} khỏi order")
        del order[ma_mon]

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
        cmd = input("Nhập mã món xóa (hoặc DONE để kết thúc): ").upper()
        if cmd == "DONE":
            hien_thi_order()
            break
        xoa_mon(cmd)
