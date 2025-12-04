class TableManager:
    REQUIRED_FIELDS = ['table_name', 'capacity', location_id']

    def create_table (self, data):
        missing_fields =[]

        for feilds in self.REQUIRED_FIELDS:
            if fields not in data or not data[field]:
                missing_fields.append(field)

        if missing_fields:
            error_msg = f"Lỗi: Các trường bắt buộc bị thiếu hoặc để trống: {', '.join(missing_fields)}"
            return False, error_msg
        if self.check_duplicate(data['table_name']):
            return False, "Lỗi: tên bàn đã tồn tại. Vui lòng chọn tên khác"

        print(f"DEBUG: Data hợp lệ: {data}")
        return True, f"Tạo bàn '{data['table_name']}' thành công"

    def check_duplicate(self, table_name):
        if table_name == 'A99':
            return True
        return False
        