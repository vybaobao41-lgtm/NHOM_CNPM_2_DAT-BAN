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
import datetime

# --- Dữ liệu Mẫu (Bạn thay thế bằng cách lấy dữ liệu đặt bàn thực tế của bạn) ---
# Giả sử đây là dữ liệu bạn nhận được từ database hoặc file
SAMPLE_BOOKINGS = [
    {
        'table_id': 1,
        'name': 'Anh Khoa',
        # Đặt từ 3:00 PM đến 4:00 PM hôm nay
        'start_time': '2025-12-13 15:00:00',
        'end_time': '2025-12-13 16:00:00'
    },
    {
        'table_id': 2,
        'name': 'Chị Lan',
        # Đặt từ 4:30 PM đến 5:30 PM hôm nay
        'start_time': '2025-12-13 16:30:00',
        'end_time': '2025-12-13 17:30:00'
    },
    {
        'table_id': 3,
        'name': 'Chị Mai',
        # Đặt lúc 10:00 AM sáng hôm sau (Thời gian trong tương lai)
        'start_time': '2025-12-14 10:00:00',
        'end_time': '2025-12-14 12:00:00'
    },
]

# Tên file hoặc nguồn dữ liệu đặt bàn của bạn
BOOKING_DATA_SOURCE = SAMPLE_BOOKINGS 


# --------------------------------------------------------------------------
# Hàm Chính: Kiểm tra trạng thái của một bàn cụ thể
# --------------------------------------------------------------------------
def get_table_status(table_id):
    """
    Kiểm tra trạng thái hiện tại của một bàn dựa trên thời gian thực.
    
    Returns: 
        str: 'ĐANG SỬ DỤNG', 'ĐÃ ĐẶT (Chờ)', hoặc 'TRỐNG'
    """
    
    # Lấy thời gian hiện tại
    # LƯU Ý: Nếu múi giờ khác nhau, bạn cần xử lý múi giờ để đảm bảo chính xác
    current_time = datetime.datetime.now()
    
    # Lấy dữ liệu đặt bàn (Bạn thay thế bằng hàm load data thực tế của mình)
    all_bookings = BOOKING_DATA_SOURCE 
    
    # Lọc các lần đặt bàn cho bàn này
    table_bookings = [
        b for b in all_bookings if b.get('table_id') == table_id
    ]
    
    # Kiểm tra trạng thái
    for booking in table_bookings:
        # Giả định format là 'YYYY-MM-DD HH:MM:SS'
        TIME_FORMAT = '%Y-%m-%d %H:%M:%S'
        
        try:
            # Chuyển chuỗi thời gian sang đối tượng datetime để so sánh
            start_time = datetime.datetime.strptime(booking['start_time'], TIME_FORMAT)
            end_time = datetime.datetime.strptime(booking['end_time'], TIME_FORMAT)
        except (ValueError, KeyError):
            # Bỏ qua nếu dữ liệu bị lỗi format hoặc thiếu key
            continue 

        # 1. Trạng thái ĐANG SỬ DỤNG (Thời gian hiện tại nằm giữa thời gian bắt đầu và kết thúc)
        if start_time <= current_time < end_time:
            return "ĐANG SỬ DỤNG"
        
        # 2. Trạng thái ĐÃ ĐẶT (Chờ) (Thời gian đặt bàn là trong tương lai)
        elif start_time > current_time:
            # Nếu có một lần đặt trong tương lai, báo là đã đặt
            return "ĐÃ ĐẶT (Chờ)"
            
    # 3. Trạng thái TRỐNG (Không có lần đặt nào thỏa mãn các điều kiện trên)
    return "TRỐNG"


# --- Ví dụ về cách sử dụng (bạn có thể xóa sau khi tích hợp) ---
if __name__ == '__main__':
    # Giả sử bạn có 3 bàn
    print(f"Trạng thái Bàn 1: {get_table_status(1)}") 
    print(f"Trạng thái Bàn 2: {get_table_status(2)}") 
    print(f"Trạng thái Bàn 3: {get_table_status(3)}")