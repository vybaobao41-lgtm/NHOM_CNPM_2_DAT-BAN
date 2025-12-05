# Form đặt bàn theo logic Given – When – Then (version đơn giản nhất)

# Danh sách bàn mô phỏng sơ đồ bàn
so_do_ban = []

def hien_thi_so_do():
    print("\n=== SƠ ĐỒ BÀN ĂN ===")
    if not so_do_ban:
        print("Chưa có bàn nào.")
    else:
        for ban in so_do_ban:
            print(f"Bàn {ban['id']} - Trạng thái: {ban['trang_thai']}")
    print("======================\n")

def tao_ban_moi():
    print("=== FORM ĐẶT BÀN ===")

    ngay = input("Nhập ngày: ")
    gio = input("Nhập giờ: ")

    # nhập số người hợp lệ
    while True:
        try:
            so_nguoi = int(input("Nhập số người: "))
            if so_nguoi > 0:
                break
            else:
                print("Số người phải > 0!")
        except:
            print("Vui lòng nhập số nguyên!")

    # Tạo thông tin bàn
    ban_id = len(so_do_ban) + 1
    ban_moi = {
        "id": ban_id,
        "ngay": ngay,
        "gio": gio,
        "so_nguoi": so_nguoi,
        "trang_thai": "Trống"
    }

    # GIVEN: Bàn mới đã được tạo thành công
    so_do_ban.append(ban_moi)
    print("\n✔ Bàn mới đã được tạo thành công!")

    # WHEN: Quản lý quay về màn hình sơ đồ bàn ăn
    hien_thi_so_do()

    # THEN: Bàn xuất hiện và có thể chọn tạo order hoặc đặt trước
    print(f"Bạn có thể chọn Bàn {ban_id} để:")
    print("- Tạo order")
    print("- Đặt trước (reservation)")
    print("\nHoàn tất!")

# Chạy chương trình
tao_ban_moi()
