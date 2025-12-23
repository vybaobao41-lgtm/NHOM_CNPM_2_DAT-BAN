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
        "description": f"{row['TÊN MÓN']} thuộc danh mục {row['DANH MỤC']}",
        "image": None,          # Excel chưa có → để None
        "status": "Còn hàng"    # Excel chưa có → mặc định
    })

def show_full_menu():
    """
        Hiển thị TOÀN BỘ danh sách thực đơn đã đọc từ file Excel.

        - Không có tham số đầu vào
        - Duyệt qua danh sách `menu`
        - In ra: ID, Tên món, Danh mục, Giá tiền
        - Dùng khi:
            + Người dùng muốn xem toàn bộ thực đơn
            + Màn hình "Xem danh sách món ăn"
    """
    print(f"--- DANH SÁCH THỰC ĐƠN ({len(menu)} món) ---")
    for item in menu:
        print(f"[{item['id']}] {item['name']}")
        print(f"Danh mục: {item['category']}")
        print(f"Giá: {item['price']} VND")
        print("---------------------------")

def filter_by_category(category):
    """
        Hiển thị TOÀN BỘ danh sách thực đơn đã đọc từ file Excel.

        - Không có tham số đầu vào
        - Duyệt qua danh sách `menu`
        - In ra: ID, Tên món, Danh mục, Giá tiền
        - Dùng khi:
            + Người dùng muốn xem toàn bộ thực đơn
            + Màn hình "Xem danh sách món ăn"
    """
    result = [i for i in menu if i["category"].lower() == category.lower()]
    if not result:
        print("❌ Không có món trong danh mục này")
        return

    print(f"--- DANH MỤC: {category} ---")
    for item in result:
        print(f"{item['name']} | {item['price']} VND")

def search_menu(keyword):
    """
        Tìm kiếm món ăn theo TỪ KHÓA trong tên món.

        Tham số:
            keyword (str): Từ khóa cần tìm (VD: "Bánh")

        - Tìm kiếm gần đúng (contains)
        - Không phân biệt hoa/thường
        - Dùng khi:
            + Người dùng nhập ô tìm kiếm
            + Chức năng search món ăn
    """
    result = [i for i in menu if keyword.lower() in i["name"].lower()]
    if not result:
        print("❌ Không tìm thấy món")
        return

    for item in result:
        print(f"{item['name']} | {item['category']} | {item['price']} VND")

def show_menu_status():
    """
        Hiển thị TRẠNG THÁI của từng món ăn.

        - Hiện tại trạng thái mặc định là "Còn hàng"
        - Chưa đọc từ Excel (hard-code)
        - Dùng khi:
            + Kiểm tra món còn / hết
            + Sau này mở rộng để quản lý tồn kho
    """
    for item in menu:
        print(f"{item['name']}: {item['status']}")

if __name__ == "__main__":
    show_full_menu()
    filter_by_category("Tráng Miệng")
    search_menu("Bánh")
    show_menu_status()
