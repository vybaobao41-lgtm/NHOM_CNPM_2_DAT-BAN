# =========================
# US-11 — THÊM MÓN VÀO THỰC ĐƠN
# AC-01: Thông tin không hợp lệ
# =========================

thuc_don = []  # Danh sách món ăn

def ac01_kiem_tra_thong_tin_trong(ten_mon, gia, loai_mon):
    if ten_mon.strip() == "":
        return False, "❌ Tên món không được để trống"
    if gia.strip() == "":
        return False, "❌ Giá không được để trống"
    if loai_mon.strip() == "":
        return False, "❌ Loại món không được để trống"
    return True, ""

def ac01_them_mon():
    print("\n--- AC-01: Thông tin không hợp lệ ---")
    ten_mon = input("Nhập tên món: ")
    gia = input("Nhập giá: ")
    loai_mon = input("Nhập loại món: ")

    hop_le, thong_bao = ac01_kiem_tra_thong_tin_trong(ten_mon, gia, loai_mon)
    if not hop_le:
        print(thong_bao)
        print("❌ Không cho phép lưu món ăn")
        return

    print("✔ Thông tin không bị bỏ trống")

# =========================
# AC-02: Kiểm tra giá hợp lệ
# =========================

def ac02_kiem_tra_gia(gia):
    if not gia.isdigit():
        return False, "❌ Giá phải là số"
    if int(gia) <= 0:
        return False, "❌ Giá phải lớn hơn 0"
    return True, ""

def ac02_them_mon():
    print("\n--- AC-02: Kiểm tra giá hợp lệ ---")
    ten_mon = input("Nhập tên món: ")
    gia = input("Nhập giá: ")
    loai_mon = input("Nhập loại món: ")

    hop_le, thong_bao = ac01_kiem_tra_thong_tin_trong(ten_mon, gia, loai_mon)
    if not hop_le:
        print(thong_bao)
        return

    hop_le, thong_bao = ac02_kiem_tra_gia(gia)
    if not hop_le:
        print(thong_bao)
        print("❌ Không cho phép lưu")
        return

    print("✔ Giá hợp lệ")

    # =========================
# AC-03: Thêm món thành công
# =========================

def ac03_them_mon_thanh_cong():
    print("\n--- AC-03: Thêm món thành công ---")
    ten_mon = input("Nhập tên món: ")
    gia = input("Nhập giá: ")
    loai_mon = input("Nhập loại món: ")

    hop_le, thong_bao = ac01_kiem_tra_thong_tin_trong(ten_mon, gia, loai_mon)
    if not hop_le:
        print(thong_bao)
        return

    hop_le, thong_bao = ac02_kiem_tra_gia(gia)
    if not hop_le:
        print(thong_bao)
        return

    mon_moi = {
        "ten_mon": ten_mon,
        "gia": int(gia),
        "loai_mon": loai_mon
    }

    thuc_don.append(mon_moi)
    print("✔ Thêm món vào thực đơn thành công")

# =========================
# AC-04: Hiển thị món trong danh sách
# =========================

def ac04_hien_thi_thuc_don():
    print("\n--- AC-04: Danh sách thực đơn ---")
    if not thuc_don:
        print("📭 Thực đơn hiện đang trống")
        return

    for i, mon in enumerate(thuc_don, start=1):
        print(f"{i}. {mon['ten_mon']} - {mon['gia']}đ - {mon['loai_mon']}")

