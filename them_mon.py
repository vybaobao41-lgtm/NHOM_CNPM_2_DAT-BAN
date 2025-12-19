menu = []

def them_mon(name, price, category):
    # AC02
    if not name or not price or not category:
        return "Lỗi: Thiếu thông tin bắt buộc"

    # AC03
    try:
        price = float(price)
        if price <= 0:
            return "Giá phải lớn hơn 0"
    except ValueError:
        return "Giá phải lớn hơn 0"

    item = {
        "name": name,
        "price": price,
        "category": category
    }
    menu.append(item)
    return "Thêm món thành công"
