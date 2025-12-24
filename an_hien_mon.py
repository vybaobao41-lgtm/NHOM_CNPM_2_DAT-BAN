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
    
# -------------------------
# AC-01 — ẨN MÓN
# -------------------------
def an_mon(mon_an):
    """
    Ẩn món: đổi trạng thái sang Ngừng bán
    AC-03 cũng được đảm bảo vì không xóa dữ liệu
    """
    if not mon_an.dang_ban:
        return "⚠ Món đã ngừng bán"
    mon_an.dang_ban = False
    return f"✔ Ẩn món '{mon_an.ten_mon}' thành công"

# -------------------------
# AC-02 — HIỆN MÓN
# -------------------------
def hien_mon(mon_an):
    """Hiện món: đổi trạng thái sang Đang bán"""
    if mon_an.dang_ban:
        return "⚠ Món đang được bán"
    mon_an.dang_ban = True
    return f"✔ Hiện món '{mon_an.ten_mon}' thành công"
