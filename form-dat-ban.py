import tkinter as tk
from tkinter import messagebox

# ======= DATA GIẢ LẬP: Danh sách bàn đang có =======
danh_sach_ban = []   # Mỗi bàn = {"id": 1, "ngay": "...", "gio": "...", "so_nguoi": 4, "trang_thai": "Trống"}


# FORM SƠ ĐỒ BÀN
def mo_so_do_ban():
    so_do = tk.Toplevel()
    so_do.title("Sơ đồ bàn ăn")
    so_do.geometry("500x400")

    tk.Label(so_do, text="SƠ ĐỒ BÀN ĂN", font=("Arial",20,"bold")).pack(pady=10)

    frame = tk.Frame(so_do)
    frame.pack()

    # Vẽ từng bàn
    for ban in danh_sach_ban:
        btn = tk.Button(frame,
            text=f"Bàn {ban['id']}\n({ban['trang_thai']})",
            width=12, height=4,
            command=lambda b=ban: xu_ly_ban_duoc_chon(b)
        )
        btn.pack(pady=5)


def xu_ly_ban_duoc_chon(ban):
    chon = messagebox.askquestion(
        "Chọn chức năng",
        f"Bạn muốn làm gì với Bàn {ban['id']}?\nTrạng thái: {ban['trang_thai']}",
        icon='question'
    )

    if chon == "yes":
        messagebox.showinfo("Order", f"Đi tới màn hình tạo order cho Bàn {ban['id']}")
    else:
        messagebox.showinfo("Đặt trước", f"Đi tới màn hình đặt trước cho Bàn {ban['id']}")

# FORM TẠO BÀN MỚI
def mo_form_dat_ban():
    form = tk.Toplevel()
    form.title("Tạo Bàn Mới")
    form.geometry("400x300")

    tk.Label(form, text="TẠO BÀN MỚI", font=("Arial",18,"bold")).pack(pady=10)

    tk.Label(form, text="Ngày:").pack()
    entry_ngay = tk.Entry(form)
    entry_ngay.pack()

    tk.Label(form, text="Giờ:").pack()
    entry_gio = tk.Entry(form)
    entry_gio.pack()

    tk.Label(form, text="Số người:").pack()
    entry_so = tk.Entry(form)
    entry_so.pack()

    def tao_ban():
        ngay = entry_ngay.get()
        gio = entry_gio.get()
        so = entry_so.get()

        if not ngay or not gio or not so:
            messagebox.showwarning("Thiếu thông tin", "Vui lòng nhập đầy đủ thông tin!")
            return

        # Tạo ID bàn mới
        id_ban = len(danh_sach_ban) + 1

        # Thêm vào danh sách
        danh_sach_ban.append({
            "id": id_ban,
            "ngay": ngay,
            "gio": gio,
            "so_nguoi": so,
            "trang_thai": "Trống"
        })

        messagebox.showinfo("Thành công", f"Tạo bàn {id_ban} thành công!")

        form.destroy()  # tắt form tạo bàn
        mo_so_do_ban()  # quay về sơ đồ bàn như yêu cầu

    tk.Button(form, text="Tạo bàn", command=tao_ban).pack(pady=20)

# GIAO DIỆN CHÍNH
root = tk.Tk()
root.title("Quản lý nhà hàng")
root.geometry("400x300")

tk.Label(root, text="QUẢN LÝ NHÀ HÀNG", font=("Arial",20,"bold")).pack(pady=20)

tk.Button(root, text="Tạo Bàn Mới", width=20, height=2, command=mo_form_dat_ban).pack(pady=10)
tk.Button(root, text="Xem Sơ Đồ Bàn", width=20, height=2, command=mo_so_do_ban).pack(pady=10)

root.mainloop()
