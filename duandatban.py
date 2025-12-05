import tkinter as tk
from tkinter import messagebox

def dat_ban():
    ngay = entry_ngay.get().strip()
    gio = entry_gio.get().strip()
    so_nguoi = entry_so_nguoi.get().strip()

    # Kiểm tra dữ liệu
    if not ngay or not gio or not so_nguoi:
        return messagebox.showwarning("Thiếu thông tin", "Vui lòng nhập đầy đủ thông tin!")

    if not so_nguoi.isdigit() or int(so_nguoi) <= 0:
        return messagebox.showerror("Lỗi", "Số người phải là số dương!")

    messagebox.showinfo("Thành công", "Đặt bàn thành công!")

# Giao diện
root = tk.Tk()
root.title("Form Đặt Bàn")
root.geometry("320x240")
root.configure(bg="#f4f4f4")

font = ("Arial", 11)

tk.Label(root, text="Ngày (YYYY-MM-DD):", bg="#f4f4f4", font=font).pack(anchor="w", padx=15, pady=5)
entry_ngay = tk.Entry(root, font=font)
entry_ngay.pack(padx=15, fill="x")

tk.Label(root, text="Giờ (HH:MM):", bg="#f4f4f4", font=font).pack(anchor="w", padx=15, pady=5)
entry_gio = tk.Entry(root, font=font)
entry_gio.pack(padx=15, fill="x")

tk.Label(root, text="Số người:", bg="#f4f4f4", font=font).pack(anchor="w", padx=15, pady=5)
entry_so_nguoi = tk.Entry(root, font=font)
entry_so_nguoi.pack(padx=15, fill="x")

btn = tk.Button(root, text="Đặt bàn", font=("Arial", 12, "bold"),
                bg="#4CAF50", fg="white", padx=10, pady=5, command=dat_ban)
btn.pack(pady=15)

root.mainloop()
