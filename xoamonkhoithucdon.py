import json
import os
import tkinter as tk
from tkinter import messagebox

# File thực đơn
FILE_MENU = "menu.json"

class XoaMonGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Quản lý thực đơn - Xóa món")
        self.root.geometry("600x400")

        self.thuc_don = []

        self.tao_giao_dien()
        self.tai_du_lieu()

    # Tạo giao diện GUI
    def tao_giao_dien(self):
        tk.Label(self.root, text="DANH SÁCH THỰC ĐƠN", font=("Arial", 14, "bold")).pack(pady=10)

        self.listbox = tk.Listbox(self.root, width=80, height=15)
        self.listbox.pack(padx=10, pady=5)

        self.btn_xoa = tk.Button(
            self.root,
            text="🗑 Xóa món đã chọn",
            bg="#ff6b6b",
            fg="white",
            font=("Arial", 12, "bold"),
            command=self.xoa_mon
        )
        self.btn_xoa.pack(pady=10)

    # Tải dữ liệu từ file menu.json
    def tai_du_lieu(self):
        if not os.path.exists(FILE_MENU):
            messagebox.showerror("Lỗi", f"Không tìm thấy file {FILE_MENU}")
            return

        try:
            with open(FILE_MENU, "r", encoding="utf-8") as f:
                self.thuc_don = json.load(f)
        except Exception as e:
            messagebox.showerror("Lỗi", f"Không thể đọc file {FILE_MENU}\nChi tiết: {e}")
            return

        self.cap_nhat_listbox()

    # Cập nhật listbox
    def cap_nhat_listbox(self):
        self.listbox.delete(0, tk.END)
        for mon in self.thuc_don:
            dong = f"{mon['ten']} | {mon['danh_muc']} | {mon['gia']} VND"
            self.listbox.insert(tk.END, dong)

    # Xóa món đã chọn
    def xoa_mon(self):
        chon = self.listbox.curselection()
        if not chon:
            messagebox.showwarning("Cảnh báo", "Vui lòng chọn món cần xóa")
            return

        index = chon[0]
        mon = self.thuc_don[index]

        xac_nhan = messagebox.askyesno(
            "Xác nhận xóa",
            f"Bạn có chắc chắn muốn xóa món:\n\n"
            f"Tên: {mon['ten']}\n"
            f"Danh mục: {mon['danh_muc']}\n"
            f"Giá: {mon['gia']} VND"
        )

        if not xac_nhan:
            return

        try:
            # Xóa món khỏi danh sách
            self.thuc_don.pop(index)
            # Ghi lại file menu.json
            with open(FILE_MENU, "w", encoding="utf-8") as f:
                json.dump(self.thuc_don, f, ensure_ascii=False, indent=4)

            self.cap_nhat_listbox()
            messagebox.showinfo("Thành công", "Đã xóa món khỏi thực đơn")

        except Exception as e:
            messagebox.showerror("Lỗi", f"Không thể xóa món.\nChi tiết: {e}")


if __name__ == "__main__":
    root = tk.Tk()
    app = XoaMonGUI(root)
    root.mainloop()
