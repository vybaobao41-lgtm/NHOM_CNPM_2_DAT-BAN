menu = []

def them_mon(name, price, category):
    # AC02: kiểm tra thiếu thông tin
    if not name or not price or not category:
        return "Lỗi: Thiếu thông tin bắt buộc"

    item = {
        "name": name,
        "price": price,
        "category": category
    }
    menu.append(item)
    return "Thêm món thành công"
