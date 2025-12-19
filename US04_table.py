import time
import threading
import os
import random

# ===============================
# DỮ LIỆU & HẰNG SỐ
# ===============================
STATUSES = ["TRỐNG", "ĐÃ ĐẶT", "ĐANG DÙNG"]
tables = []

# ===============================
# AC01 – NHẬP DỮ LIỆU BÀN TỪ PHÍM
# ===============================
def input_tables():
    print("📝 NHẬP DANH SÁCH BÀN (Enter tên bàn để kết thúc)\n")
    while True:
        name = input("Tên bàn: ")
        if not name:
            break

        capacity = int(input("Số chỗ: "))
        area = input("Khu vực: ")

        tables.append({
            "name": name,
            "capacity": capacity,
            "area": area,
            "status": "TRỐNG"
        })

# ===============================
# AC02 – CẬP NHẬT TRẠNG THÁI REALTIME
# ===============================
def realtime_update():
    while True:
        if tables:
            table = random.choice(tables)
            table["status"] = random.choice(STATUSES)
        time.sleep(5)

# ===============================
# HIỂN THỊ DANH SÁCH BÀN REALTIME
# ===============================
def display_tables():
    os.system("cls" if os.name == "nt" else "clear")
    print("📡 DANH SÁCH BÀN – THEO THỜI GIAN THỰC\n")

    if not tables:
        print("⚠️ Chưa có bàn nào.")
        return

    for t in tables:
        print(
            f"👉 {t['name']} | {t['capacity']} chỗ | {t['area']} | {t['status']}"
        )

    print("\n⏳ Tự động cập nhật mỗi 5 giây")

# ===============================
# AC03 – TÌM KIẾM & LỌC BÀN
# ===============================
def filter_tables(status=None, capacity=None, area=None, name=None):
    result = tables

    if status:
        result = [t for t in result if t["status"] == status]

    if capacity:
        result = [t for t in result if t["capacity"] >= capacity]

    if area:
        result = [t for t in result if area.lower() in t["area"].lower()]

    if name:
        result = [t for t in result if name.lower() in t["name"].lower()]

    return result

# ===============================
# MENU TÌM KIẾM / LỌC NHANH
# ===============================
def search_menu():
    print("\n🔍 TÌM / LỌC BÀN ĂN")
    status = input("Trạng thái (TRỐNG / ĐÃ ĐẶT / ĐANG DÙNG, Enter bỏ qua): ")
    capacity = input("Số chỗ tối thiểu (Enter bỏ qua): ")
    area = input("Khu vực (Enter bỏ qua): ")
    name = input("Tên bàn (Enter bỏ qua): ")

    capacity = int(capacity) if capacity else None

    result = filter_tables(
        status=status if status else None,
        capacity=capacity,
        area=area if area else None,
        name=name if name else None
    )

    print("\n✅ KẾT QUẢ:")
    if not result:
        print("❌ Không có bàn phù hợp.")
    else:
        for t in result:
            print(
                f"👉 {t['name']} | {t['capacity']} chỗ | {t['area']} | {t['status']}"
            )

    input("\nNhấn Enter để quay lại bảng realtime...")

# ===============================
# CHƯƠNG TRÌNH CHÍNH
# ===============================
if __name__ == "__main__":
    input_tables()

    threading.Thread(target=realtime_update, daemon=True).start()

    while True:
        display_tables()
        print("\n📌 Nhấn [F] để tìm / lọc bàn | [Ctrl + C] để thoát")
        time.sleep(5)

        choice = input("👉 Lựa chọn: ").lower()
        if choice == "f":
            search_menu()
