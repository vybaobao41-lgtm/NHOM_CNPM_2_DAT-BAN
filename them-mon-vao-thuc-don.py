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
