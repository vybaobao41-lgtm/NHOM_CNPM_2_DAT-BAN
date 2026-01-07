from datetime import datetime
from collections import defaultdict

# ===============================
# DỮ LIỆU ĐẶT BÀN GIẢ LẬP
# ===============================
reservations = [
    {"date": "2026-01-01", "status": "BOOKED"},
    {"date": "2026-01-01", "status": "CHECKED_IN"},
    {"date": "2026-01-02", "status": "BOOKED"},
    {"date": "2026-01-02", "status": "CANCELED"},
    {"date": "2026-01-03", "status": "CHECKED_IN"},
]


# ===============================
# KIỂM TRA TRẠNG THÁI HỢP LỆ
# ===============================
def is_valid_status(status):
    return status in ["BOOKED", "CHECKED_IN"]


# ===============================
# PARSE NGÀY AN TOÀN
# ===============================
def parse_date(date_str):
    """
    Chỉ lấy 10 ký tự đầu tiên (YYYY-MM-DD)
    Tránh lỗi 'unconverted data remains'
    """
    return datetime.strptime(date_str.strip()[:10], "%Y-%m-%d")


# ===============================
# HÀM BÁO CÁO SỐ LƯỢNG ĐẶT BÀN
# ===============================
def bao_cao_so_luong_dat_ban(start_date, end_date):
    start = parse_date(start_date)
    end = parse_date(end_date)

    tong_so_luot = 0
    thong_ke_theo_ngay = defaultdict(int)

    for r in reservations:
        ngay_dat = parse_date(r["date"])

        if start <= ngay_dat <= end and is_valid_status(r["status"]):
            tong_so_luot += 1
            thong_ke_theo_ngay[r["date"]] += 1

    return tong_so_luot, thong_ke_theo_ngay


# ===============================
# CHẠY CHƯƠNG TRÌNH
# ===============================
if __name__ == "__main__":
    print("=== BÁO CÁO SỐ LƯỢNG ĐẶT BÀN ===")

    start_date = input("Nhập ngày bắt đầu (YYYY-MM-DD): ")
    end_date = input("Nhập ngày kết thúc (YYYY-MM-DD): ")

    try:
        tong, chi_tiet = bao_cao_so_luong_dat_ban(start_date, end_date)

        print("\n--- KẾT QUẢ BÁO CÁO ---")
        print(f"Tổng số lượt đặt bàn: {tong}")

        if tong == 0:
            print("Không có dữ liệu trong khoảng thời gian này.")
        else:
            print("Chi tiết theo ngày:")
            for ngay, so_luong in sorted(chi_tiet.items()):
                print(f"- {ngay}: {so_luong} lượt")

    except ValueError:
        print("❌ Sai định dạng ngày. Vui lòng nhập đúng YYYY-MM-DD.")
