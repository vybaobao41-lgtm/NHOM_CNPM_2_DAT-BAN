# ===== US-17: Cập nhật món trong order theo ID =====

class OrderItem:
    def __init__(self, ma_mon, ten_mon, ten_mon_en, danh_muc, gia, so_luong, ghi_chu=""):
        self.ma_mon = ma_mon             # ID món
        self.ten_mon = ten_mon           # Tiếng Việt
        self.ten_mon_en = ten_mon_en     # Tiếng Anh
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
def cap_nhat_mon(order, ma_mon_nhap, so_luong_moi=None, ghi_chu_moi=None):
    """
    US-17 — Cập nhật món trong order theo ID
    AC01 — Cập nhật số lượng
    AC02 — Không cho phép số lượng ≤ 0
    AC03 — Cập nhật ghi chú
    """
    for item in order:
        if ma_mon_nhap.upper() == item.ma_mon.upper():  # So sánh ID không phân biệt chữ hoa/thường
            if so_luong_moi is not None:
                if so_luong_moi <= 0:
                    raise ValueError("Số lượng phải lớn hơn 0")
                item.so_luong = so_luong_moi

            if ghi_chu_moi is not None:
                item.ghi_chu = ghi_chu_moi

            return True

    raise ValueError("Không tìm thấy món với ID đã nhập")


# ===== HIỂN THỊ ORDER DẠNG BẢNG =====
def hien_thi_order(order, title):
    rows = []
    for item in order:
        if item.ten_mon.lower() == item.ten_mon_en.lower():
            ten_hien_thi = item.ten_mon
        else:
            ten_hien_thi = f"{item.ten_mon} ({item.ten_mon_en})"

        rows.append([
            item.ma_mon,
            ten_hien_thi,
            item.danh_muc,
            f"{item.gia} VND",
            item.so_luong,
            item.ghi_chu
        ])

    print(f"\n{title}")
    print_table(
        ["ID", "Tên món", "Danh mục", "Giá", "Số lượng", "Ghi chú"],
        rows
    )


# ===== CHƯƠNG TRÌNH CHÍNH =====
if __name__ == "__main__":
    order = [
        OrderItem("TE001", "Trà Lipton", "Lipton Tea", "Soft Drink", 35000, 2),
        OrderItem("SF003", "7Up", "7Up", "Soft Drink", 35000, 4, "Thêm đá"),
        OrderItem("KV007", "Nem Rán Thập Cẩm", "Vietnamese Fried Spring Rolls", "Khai Vị", 119000, 2),
        OrderItem("SN001", "Khoai Tây Chiên", "French Fries with Mayonnaise Sauce", "Snack & Món Chiên Giòn", 79000, 3),
        OrderItem("MN005", "Cơm Chiên Hải Sản", "Fried Rice with Seafood", "Món chính", 155000, 3),
        OrderItem("MC004", "Gỏi Hoa Chuối", "Banana Blossom Salad", "Món chay", 99000, 1),
        OrderItem("SF008", "Fanta", "Fanta", "Soft Drink", 35000, 8, "Thêm đá")
    ]

    hien_thi_order(order, "ORDER BAN ĐẦU")

    print("\n=== CẬP NHẬT MÓN (US-17 THEO ID) ===")
    ma_mon = input("Nhập ID món cần cập nhật: ").strip()

    sl_input = input("Nhập số lượng mới (Enter để bỏ qua): ")
    so_luong_moi = None if sl_input.strip() == "" else int(sl_input)

    ghi_chu_input = input("Nhập ghi chú mới (Enter để bỏ qua): ")
    ghi_chu_moi = None if ghi_chu_input.strip() == "" else ghi_chu_input

    try:
        cap_nhat_mon(order, ma_mon, so_luong_moi, ghi_chu_moi)
        print("\n✅ Cập nhật thành công")
    except ValueError as e:
        print("\n❌ Lỗi:", e)

    hien_thi_order(order, "ORDER SAU CẬP NHẬT")
