import pandas as pd

# =========================
# ĐỌC MENU TỪ EXCEL
# =========================
FILE_PATH = "THUCDON.xlsx"
df = pd.read_excel(FILE_PATH)

menu = []
for idx, row in df.iterrows():
    menu.append({
        "id": idx + 1,
        "name": row["TÊN MÓN"],
        "category": row["DANH MỤC"],
        "price": int(row["GIÁ TIỀN (VND)"]),
        "status": "Còn hàng"
    })

# =========================
# DANH MỤC + SỐ LA MÃ
# =========================
categories = [
    "Tráng Miệng",
    "Món Chay",
    "Mì Ý & Mỳ Việt Nam",
    "Burger & Sandwich",
    "Pizza",
    "Món chính",
    "Súp & Cháo",
    "Snack & Món Chiên Giòn",
    "Khai vị",
    "Vietnamese Coffee",
    "Expresso Bar",
    "Tea",
    "Yogurt",
    "Freshly Squeezed Juice",
    "Healthy Juice",
    "Non Alcoholic Cocktails",
    "Cocktail",
    "Long drink",
    "Whisky",
    "Cognag & Brandy",
    "Sangria",
    "House Wine",
    "Soft Drink",
    "Sparking & Champagne",
    "Beer",
    "Red Whine",
    "White Wine"
]

roman_map = {
    "I": 1, "II": 2, "III": 3, "IV": 4, "V": 5,
    "VI": 6, "VII": 7, "VIII": 8, "IX": 9, "X": 10,
    "XI": 11, "XII": 12, "XIII": 13, "XIV": 14, "XV": 15,
    "XVI": 16, "XVII": 17, "XVIII": 18, "XIX": 19, "XX": 20,
    "XXI": 21, "XXII": 22, "XXIII": 23, "XXIV": 24, "XXV": 25,
    "XXVI": 26, "XXVII": 27
}

# =========================
# IN BẢNG ASCII
# =========================
def print_table(headers, rows):
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
    for i, cat in enumerate(categories, start=1):
        roman = list(roman_map.keys())[i - 1]
        print(f"{roman}. {cat}")

def filter_by_category():
    show_categories()
    choice = input("\n👉 Nhập số La Mã hoặc tên danh mục: ").strip()

    selected_category = None

    # Nếu nhập số La Mã
    key = choice.upper()
    if key in roman_map:
        index = roman_map[key] - 1
        if 0 <= index < len(categories):
            selected_category = categories[index]
    else:
        # Nhập tên danh mục
        for cat in categories:
            if choice.lower() == cat.lower():
                selected_category = cat
                break

    if not selected_category:
        print("❌ Danh mục không hợp lệ")
        return

    result = [m for m in menu if m["category"].lower() == selected_category.lower()]
    if not result:
        print("❌ Không có món trong danh mục này")
        return

    rows = []
    for item in result:
        rows.append([item["id"], item["name"], f"{item['price']} VND"])

    print(f"\nDANH MỤC: {selected_category}")
    print_table(["ID", "Tên món", "Giá"], rows)

def show_full_menu():
    rows = []
    for item in menu:
        rows.append([item["id"], item["name"], item["category"], f"{item['price']} VND"])
    print("\nDANH SÁCH THỰC ĐƠN")
    print_table(["ID", "Tên món", "Danh mục", "Giá"], rows)

def search_menu():
    keyword = input("Nhập từ khóa: ")
    result = [m for m in menu if keyword.lower() in m["name"].lower()]
    if not result:
        print("❌ Không tìm thấy món")
        return

    rows = []
    for item in result:
        rows.append([item["id"], item["name"], item["category"], f"{item['price']} VND"])
    print_table(["ID", "Tên món", "Danh mục", "Giá"], rows)

def show_menu_status():
    rows = []

    for item in menu:
        n = item["id"]
        is_prime = True

        if n < 2:
            is_prime = False
        else:
            for i in range(2, int(n ** 0.5) + 1):
                if n % i == 0:
                    is_prime = False
                    break

        status = "Còn hàng" if is_prime else "Hết hàng"

        rows.append([
            item["id"],
            item["name"],
            f"{item['price']} VND",
            status
        ])

    print("\nTRẠNG THÁI MÓN ĂN")
    print_table(["ID", "Tên món", "Giá", "Trạng thái"], rows)


# =========================
# MENU CHÍNH
# =========================
def main_menu():
    while True:
        print("""
========== MENU ==========
1. Xem toàn bộ thực đơn
2. Xem món theo danh mục
3. Tìm kiếm món ăn
4. Xem trạng thái món
0. Thoát
==========================
        """)

        choice = input("👉 Chọn: ")

        if choice == "1":
            show_full_menu()
        elif choice == "2":
            filter_by_category()
        elif choice == "3":
            search_menu()
        elif choice == "4":
            show_menu_status()
        elif choice == "0":
            print("👋 Thoát chương trình")
            break
        else:
            print("❌ Lựa chọn không hợp lệ")

# =========================
# CHẠY CHƯƠNG TRÌNH
# =========================
if __name__ == "__main__":
    main_menu()
