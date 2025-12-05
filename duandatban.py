def validate_table_data(name, seats):
    #AC-Kiểm tra dữ liệu hợp lệ
    errors = []

    # Kiểm tra tên bàn
    if not name or name.strip() == "":
        errors.append("Tên bàn không được để trống")

    # Kiểm tra số lượng chỗ ngồi
    if not isinstance(seats, int) or seats <= 0:
        errors.append("Số lượng chỗ ngồi phải là số nguyên dương")

    return errors


# Demo
if __name__ == "__main__":
    print(validate_table_data("Bàn 1", 4))       # Hợp lệ → []
    print(validate_table_data("", -2))          # Sai → danh sách lỗi
