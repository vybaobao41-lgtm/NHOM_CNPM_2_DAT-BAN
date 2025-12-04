tables = {}  # Lưu bàn: số bàn -> trạng thái ("trong" hoặc "dat")


def add_table():
    try:
        table_number = int(input("Nhập số hiệu bàn: "))
        if table_number <= 0:
            print("❌ Số bàn phải > 0!")
            return
    except ValueError:
        print("❌ Vui lòng nhập số hợp lệ!")
        return

    if table_number in tables:
        print(f"⚠ Bàn số {table_number} đã tồn tại!")
    else:
        tables[table_number] = "trong"
        print(f"✔ Thêm bàn số {table_number} thành công!")


def show_tables():
    empty_tables = [t for t, status in tables.items() if status == "trong"]

    if not empty_tables:
        print("⚠ Không có bàn trống!")
    else:
        print("\n📌 Danh sách bàn TRỐNG:")
        for t in sorted(empty_tables):
            print(f" - Bàn số {t}")
        print("")


def reserve_table():
    try:
        table_number = int(input("Nhập số bàn muốn đặt: "))
    except ValueError:
        print("❌ Vui lòng nhập số hợp lệ!")
        return

    if table_number not in tables:
        print(f"⚠ Không tồn tại bàn số {table_number}!")
    elif tables[table_number] == "dat":
        print(f"⚠ Bàn số {table_number} đã được đặt trước!")
    else:
        tables[table_number] = "dat"
        print(f"✔ Đặt bàn số {table_number} thành công!")
