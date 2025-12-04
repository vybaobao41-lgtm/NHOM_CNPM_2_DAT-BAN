# main.py
from table_manager import add_table, show_tables, reserve_table


def main():
    while True:
        print("\n===== HỆ THỐNG QUẢN LÝ BÀN ĂN =====")
        print("1. Thêm bàn mới")
        print("2. Xem bàn trống")
        print("3. Đặt bàn")
        print("0. Thoát")

        choice = input("Chọn chức năng: ")

        if choice == "1":
            add_table()
        elif choice == "2":
            show_tables()
        elif choice == "3":
            reserve_table()
        elif choice == "0":
            print("👋 Tạm biệt!")
            break
        else:
            print("❌ Lựa chọn không hợp lệ!")


if __name__ == "__main__":
    main()
