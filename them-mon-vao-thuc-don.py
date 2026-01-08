# =========================
# US-11 — THÊM MÓN VÀO THỰC ĐƠN
# Đọc / Ghi: THUCDON.json
# =========================

import json
import os

FILE_NAME = "THUCDON.json"

# =========================
# XỬ LÝ FILE & DỮ LIỆU
# =========================

def chuan_hoa_thuc_don(ds):
    ket_qua = []
    for mon in ds:
        ket_qua.append({
            "ten_mon": mon.get("ten_mon") or mon.get("ten") or mon.get("name") or "Chưa đặt tên",
            "gia": mon.get("gia") or mon.get("price") or mon.get("don_gia") or 0,
            "loai_mon": mon.get("loai_mon") or mon.get("loai") or mon.get("category") or "Chưa phân loại"
        })
    return ket_qua


def doc_thuc_don():
    if not os.path.exists(FILE_NAME):
        return []
    with open(FILE_NAME, "r", encoding="utf-8") as f:
        return chuan_hoa_thuc_don(json.load(f))


def luu_thuc_don(ds):
    with open(FILE_NAME, "w", encoding="utf-8") as f:
        json.dump(ds, f, ensure_ascii=False, indent=4)


# =========================
# VALIDATION (AC-01 + AC-02)
# =========================

def kiem_tra(ten, gia, loai):
    if not ten.strip():
        return False, "❌ Tên món không được để trống"
    if not gia.isdigit() or int(gia) <= 0:
        return False, "❌ Giá phải là số > 0"
    if not loai.strip():
        return False, "❌ Loại món không được để trống"
    return True, ""


# =========================
# AC-03: THÊM MÓN
# =========================

def them_mon():
    thuc_don = doc_thuc_don()

    so_mon = input("Nhập số món muốn thêm: ")
    if not so_mon.isdigit() or int(so_mon) <= 0:
        print("❌ Số món không hợp lệ")
        return

    for i in range(int(so_mon)):
        print(f"\nMón {i + 1}:")
        ten = input("Tên món: ")
        gia = input("Giá: ")
        loai = input("Loại món: ")

        hop_le, tb = kiem_tra(ten, gia, loai)
        if not hop_le:
            print(tb)
            continue

        thuc_don.append({
            "ten_mon": ten.strip(),
            "gia": int(gia),
            "loai_mon": loai.strip()
        })

        print("✔ Đã thêm")

    luu_thuc_don(thuc_don)
    print("\n✅ Lưu thành công vào THUCDON.json")


# =========================
# AC-04: HIỂN THỊ (GỌN)
# =========================

def hien_thi():
    ds = doc_thuc_don()
    if not ds:
        print("📭 Thực đơn trống")
        return

    print("\n--- THỰC ĐƠN ---")
    for i, mon in enumerate(ds, 1):
        print(f"{i}. {mon['ten_mon']} - {mon['gia']}đ")


# =========================
# MENU
# =========================

if __name__ == "__main__":
    while True:
        print("\n=== US-11: THÊM MÓN VÀO THỰC ĐƠN ===")
        print("1. Thêm món")
        print("2. Xem thực đơn")
        print("0. Thoát")

        chon = input("Chọn: ")

        if chon == "1":
            them_mon()
        elif chon == "2":
            hien_thi()
        elif chon == "0":
            break
        else:
            print("❌ Lựa chọn không hợp lệ")
