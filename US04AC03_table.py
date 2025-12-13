# table_manager.py

tables = [
    {"name": "B1", "capacity": 4, "area": "Trong nhà", "status": "TRỐNG"},
    {"name": "B2", "capacity": 6, "area": "Ngoài trời", "status": "ĐÃ ĐẶT"},
    {"name": "VIP1", "capacity": 10, "area": "VIP", "status": "TRỐNG"},
    {"name": "B3", "capacity": 4, "area": "Trong nhà", "status": "ĐANG DÙNG"},
]

def filter_tables(status=None, capacity=None, area=None, name=None):
    result = tables

    if status:
        result = [t for t in result if t["status"] == status]

    if capacity:
        result = [t for t in result if t["capacity"] == capacity]

    if area:
        result = [t for t in result if t["area"] == area]

    if name:
        result = [t for t in result if name.lower() in t["name"].lower()]

    return result
