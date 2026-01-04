# =========================
# AC-01: Hiển thị thông tin món cần cập nhật
# =========================

class MonAn:
    def __init__(self, ten, gia, loai):
        self.ten = ten
        self.gia = gia
        self.loai = loai

    def hien_thi(self):
        print(f"Tên món: {self.ten} | Giá: {self.gia} | Loại: {self.loai}")


# Danh sách thực đơn ban đầu (nhiều món)
thuc_don = [
    MonAn("Cơm gà", 35000, "Món chính"),
    MonAn("Bún bò", 40000, "Món chính"),
    MonAn("Phở bò", 45000, "Món chính"),
    MonAn("Cơm sườn", 50000, "Món chính"),
    MonAn("Gà chiên nước mắm", 60000, "Món chính"),

    MonAn("Trà đá", 5000, "Nước uống"),
    MonAn("Trà đào", 25000, "Nước uống"),
    MonAn("Nước cam", 30000, "Nước uống"),

    MonAn("Bánh flan", 20000, "Tráng miệng"),
    MonAn("Rau câu", 15000, "Tráng miệng")
]

def hien_thi_thuc_don():
    print("\n--- DANH SÁCH THỰC ĐƠN ---")
    for i, mon in enumerate(thuc_don, start=1):
        print(f"{i}. ", end="")
        mon.hien_thi()


# Chạy thử AC-01
hien_thi_thuc_don()
