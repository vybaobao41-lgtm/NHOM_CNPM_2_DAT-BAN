# ===== US-17: Cập nhật món trong order =====

class OrderItem:
    def __init__(self, ten_mon, danh_muc, gia, so_luong, ghi_chu=""):
        self.ten_mon = ten_mon
        self.danh_muc = danh_muc
        self.gia = gia
        self.so_luong = so_luong
        self.ghi_chu = ghi_chu


# ===== HÀM IN BẢNG ASCII =====
def print_table(headers, rows):
    col_widths = [len(h) for h in headers]

    for row in rows:
        for i, cell in enumerate(row):
            col_widths[i] = max(col_widths[i], len(str(cell)))

    def print_line():
        print("+" + "+".join("-" * (w + 2) for w in col_widths) + "+")

    def print_row(row):
        print("|" + "|".join(
            f" {str(cell).ljust(col_widths[i])} "
            for i, cell in enumerate(row)
        ) + "|")

    print_line()
    print_row(headers)
    print_line()
    for row in rows:
        print_row(row)
        print_line()


# ===== HÀM NGHIỆP VỤ =====
def cap_nhat_mon(order, ten_mon, so_luong_moi=None, ghi_chu_moi=None):
    """
    US-17 — Cập nhật món trong order
    AC01 — Cập nhật số lượng
    AC02 — Không cho phép số lượng ≤ 0
    AC03 — Cập nhật ghi chú
    """
    for item in order:
        if item.ten_mon.lower() == ten_mon.lower():

            if so_luong_moi is not None:
                if so_luong_moi <= 0:
                    raise ValueError("Số lượng phải lớn hơn 0")
                item.so_luong = so_luong_moi

            if ghi_chu_moi is not None:
                item.ghi_chu = ghi_chu_moi

            return True

    raise ValueError("Không tìm thấy món trong order")


# ===== HIỂN THỊ ORDER DẠNG BẢNG =====
def hien_thi_order(order, title):
    rows = []
    for item in order:
        rows.append([
            item.ten_mon,
            item.danh_muc,
            f"{item.gia} VND",
            item.so_luong,
            item.ghi_chu
        ])

    print(f"\n{title}")
    print_table(
        ["Tên món", "Danh mục", "Giá", "Số lượng", "Ghi chú"],
        rows
    )


# ===== CHƯƠNG TRÌNH CHÍNH =====
if __name__ == "__main__":

    order = [
        OrderItem("Fanta", "Soft Drink", 35000, 2),
        OrderItem("7Up","Soft Drink",35000, 4)
    ]

    hien_thi_order(order, "ORDER BAN ĐẦU")

    print("\n=== CẬP NHẬT MÓN (US-17) ===")
    ten_mon = input("Nhập tên món cần cập nhật: ")

    sl_input = input("Nhập số lượng mới (Enter để bỏ qua): ")
    so_luong_moi = None if sl_input.strip() == "" else int(sl_input)

    ghi_chu_input = input("Nhập ghi chú mới (Enter để bỏ qua): ")
    ghi_chu_moi = None if ghi_chu_input.strip() == "" else ghi_chu_input

    try:
        cap_nhat_mon(
            order,
            ten_mon,
            so_luong_moi,
            ghi_chu_moi
        )
        print("\n✅ Cập nhật thành công")
    except ValueError as e:
        print("\n❌ Lỗi:", e)

    hien_thi_order(order, "ORDER SAU CẬP NHẬT")
