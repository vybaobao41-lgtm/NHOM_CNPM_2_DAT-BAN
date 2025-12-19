# capnhatmon_input.py

# Khởi tạo danh sách món trống
menu_items = {}

def show_menu():
    if not menu_items:
        print("\nChưa có món nào trong thực đơn.")
        return
    print("\n=== DANH SÁCH THỰC ĐƠN ===")
    for id, item in menu_items.items():
        print(f"{id}. {item['name']} | Giá: {item['price']} VND | Loại: {item['category']}")

def add_menu_item():
    print("\n=== THÊM MÓN ĂN MỚI ===")
    name = input("Tên món: ").strip()
    if not name:
        print("Tên món là bắt buộc!")
        return
    try:
        price = float(input("Giá món: "))
        if price <= 0:
            print("Giá phải lớn hơn 0!")
            return
    except ValueError:
        print("Giá phải là số!")
        return
    category = input("Loại món: ").strip()
    if not category:
        print("Loại món là bắt buộc!")
        return

    # Gán ID tự động
    item_id = len(menu_items) + 1
    menu_items[item_id] = {"name": name, "price": price, "category": category}
    print("Thêm món thành công!")

def edit_menu_item():
    if not menu_items:
        print("Chưa có món nào để chỉnh sửa.")
        return

    show_menu()
    try:
        item_id = int(input("\nNhập ID món muốn chỉnh sửa: "))
        if item_id not in menu_items:
            print("Món ăn không tồn tại!")
            return
    except ValueError:
        print("ID phải là số nguyên!")
        return

    item = menu_items[item_id]

    # AC01 — Hiển thị thông tin hiện tại
    print("\n=== CHỈNH SỬA MÓN ĂN ===")
    print(f"Tên hiện tại: {item['name']}")
    print(f"Giá hiện tại: {item['price']}")
    print(f"Loại hiện tại: {item['category']}")

    # Nhập thông tin mới
    new_name = input("Tên mới (bỏ trống để giữ nguyên): ").strip()
    new_price = input("Giá mới (bỏ trống để giữ nguyên): ").strip()
    new_category = input("Loại mới (bỏ trống để giữ nguyên): ").strip()

    # AC02 — Kiểm tra bắt buộc
    if new_name == "" and item['name'] == "":
        print("Tên món là bắt buộc. Không thể lưu!")
        return
    if new_category == "" and item['category'] == "":
        print("Loại món là bắt buộc. Không thể lưu!")
        return

    # AC03 — Kiểm tra giá hợp lệ
    if new_price != "":
        try:
            price_value = float(new_price)
            if price_value <= 0:
                print("Giá phải là số lớn hơn 0. Không thể lưu!")
                return
        except ValueError:
            print("Giá phải là số lớn hơn 0. Không thể lưu!")
            return
    else:
        price_value = item['price']

    # Cập nhật thông tin
    if new_name != "":
        item['name'] = new_name
    item['price'] = price_value
    if new_category != "":
        item['category'] = new_category

    # AC04 — thông báo thành công
    print("\nCập nhật thành công!")

    # AC05 — hiển thị danh sách cập nhật
    show_menu()

# Main
if __name__ == "__main__":
    while True:
        print("\n1. Thêm món ăn")
        print("2. Hiển thị thực đơn")
        print("3. Chỉnh sửa món ăn")
        print("0. Thoát")
        choice = input("Chọn chức năng: ")
        if choice == "1":
            add_menu_item()
        elif choice == "2":
            show_menu()
        elif choice == "3":
            edit_menu_item()
        elif choice == "0":
            print("Thoát chương trình.")
            break
        else:
            print("Lựa chọn không hợp lệ.")
