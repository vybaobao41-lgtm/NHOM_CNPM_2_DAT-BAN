from datetime import datetime, timedelta
import random

# =========================
# DỮ LIỆU GIẢ LẬP MỞ RỘNG
# =========================

reservations = [
    # 3 bản ghi gốc
    {
        "customer": "Nguyen Van A",
        "phone": "0901234567",
        "guests": 4,
        "table": "B1",
        "start": datetime.now() + timedelta(minutes=10),
        "end": datetime.now() + timedelta(hours=2, minutes=10),
        "note": "Sinh nhật, cần trang trí",
        "status": "Chưa đến"
    },
    {
        "customer": "Tran Van B",
        "phone": "0911111111",
        "guests": 2,
        "table": "B2",
        "start": datetime.now() + timedelta(minutes=40),
        "end": datetime.now() + timedelta(hours=2, minutes=40),
        "note": "",
        "status": "Chưa đến"
    },
    {
        "customer": "Le Thi C",
        "phone": "0922222222",
        "guests": 3,
        "table": "B3",
        "start": datetime.now() + timedelta(minutes=20),
        "end": datetime.now() + timedelta(hours=2, minutes=20),
        "note": "Yêu cầu món chay",
        "status": "Đã check-in"
    },
]

# Tạo thêm 20 bản ghi giả lập
names = ["Pham Van D", "Nguyen Thi E", "Hoang Van F", "Le Van G", "Tran Thi H",
         "Nguyen Van I", "Pham Thi J", "Le Thi K", "Tran Van L", "Hoang Thi M",
         "Nguyen Van N", "Pham Van O", "Le Van P", "Tran Thi Q", "Hoang Van R",
         "Nguyen Thi S", "Pham Van T", "Le Thi U", "Tran Van V", "Hoang Thi W"]

notes = ["", "Yêu cầu món chay", "Sinh nhật", "Gặp đối tác", "Cần bàn gần cửa sổ"]

for i in range(20):
    start_offset = random.randint(0, 120)  # 0 đến 120 phút từ bây giờ
    duration = random.randint(60, 150)  # thời gian đặt bàn 1-2.5 giờ
    reservations.append({
        "customer": names[i],
        "phone": f"09{random.randint(10000000, 99999999)}",
        "guests": random.randint(1, 6),
        "table": f"B{i+4}",
        "start": datetime.now() + timedelta(minutes=start_offset),
        "end": datetime.now() + timedelta(minutes=start_offset + duration),
        "note": random.choice(notes),
        "status": random.choice(["Chưa đến", "Đã check-in", "Đã hủy"])
    })

# =========================
# LẤY DANH SÁCH SẮP ĐẾN
# =========================
# =========================
# LẤY DANH SÁCH SẮP ĐẾN (nhập từ bàn phím)
# =========================
def get_upcoming_reservations_from_input():
    while True:
        try:
            minutes = int(input("Nhập số phút muốn kiểm tra bàn sắp đến: "))
            if minutes <= 0:
                print("❌ Vui lòng nhập số phút > 0.")
                continue
            break
        except ValueError:
            print("❌ Vui lòng nhập một số nguyên hợp lệ.")

    now = datetime.now()
    end_window = now + timedelta(minutes=minutes)
    upcoming = [
        r for r in reservations
        if r["status"] == "Chưa đến" and now <= r["start"] <= end_window
    ]
    upcoming.sort(key=lambda x: x["start"])
    return upcoming


# =========================
# IN BẢNG ASCII
# =========================
def print_reservations_table(res_list, title="Danh sách"):
    if not res_list:
        print("❌ Không có bàn sắp đến")
        return

    # Chuẩn bị dữ liệu
    rows = []
    for r in res_list:
        rows.append([
            r["table"],
            r["customer"],
            r["phone"],
            r["guests"],
            r["start"].strftime("%H:%M"),
            r["end"].strftime("%H:%M"),
            r["status"],
            r["note"]
        ])

    headers = ["Bàn", "Khách", "SĐT", "Số khách", "Bắt đầu", "Kết thúc", "Trạng thái", "Ghi chú"]

    # Tính chiều rộng từng cột
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

    # In bảng
    print(f"\n--- {title} ---")
    print_line()
    print_row(headers)
    print_line()
    for row in rows:
        print_row(row)
        print_line()

# =========================
# Demo / test
# =========================
if __name__ == "__main__":
    upcoming = get_upcoming_reservations_from_input()
    print_reservations_table(upcoming, title="ĐẶT BÀN SẮP ĐẾN")
