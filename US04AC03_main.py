from US04AC03_table import filter_tables

def display_tables(tables):
    if not tables:
        print("❌ Không có bàn phù hợp.")
        return

    print("\n✅ Kết quả tìm / lọc:")
    for t in tables:
        print(
            f"👉 {t['name']} | {t['capacity']} chỗ | {t['area']} | {t['status']} ⭐"
        )

def main():
    print("🔍 LỌC / TÌM BÀN (US04 - AC03)")

    status = input("Trạng thái (TRỐNG / ĐÃ ĐẶT / ĐANG DÙNG, Enter bỏ qua): ")
    capacity = input("Số chỗ (Enter bỏ qua): ")
    area = input("Khu vực (Enter bỏ qua): ")
    name = input("Tên bàn (Enter bỏ qua): ")

    capacity = int(capacity) if capacity else None

    result = filter_tables(
        status=status if status else None,
        capacity=capacity,
        area=area if area else None,
        name=name if name else None
    )

    display_tables(result)

if __name__ == "__main__":
    main()
