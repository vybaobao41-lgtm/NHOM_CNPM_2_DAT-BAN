# ===== US-17: Cập nhật món trong order =====

class OrderItem:
    def __init__(self, ten_mon, danh_muc, gia, so_luong, ghi_chu=""):
        self.ten_mon = ten_mon
        self.danh_muc = danh_muc
        self.gia = gia
        self.so_luong = so_luong
        self.ghi_chu = ghi_chu

    def __str__(self):
        return (f"{self.ten_mon} | {self.danh_muc} | "
                f"{self.gia} VND | SL: {self.so_luong} | Ghi chú: {self.ghi_chu}")


def cap_nhat_mon(order, ten_mon, so_luong_moi=None, ghi_chu_moi=None):
    """
    US-17 — Cập nhật món trong order
    AC01 — Cập nhật số lượng
    AC02 — Không cho phép số lượng ≤ 0
    AC03 — Cập nhật ghi chú
    """
    for item in order:
        if item.ten_mon == ten_mon:

            # AC02 — Không cho phép số lượng ≤ 0
            if so_luong_moi is not None:
                if so_luong_moi <= 0:
                    raise ValueError("Số lượng phải lớn hơn 0")
                item.so_luong = so_luong_moi  # AC01

            # AC03 — Cập nhật ghi chú
            if ghi_chu_moi is not None:
                item.ghi_chu = ghi_chu_moi

            return True  # Cập nhật thành công

    raise ValueError("Không tìm thấy món trong order")


# ===== Ví dụ sử dụng =====
if __name__ == "__main__":
    # Order mẫu
    order = [
        OrderItem("Fanta", "Soft Drink",  35000 , 2),
        OrderItem("Khoai Tây Chiên (French Fries with Mayonnaise Sauce)", "Snack & Món Chiên Giòn",  79000 , 1)
    ]

    print("=== Order ban đầu ===")
    for item in order:
        print(item)

    print("\n=== Cập nhật món ===")
    try:
        cap_nhat_mon(
            order,
            ten_mon = "Fanta",
            so_luong_moi = 3,
            ghi_chu_moi = "Ít đá"
        )
        print("Cập nhật thành công")
    except ValueError as e:
        print("Lỗi:", e)

    print("\n=== Order sau cập nhật ===")
    for item in order:
        print(item)
