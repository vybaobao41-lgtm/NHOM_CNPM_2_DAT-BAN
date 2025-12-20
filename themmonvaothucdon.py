# US-11 — Thêm món mới vào thực đơn

menu = []  # Danh sách món ăn (dữ liệu giả)


def add_menu_item(name, price, category):
    # ===== AC01: Kiểm tra thiếu thông tin =====
    if not name or not category or price is None:
        return "Lỗi: Thiếu thông tin bắt buộc"

    # ===== AC02: Kiểm tra giá hợp lệ =====
    try:
        price = float(price)
        if price <= 0:
            return "Lỗi: Giá phải lớn hơn 0"
    except ValueError:
        return "Lỗi: Giá phải là số"

    # ===== AC03 + AC04: Lưu món & hiển thị =====
    item = {
        "name": name,
        "price": price,
        "category": category
    }
    menu.append(item)
    return "Thêm món thành công"


def show_menu():
    print("\n📋 Danh sách thực đơn:")
    if not menu:
        print("Chưa có món nào")
    for i, item in enumerate(menu, start=1):
        print(f"{i}. {item['name']} - {item['price']} - {item['category']}")


# ===== Chạy thử chương trình =====
if __name__ == "__main__":
    while True:
        print("\n--- Thêm món mới ---")
        name = input("Tên món: ")
        price = input("Giá: ")
        category = input("Loại món: ")

        result = add_menu_item(name, price, category)
        print(result)

        show_menu()

        cont = input("\nTiếp tục? (y/n): ")
        if cont.lower() != "y":
            break
