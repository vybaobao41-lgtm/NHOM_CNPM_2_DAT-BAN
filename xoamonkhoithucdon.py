class MenuManager:
    def __init__(self):
        # Danh sách món ăn, mỗi món là dict
        self.menu = []

    def add_dish(self, dish_id, name, price):
        self.menu.append({
            "id": dish_id,
            "name": name,
            "price": price
        })

    def get_menu(self):
        return self.menu

    def delete_dish(self, dish_id):
        """
        Xoá món ăn khỏi thực đơn
        Trả về True nếu xoá thành công
        """
        for dish in self.menu:
            if dish["id"] == dish_id:
                self.menu.remove(dish)
                return True
        return False


# ======== CHƯƠNG TRÌNH CHÍNH ========
if __name__ == "__main__":
    # Khởi tạo MenuManager
    menu_manager = MenuManager()

    # Thêm món mẫu
    menu_manager.add_dish(1, "Tôm hùm sốt bơ tỏi", 1200000)
    menu_manager.add_dish(2, "Mì Ý cua sốt kem", 100000)
    menu_manager.add_dish(3, "Pizza 4 Cheese ", 125000)
    menu_manager.add_dish(4, "Salad trộn dầu giấm", 80000)
    menu_manager.add_dish(5, "Súp bí đỏ", 70000)
    menu_manager.add_dish(6, "Bò bít tết", 250000)  
    menu_manager.add_dish(7, "Ghẹ rang muối", 250000)    
    menu_manager.add_dish(8, "Sashimi cá hồi", 290000)   
    menu_manager.add_dish(9, "Gà hầm nấm đông cô", 500000)
    menu_manager.add_dish(10, "Chivas18 ", 15000000)       

    # Hàm hiển thị menu
    def show_menu():
        print("\n=== DANH SÁCH THỰC ĐƠN ===")
        for dish in menu_manager.get_menu():
            print(f"{dish['id']} - {dish['name']} - {dish['price']} VNĐ")

    # AC-01: Hiển thị danh sách thực đơn
    show_menu()

    # AC-02: Xoá món
    try:
        dish_id = int(input("\nNhập ID món cần xoá: "))
        if menu_manager.delete_dish(dish_id):
            print("✔ Xoá món thành công!")
        else:
            print("✖ Có lỗi xảy ra khi xoá món!")
    except ValueError:
        print("✖ Vui lòng nhập số hợp lệ!")

    # AC-03: Hiển thị lại menu đã cập nhật
    show_menu()
