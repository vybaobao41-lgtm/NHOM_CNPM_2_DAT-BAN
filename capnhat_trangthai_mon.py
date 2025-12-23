from datetime import datetime

class OrderManager:
    def __init__(self):
        # Giả lập danh sách đơn hàng (trong thực tế sẽ lấy từ Database)
        self.current_order = []

    def add_item_to_order(self, dish):
        """
        Xử lý thêm món vào đơn hàng
        dish: Dictionary chứa {id, name, is_available}
        """

        # Không cho thêm món đã hết
        if not dish.get('is_available', True):
            return {"status": "error", "message": f"Món {dish['name']} đã hết hàng!"}

        # Nếu món đã tồn tại trong order → tăng số lượng
        for item in self.current_order:
            if item['id'] == dish['id']:
                item['quantity'] += 1
                return {
                    "status": "success",
                    "message": f"Đã tăng số lượng món {dish['name']}"
                }

        # AC-01: Thêm món mới với trạng thái mặc định
        new_item = {
            "id": dish['id'],
            "name": dish['name'],
            "quantity": 1,
            "status": "Đang chế biến",          # 👈 AC-01
            "completed_at": None                # 👈 Chưa hoàn thành
        }

        self.current_order.append(new_item)
        return {
            "status": "success",
            "message": f"Đã thêm món {dish['name']} vào đơn hàng"
        }

    # AC-02: Cập nhật trạng thái món sang "Hoàn thành"
    def complete_item(self, dish_id):
        for item in self.current_order:
            if item['id'] == dish_id:
                if item['status'] == "Hoàn thành":
                    return {
                        "status": "error",
                        "message": "Món này đã hoàn thành trước đó"
                    }

                item['status'] = "Hoàn thành"
                item['completed_at'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

                return {
                    "status": "success",
                    "message": f"Món {item['name']} đã hoàn thành",
                    "completed_at": item['completed_at']
                }

        return {"status": "error", "message": "Không tìm thấy món trong đơn hàng"}
if __name__ == "__main__":
    manager = OrderManager()

    pho_bo = {"id": 1, "name": "Phở Bò", "is_available": True}

    print(manager.add_item_to_order(pho_bo))
    print(manager.current_order)

    print(manager.complete_item(1))
    print(manager.current_order)
