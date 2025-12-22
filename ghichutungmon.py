import datetime

# Danh sách lưu nhật ký (AC07)
lich_su_thao_tac = []

print("--- HỆ THỐNG ĐẶT MÓN NHÀ HÀNG ---")
nhan_vien = input("Nhập tên nhân viên đang trực: ")
ten_mon = "Beef Steak"
ghi_chu = ""
da_gui_bep = False

while True:
    print("\n-------------------------------")
    print(f"Món ăn: {ten_mon}")
    # Hiển thị ghi chú ngay dưới món (AC01)
    print(f"Ghi chú: {ghi_chu if ghi_chu != '' else '(Trống)'}")
    print(f"Trạng thái: {'Đã gửi bếp' if da_gui_bep else 'Chờ gửi'}")
    print("-------------------------------")
    print("1. Thêm/Sửa ghi chú")
    print("2. Xóa ghi chú")
    print("3. Gửi order xuống bếp")
    print("4. Xem nhật ký")
    print("5. Thoát")
    
    lua_chon = input("Chọn thao tác (1-5): ")

    if lua_chon == '1':
        # AC01, AC02: Thêm và Sửa ghi chú
        # Given: Nhân viên đang chọn món
        noi_dung = input("Nhập nội dung ghi chú (VD: ít tiêu, không rau thơm có mùi mạnh, không quá nhiều bơ, nước sốt ít ngọt...): ")
        
        # AC06: Kiểm tra dữ liệu (Validation)
        # When: Ghi chú rỗng hoặc quá dài
        if noi_dung == "":
            # Then: Hệ thống báo lỗi
            print(">> Lỗi: Ghi chú không được bỏ trống!")
        elif len(noi_dung) > 50:
            print(">> Lỗi: Ghi chú không được dài quá 50 ký tự!")
        else:
            # Lưu lại thông tin cũ để ghi nhật ký
            ghi_chu_cu = ghi_chu
            ghi_chu = noi_dung # Cập nhật ghi chú mới
            
            # AC07: Lưu nhật ký thao tác
            thoi_gian = datetime.datetime.now().strftime("%H:%M:%S")
            loai_thao_tac = "Sửa" if ghi_chu_cu != "" else "Thêm"
            nhat_ky = f"[{thoi_gian}] {nhan_vien} {loai_thao_tac}: '{ghi_chu_cu}' -> '{ghi_chu}'"
            
            # AC05: Nếu đã gửi bếp mà còn sửa thì đánh dấu
            if da_gui_bep:
                nhat_ky += " (ĐÃ THAY ĐỔI SAU KHI GỬI BẾP)"
            
            lich_su_thao_tac.append(nhat_ky)
            print(">> Cập nhật ghi chú thành công!")

    elif lua_chon == '2':
        # AC03: Xóa ghi chú
        # Given: Món đang có ghi chú
        if ghi_chu == "":
            print(">> Món này hiện chưa có ghi chú nào.")
        else:
            # When: Nhân viên xóa ghi chú
            thoi_gian = datetime.datetime.now().strftime("%H:%M:%S")
            lich_su_thao_tac.append(f"[{thoi_gian}] {nhan_vien} Xóa ghi chú: '{ghi_chu}'")
            
            ghi_chu = "" 
            # Then: Món vẫn giữ nguyên, chỉ mất ghi chú
            print(">> Đã xóa ghi chú. Món ăn vẫn nằm trong đơn hàng.")

    elif lua_chon == '3':
        # AC04: Gửi xuống bếp
        # Given: Order đã xong
        # When: Nhân viên xác nhận gửi
        da_gui_bep = True
        # Then: Bếp nhận được món kèm ghi chú
        print(f">> ĐÃ GỬI XUỐNG BẾP: {ten_mon} - Ghi chú: {ghi_chu}")

    elif lua_chon == '4':
        # AC07: Hiển thị nhật ký
        print("\n--- NHẬT KÝ HỆ THỐNG ---")
        if not lich_su_thao_tac:
            print("Chưa có thao tác nào được thực hiện.")
        else:
            for log in lich_su_thao_tac:
                print(log)

    elif lua_chon == '5':
        print("Đang thoát chương trình...")
        break
    else:
        print(">> Lựa chọn không hợp lệ, vui lòng nhập lại (1-5).")