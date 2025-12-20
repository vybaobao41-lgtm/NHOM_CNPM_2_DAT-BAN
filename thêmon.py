class OrderManager:
    def __init__(self):
        # Giả lập danh sách đơn hàng (trong thực tế sẽ lấy từ Database)
        self.current_order = []

    def add_item_to_order(self, dish):
        """
        Xử lý thêm món vào đơn hàng dựa trên các tiêu chí AC
        dish: Dictionary chứa {id, name, is_available}
        """
        
        # AC-03: Không cho thêm món đã bị ẩn (hết món)
        if not dish.get('is_available', True):
            return {"status": "error", "message": f"Món {dish['name']} đã hết hàng!"}

        # Kiểm tra xem món đã tồn tại trong order chưa (Để thực hiện AC-02)
        for item in self.current_order:
            if item['id'] == dish['id']:
                # AC-02: Tăng số lượng món đã tồn tại
                item['quantity'] += 1
                return {"status": "success", "message": f"Đã tăng số lượng món {dish['name']}"}

        # AC-01: Thêm món mới vào order (nếu chưa tồn tại)
        new_item = {
            "id": dish['id'],
            "name": dish['name'],
            "quantity": 1
        }
        self.current_order.append(new_item)
        return {"status": "success", "message": f"Đã thêm món {dish['name']} vào đơn hàng"}

# --- Ví dụ chạy thử ---
if __name__ == "__main__":
    manager = OrderManager()
    
    # Giả lập dữ liệu món ăn
    pho_bo = {"id": 1, "name": "Phở Bò", "is_available": True}
    com_tam = {"id": 2, "name": "Cơm Tấm", "is_available": False} # Món đã hết

    print(manager.add_item_to_order(pho_bo))  # AC-01: Thêm mới thành công
    print(manager.add_item_to_order(pho_bo))  # AC-02: Tăng số lượng lên 2
    print(manager.add_item_to_order(com_tam)) # AC-03: Báo lỗi vì hết món