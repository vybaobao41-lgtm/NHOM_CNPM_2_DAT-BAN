import random

# =========================
# DANH MỤC THỰC ĐƠN
# =========================
categories = {
    "Hải sản": [
        "Tôm hấp bia", "Cá nướng giấy bạc", "Mực xào sa tế", "Ghẹ rang muối", "Sò điệp nướng mỡ hành",
        "Hàu nướng phô mai", "Cá hồi áp chảo", "Tôm sốt me", "Mực nhồi thịt", "Cá trê chiên giòn"
    ],
    "Món khai vị": [
        "Súp cua", "Salad rau củ", "Chả giò hải sản", "Gỏi cuốn", "Sườn nướng BBQ",
        "Bánh xèo mini", "Nem chua rán", "Súp bí đỏ", "Bánh bao chiên", "Khoai tây chiên"
    ],
    "Món chính": [
        "Cơm chiên hải sản", "Phở bò tái", "Bún chả Hà Nội", "Mì xào thập cẩm", "Cá kho tộ",
        "Gà rang muối", "Heo quay", "Lẩu hải sản", "Cá hồi nướng", "Mực xào chua ngọt"
    ],
    "Tráng miệng": [
        "Kem socola", "Bánh flan", "Chè ba màu", "Bánh bông lan", "Trái cây tráng miệng",
        "Kem vani", "Pudding socola", "Bánh mousse", "Chè đậu xanh", "Bánh crepe"
    ],
    "Đồ uống": [
        "Nước cam", "Trà đá", "Trà sữa", "Cà phê sữa đá", "Sinh tố bơ",
        "Sinh tố dâu", "Nước ép cà rốt", "Nước ép táo", "Bia tươi", "Nước khoáng"
    ]
}

# =========================
# TẠO DỮ LIỆU 350 MÓN ĂN
# =========================
menu = []
id_counter = 1

for category, items in categories.items():
    # Tạo 70 món mỗi danh mục để tổng ~350 món
    for i in range(70):
        name_base = random.choice(items)
        name = f"{name_base} {i + 1}"
        price = random.randint(50000, 500000)  # giá từ 50k → 500k
        status = random.choice(["Còn hàng", "Hết hàng"])
        menu.append({
            "name": name,
            "category": category,
            "price": price,
            "description": f"{name} - Món ăn ngon thuộc danh mục {category}.",
            "image": f"image_{id_counter}.jpg",
            "status": status
        })
        id_counter += 1


# =========================
# AC-01: Hiển thị đầy đủ món ăn
# =========================
def show_full_menu():
    print(f"--- DANH SÁCH THỰC ĐƠN ({len(menu)} món) ---")
    for item in menu:
        print(f"Tên món: {item['name']}")
        print(f"Danh mục: {item['category']}")
        print(f"Giá: {item['price']} VND")
        print(f"Mô tả: {item['description']}")
        print(f"Hình ảnh: {item['image']}")
        print(f"Trạng thái: {item['status']}")
        print("---------------------------")


# =========================
# AC-02: Lọc theo danh mục
# =========================
def filter_by_category(category):
    filtered = [item for item in menu if item["category"].lower() == category.lower()]
    if not filtered:
        print(f"❌ Không tìm thấy món trong danh mục '{category}'")
        return
    print(f"--- MÓN ĂN DANH MỤC: {category} ({len(filtered)} món) ---")
    for item in filtered:
        print(f"{item['name']} | {item['price']} VND | {item['status']}")


# =========================
# AC-03: Tìm kiếm món
# =========================
def search_menu(keyword):
    result = [item for item in menu if
              keyword.lower() in item["name"].lower() or keyword.lower() in item["description"].lower()]
    if not result:
        print(f"❌ Không tìm thấy món với từ khóa '{keyword}'")
        return
    print(f"--- KẾT QUẢ TÌM KIẾM: '{keyword}' ({len(result)} món) ---")
    for item in result:
        print(f"{item['name']} | {item['category']} | {item['price']} VND | {item['status']}")


# =========================
# AC-04: Hiển thị trạng thái món
# =========================
def show_menu_status():
    print("--- TRẠNG THÁI MÓN ĂN ---")
    for item in menu:
        print(f"{item['name']}: {item['status']}")


# =========================
# DEMO / TEST
# =========================
if __name__ == "__main__":
    print("1️⃣ Hiển thị đầy đủ menu (AC-01)")
    show_full_menu()

    print("\n2️⃣ Lọc danh mục Hải sản (AC-02)")
    filter_by_category("Hải sản")

    print("\n3️⃣ Tìm kiếm từ khóa 'Tôm' (AC-03)")
    search_menu("Tôm")

    print("\n4️⃣ Hiển thị trạng thái món ăn (AC-04)")
    show_menu_status()
