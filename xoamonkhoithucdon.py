import pandas as pd
import tkinter as tk
from tkinter import messagebox, ttk

FILE_PATH = "THUCDON.xlsx"

TEN_MON_COL = "TÊN MÓN"
DANH_MUC_COL = "DANH MỤC"
GIA_COL = "GIÁ TIỀN (VND)"


def doc_thuc_don():
    try:
        df = pd.read_excel(FILE_PATH)
        for col in [TEN_MON_COL, DANH_MUC_COL, GIA_COL]:
            if col not in df.columns:
                raise ValueError
        return df
    except FileNotFoundError:
        messagebox.showerror("Lỗi", "Không tìm thấy file THUCDON.xlsx")
    except ValueError:
        messagebox.showerror(
            "Lỗi",
            "File thực đơn không đúng định dạng.\n"
            "Cần có các cột:\n"
            "- TÊN MÓN\n- DANH MỤC\n- GIÁ TIỀN (VND)"
        )
    return None


def load_danh_sach():
    tree.delete(*tree.get_children())
    df = doc_thuc_don()
    if df is None:
        return
    for _, row in df.iterrows():
        tree.insert("", tk.END, values=(
            row[TEN_MON_COL],
            row[DANH_MUC_COL],
            row[GIA_COL]
        ))


def xoa_mon_da_chon():
    selected = tree.selection()

    if not selected:
        messagebox.showwarning(
            "Cảnh báo",
            "Vui lòng chọn món cần xóa trong danh sách"
        )
        return

    item = tree.item(selected[0])
    ten_mon, danh_muc, gia = item["values"]

    xac_nhan = messagebox.askyesno(
        "Xác nhận xóa",
        f"Bạn có chắc chắn muốn xóa món:\n\n"
        f"{ten_mon}\n"
        f"Danh mục: {danh_muc}\n"
        f"Giá: {gia} VND"
    )

    if not xac_nhan:
        return

    df = doc_thuc_don()
    if df is None:
        return

    try:
        df_moi = df[df[TEN_MON_COL].astype(str) != str(ten_mon)]
        df_moi.to_excel(FILE_PATH, index=False)

        messagebox.showinfo(
            "Thành công",
            "Đã xóa món khỏi thực đơn"
        )
        load_danh_sach()

    except Exception as e:
        messagebox.showerror(
            "Lỗi",
            f"Xóa món thất bại:\n{e}"
        )


# ===== GIAO DIỆN =====
root = tk.Tk()
root.title("Quản lý thực đơn – Xóa món")
root.geometry("820x480")

columns = (TEN_MON_COL, DANH_MUC_COL, GIA_COL)
tree = ttk.Treeview(root, columns=columns, show="headings", height=16)

for col in columns:
    tree.heading(col, text=col)
    tree.column(col, width=300 if col == TEN_MON_COL else 160)

tree.pack(pady=15)

btn_xoa = tk.Button(
    root,
    text="❌ XÓA MÓN ĐÃ CHỌN",
    bg="red",
    fg="white",
    font=("Arial", 11, "bold"),
    width=25,
    command=xoa_mon_da_chon
)
btn_xoa.pack(pady=10)

load_danh_sach()
root.mainloop()
