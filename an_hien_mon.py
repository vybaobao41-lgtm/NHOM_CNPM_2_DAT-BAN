# -------------------------
# CLASS MÓN ĂN
# -------------------------
class MonAn:
    def __init__(self, ten_mon, gia, loai_mon, dang_ban=True):
        self.ten_mon = ten_mon      # Tên món
        self.gia = gia              # Giá món
        self.loai_mon = loai_mon    # Loại món (Món chính, Đồ uống...)
        self.dang_ban = dang_ban    # True = đang bán, False = ngừng bán

    def trang_thai(self):
        """Trả về trạng thái món ăn"""
        return "Đang bán" if self.dang_ban else "Ngừng bán"