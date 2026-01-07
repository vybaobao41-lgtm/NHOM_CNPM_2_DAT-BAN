import json


# =========================
# ĐỌC MENU TỪ FILE JSON
# =========================
def load_menu_from_json(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            # Dữ liệu JSON đã có sẵn cấu trúc: id, ten, gia, danh_muc, trang_thai
            return json.load(f)
    except FileNotFoundError:
        print(f"❌ Không tìm thấy file {file_path}")
        return []


# Load dữ liệu
FILE_NAME = "THUCDON.json"
menu = load_menu_from_json(FILE_NAME)

# =========================
# DANH MỤC + SỐ LA MÃ
# =========================
# Tự động lấy danh sách danh mục duy nhất từ dữ liệu JSON
categories = sorted(list(set(item['danh_muc'] for item in menu)))

roman_numbers = [
    "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX", "X",
    "XI", "XII", "XIII", "XIV", "XV", "XVI", "XVII", "XVIII", "XIX", "XX",
    "XXI", "XXII", "XXIII", "XXIV", "XXV", "XXVI", "XXVII"
]
roman_map = {roman: i + 1 for i, roman in enumerate(roman_numbers)}


# =========================
# IN BẢNG ASCII
# =========================
def print_table(headers, rows):
    if not rows:
        return
    widths = [len(h) for h in headers]
    for r in rows:
        for i, c in enumerate(r):
            widths[i] = max(widths[i], len(str(c)))

    def line():
        print("+" + "+".join("-" * (w + 2) for w in widths) + "+")

    def row(r):
        print("|" + "|".join(f" {str(c).ljust(widths[i])} " for i, c in enumerate(r)) + "|")

    line()
    row(headers)
    line()
    for r in rows:
        row(r)
        line()


# =========================
# CHỨC NĂNG
# =========================
def show_categories():
    print("\nDANH SÁCH DANH MỤC")
    for i, cat in enumerate(categories):
        roman = roman_numbers[i] if i < len(roman_numbers) else str(i + 1)
        print(f"{roman}. {cat}")


def filter_by_category():
    show_categories()
    choice = input("\n👉 Nhập số La Mã hoặc tên danh mục: ").strip()

    selected_category = None
    key = choice.upper()

    if key in roman_map:
        index = roman_map[key] - 1
        if 0 <= index < len(categories):
            selected_category = categories[index]
    else:
        for cat in categories:
            if choice.lower() == cat.lower():
                selected_category = cat
                break

    if not selected_category:
        print("❌ Danh mục không hợp lệ")
        return

    result = [m for m in menu if m["danh_muc"] == selected_category]
    rows = [[m["id"], m["ten"], f"{m['gia']} VND", m["trang_thai"]] for m in result]

    print(f"\nDANH MỤC: {selected_category}")
    print_table(["ID", "Tên món", "Giá", "Trạng thái"], rows)


def show_full_menu():
    rows = [[m["id"], m["ten"], m["danh_muc"], f"{m['gia']} VND"] for m in menu]
    print("\nDANH SÁCH THỰC ĐƠN")
    print_table(["ID", "Tên món", "Danh mục", "Giá"], rows)


def search_menu():
    keyword = input("Nhập từ khóa tìm kiếm: ").lower()
    result = [m for m in menu if keyword in m["ten"].lower()]

    if not result:
        print("❌ Không tìm thấy món")
        return

    rows = [[m["id"], m["ten"], m["danh_muc"], f"{m['gia']} VND"] for m in result]
    print_table(["ID", "Tên món", "Danh mục", "Giá"], rows)


def show_menu_status():
    # Hiển thị trạng thái thực tế từ file JSON
    rows = [[m["id"], m["ten"], f"{m['gia']} VND", m["trang_thai"]] for m in menu]
    print("\nTRẠNG THÁI MÓN ĂN (Cập nhật từ hệ thống)")
    print_table(["ID", "Tên món", "Giá", "Trạng thái"], rows)


# =========================
# MENU CHÍNH
# =========================
def main_menu():
    if not menu:
        return

    while True:
        print("""
========== MENU QUẢN LÝ ==========
1. Xem toàn bộ thực đơn
2. Xem món theo danh mục
3. Tìm kiếm món ăn
4. Xem trạng thái món (Còn/Hết)
0. Thoát
==================================
        """)

        choice = input("👉 Chọn chức năng: ")

        if choice == "1":
            show_full_menu()
        elif choice == "2":
            filter_by_category()
        elif choice == "3":
            search_menu()
        elif choice == "4":
            show_menu_status()
        elif choice == "0":
            print("👋 Tạm biệt!")
            break
        else:
            print("❌ Lựa chọn không hợp lệ")


if __name__ == "__main__":
    main_menu()