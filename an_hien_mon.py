# an_hien_mon.py

# Danh sách món trống
menu_items = {}

def show_menu_for_customers():
    print("\n=== MENU KHÁCH HÀNG ===")
    has_visible = False
    for id, item in menu_items.items():
        if item["status"] == "Hiển thị":
            print(f"{item['name']} | Giá: {item['price']} VND | Loại: {item['category']}")
            has_visible = True
    if not has_visible:
        print("Chưa có món nào đang bán.")

def show_menu_for_management():
    print("\n=== DANH SÁCH QUẢN LÝ ===")
    if not menu_items:
        print("Chưa có món nào trong danh sách.")
        return
    for id, item in menu_items.items():
        tag = "" if item["status"] == "Hiển thị" else "(Đang ẩn)"
        print(f"{id}. {item['name']} | Giá: {item['price']} VND | Loại: {item['category']} {tag}")

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

    item_id = len(menu_items) + 1
    menu_items[item_id] = {"name": name, "price": price, "category": category, "status": "Hiển thị"}
    print(f"Món '{name}' đã được thêm vào danh sách!")

def toggle_menu_item():
    show_menu_for_management()
    try:
        item_id = int(input("\nNhập ID món muốn ẩn/hiện: "))
        if item_id not in menu_items:
            print("Món ăn không tồn tại!")
            return
    except ValueError:
        print("ID phải là số nguyên!")
        return

    item = menu_items[item_id]
    if item["status"] == "Hiển thị":
        item["status"] = "Không hiển thị"
        print(f"Món '{item['name']}' đã được ẩn thành công!")  # AC01
    else:
        item["status"] = "Hiển thị"
        print(f"Món '{item['name']}' đã được bật bán lại!")  # AC02

    show_menu_for_management()  # AC04

def view_item_detail():
    show_menu_for_management()
    try:
        item_id = int(input("\nNhập ID món muốn xem chi tiết: "))
        if item_id not in menu_items:
            print("Món ăn không tồn tại!")
            return
    except ValueError:
        print("ID phải là số nguyên!")
        return

    item = menu_items[item_id]
    print("\n=== CHI TIẾT MÓN ĂN ===")
    print(f"Tên: {item['name']}")
    print(f"Giá: {item['price']} VND")
    print(f"Loại: {item['category']}")
    print(f"Trạng thái: {item['status']}")
    if item["status"] == "Không hiển thị":
        print("(Món đang bị ẩn nhưng dữ liệu vẫn đầy đủ)")  # AC03

# Main
if __name__ == "__main__":
    while True:
        print("\n1. Thêm món ăn")
        print("2. Xem menu khách hàng")
        print("3. Xem danh sách quản lý")
        print("4. Ẩn/hiện món ăn")
        print("5. Xem chi tiết món")
        print("0. Thoát")
        choice = input("Chọn chức năng: ")
        if choice == "1":
            add_menu_item()
        elif choice == "2":
            show_menu_for_customers()
        elif choice == "3":
            show_menu_for_management()
        elif choice == "4":
            toggle_menu_item()
        elif choice == "5":
            view_item_detail()
        elif choice == "0":
            print("Thoát chương trình.")
            break
        else:
            print("Lựa chọn không hợp lệ.")
