import datetime

class DishNoteService:
    def __init__(self):
        self.ten_mon = "Beef Steak"
        self.ghi_chu = ""
        self.da_gui_bep = False
        self.lich_su_thao_tac = [] 
        self.max_length = 50 

    def luu_log(self, thao_tac, noi_dung_cu, noi_dung_moi):
        """Hỗ trợ AC-07: Lưu nhật ký thao tác"""
        thoi_gian = datetime.datetime.now().strftime("%H:%M:%S")
        log = f"[{thoi_gian}] {thao_tac}: '{noi_dung_cu}' -> '{noi_dung_moi}'"
        if self.da_gui_bep:
            log += " (THAY ĐỔI SAU KHI GỬI BẾP - AC-05)"
        self.lich_su_thao_tac.append(log)

def menu_us20():
    service = DishNoteService()
    print("--- HỆ THỐNG GHI CHÚ MÓN ĂN ---")
    nhan_vien = input("Nhập tên nhân viên: ")

    while True:
        print("\n" + "="*55)
        print(f"TRẠNG THÁI: {service.ten_mon} | Ghi chú: {service.ghi_chu or '(Trống)'}")
        print(f"Bếp: {'Đã nhận' if service.da_gui_bep else 'Chờ gửi'}")
        print("="*55)
        print("1. Thêm/chỉnh sửa ghi chú mới cho món")
        print("2. Xóa bỏ ghi chú của món")
        print("3. Gửi ghi chú xuống bếp")
        print("4. Cập nhật ghi chú SAU khi đã gửi bếp")
        print("5. Kiểm tra ràng buộc dữ liệu ")
        print("6. Xem nhật ký thao tác chi tiết")
        print("0. Thoát")
        
        chon = input("\nChọn mục kiểm tra AC (0-6): ")

        if chon == '1':
            if service.ghi_chu:
                print(">> Ghi chú đã tồn tại, vui lòng chọn mục 2 để sửa.")
            else:
                print("Gợi ý: ít rau mùi, không tiêu, chín kỹ, sốt để riêng...")
                nd = input("Nhập ghi chú mới: ").strip()
                if nd:
                    service.luu_log("Thêm mới", "", nd)
                    service.ghi_chu = nd
                    print(">> AC-01: Thêm thành công.")
                else:
                    print("❌ Lỗi: Ghi chú không được để trống!")

        elif chon == '2':
            if not service.ghi_chu:
                print(">> [AC-02] Chưa có ghi chú để sửa, vui lòng chọn mục 1.")
            else:
                print(f"Ghi chú cũ: '{service.ghi_chu}'")
                print("Gợi ý sửa: đổi 'ít tiêu' thành 'không tiêu', thêm 'không hành'...")
                nd = input("Nhập nội dung mới: ").strip()
                if nd:
                    service.luu_log("Chỉnh sửa", service.ghi_chu, nd)
                    service.ghi_chu = nd
                    print(">> AC-02: Sửa thành công.")

        elif chon == '3':
            if service.ghi_chu:
                cu = service.ghi_chu
                service.da_gui_bep = True
                service.luu_log("Gửi bếp", cu, "Đã gửi")
                print(f">> AC-03: Đã gửi xuống bếp '{cu}'. Món ăn vẫn giữ nguyên.")
            else:
                print(">> Chưa có ghi chú để gửi, vui lòng thêm ghi chú trước.")

        elif chon == '4':
            service.da_gui_bep = True
            print(f">> AC-04: Đã gửi lệnh xuống bếp. Bếp nhận được món kèm: {service.ghi_chu or 'Không ghi chú'}")

        elif chon == '5':
            if not service.da_gui_bep:
                print(">> [Lỗi] Phải gửi bếp trước (Mục 4) mới kiểm tra được mục này.")
            else:
                print("Gợi ý cập nhật gấp: Khách đổi ý không lấy hành, bớt cay hơn...")
                nd = input("Cập nhật bổ sung cho bếp: ").strip()
                if nd:
                    cu = service.ghi_chu
                    service.ghi_chu = nd
                    service.luu_log("Cập nhật sau gửi", cu, nd)
                    print(">> AC-05: Đã cập nhật sau gửi bếp thành công.")

        elif chon == '6':
            print(f">> [AC-06] Kiểm tra Validation (Giới hạn {service.max_length} ký tự)")
            nd = input("Thử nhập ghi chú (Trống hoặc > 50 ký tự): ")
            if not nd.strip():
                print("❌ Kết quả: Hệ thống chặn thành công vì để TRỐNG.")
            elif len(nd) > service.max_length:
                print(f"❌ Kết quả: Hệ thống chặn vì QUÁ DÀI ({len(nd)} ký tự).")
            else:
                print("✅ Kết quả: Dữ liệu hợp lệ.")

        elif chon == '7':
            print("\n--- [AC-07] NHẬT KÝ THAO TÁC CHI TIẾT ---")
            for log in service.lich_su_thao_tac:
                print(log)
            if not service.lich_su_thao_tac: print("Chưa có nhật ký.")

        elif chon == '0':
            break

if __name__ == "__main__":
    menu_us20()
    