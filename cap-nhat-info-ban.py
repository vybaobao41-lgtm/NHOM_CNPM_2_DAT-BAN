# ===== US-02: Cập nhật thông tin bàn =====

class Table:
    def __init__(self, table_id, ngay, gio, so_nguoi, trang_thai):
        self.table_id = table_id
        self.ngay = ngay        # yyyy-mm-dd
        self.gio = gio          # hh:mm
        self.so_nguoi = so_nguoi
        self.trang_thai = trang_thai  # Trống / Đang sử dụng / Đã đặt

    def __str__(self):
        return (f"Bàn {self.table_id} | Ngày: {self.ngay} | Giờ: {self.gio} | "
                f"Số người: {self.so_nguoi} | Trạng thái: {self.trang_thai}")


def kiem_tra_hop_le(ngay, gio, so_nguoi, trang_thai):
    """
    AC01 — Kiểm tra tính hợp lệ của thông tin bàn
    """
    if not ngay or not gio:
        return False, "Ngày và giờ không được để trống"

    if so_nguoi <= 0:
        return False, "Số người phải lớn hơn 0"

    if trang_thai not in ["Trống", "Đang sử dụng", "Đã đặt"]:
        return False, "Trạng thái không hợp lệ"

    return True, ""


def cap_nhat_ban(danh_sach_ban, table_id,
                 ngay_moi=None, gio_moi=None,
                 so_nguoi_moi=None, trang_thai_moi=None,
                 huy=False):
    """
    US-02 — Cập nhật thông tin bàn
    AC02 — Cập nhật bàn khi đang sử dụng và đồng bộ realtime
    AC03 — Cập nhật thành công
    AC04 — Hủy cập nhật
    """

    # AC04 — Hủy cập nhật
    if huy:
        print("Đã hủy cập nhật")
        return False

    for ban in danh_sach_ban:
        if ban.table_id == table_id:

            # Giá trị mới (nếu không nhập thì giữ nguyên)
            ngay = ngay_moi if ngay_moi is not None else ban.ngay
            gio = gio_moi if gio_moi is not None else ban.gio
            so_nguoi = so_nguoi_moi if so_nguoi_moi is not None else ban.so_nguoi
            trang_thai = trang_thai_moi if trang_thai_moi is not None else ban.trang_thai

            # AC01 — Kiểm tra hợp lệ
            hop_le, thong_bao = kiem_tra_hop_le(ngay, gio, so_nguoi, trang_thai)
            if not hop_le:
                raise ValueError(thong_bao)

            # AC02 — Cho phép cập nhật cả khi đang sử dụng
            ban.ngay = ngay
            ban.gio = gio
            ban.so_nguoi = so_nguoi
            ban.trang_thai = trang_thai

            # AC03 — Cập nhật thành công (dữ liệu được cập nhật ngay)
            return True

    raise ValueError("Không tìm thấy bàn cần cập nhật")


# ===== Ví dụ sử dụng =====
if __name__ == "__main__":
    danh_sach_ban = [
        Table(1, "2025-12-23", "18:00", 4, "Trống"),
        Table(2, "2025-12-23", "19:00", 2, "Đang sử dụng")
    ]

    print("=== Danh sách bàn ban đầu ===")
    for ban in danh_sach_ban:
        print(ban)

    print("\n=== Cập nhật thông tin bàn ===")
    try:
        cap_nhat_ban(
            danh_sach_ban,
            table_id=2,
            so_nguoi_moi=3,
            trang_thai_moi="Đang sử dụng"
        )
        print("Cập nhật thành công")
    except ValueError as e:
        print("Lỗi:", e)

    print("\n=== Danh sách bàn sau cập nhật ===")
    for ban in danh_sach_ban:
        print(ban)
