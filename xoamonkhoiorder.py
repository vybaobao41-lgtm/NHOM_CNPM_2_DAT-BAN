import tkinter as tk
from tkinter import messagebox

# ================= DATA =================
order = []

# ================= FUNCTIONS =================
def add_item():
    try:
        item = {
            "id": int(entry_id.get()),
            "name": entry_name.get(),
            "price": int(entry_price.get()),
            "qty": int(entry_qty.get())
        }
        order.append(item)
        refresh_list()
        clear_entries()
    except ValueError:
        messagebox.showerror("Lỗi", "Vui lòng nhập đúng dữ liệu")

def delete_item():
    selected = listbox.curselection()
    if not selected:
        messagebox.showwarning("Thông báo", "Vui lòng chọn món để xóa")
        return

    index = selected[0]
    item = order[index]

    confirm = messagebox.askyesno(
        "Xác nhận",
        f"Bạn có chắc muốn xóa '{item['name']}'?"
    )

    if confirm:
        order.pop(index)
        refresh_list()

def calculate_total():
    total = sum(i["price"] * i["qty"] for i in order)
    label_total.config(text=f"Tổng tiền: {total:,} VND")

def refresh_list():
    listbox.delete(0, tk.END)
    for item in order:
        listbox.insert(
            tk.END,
            f"{item['id']} | {item['name']} | {item['price']} x {item['qty']}"
        )
    calculate_total()

def clear_entries():
    entry_id.delete(0, tk.END)
    entry_name.delete(0, tk.END)
    entry_price.delete(0, tk.END)
    entry_qty.delete(0, tk.END)

# ================= GUI =================
root = tk.Tk()
root.title("Quản lý Order - Nhà hàng hải sản")
root.geometry("500x450")

# ---- Input ----
tk.Label(root, text="ID món").pack()
entry_id = tk.Entry(root)
entry_id.pack()

tk.Label(root, text="Tên món").pack()
entry_name = tk.Entry(root)
entry_name.pack()

tk.Label(root, text="Giá").pack()
entry_price = tk.Entry(root)
entry_price.pack()

tk.Label(root, text="Số lượng").pack()
entry_qty = tk.Entry(root)
entry_qty.pack()

tk.Button(root, text="➕ Thêm món", command=add_item).pack(pady=5)

# ---- List ----
listbox = tk.Listbox(root, width=60)
listbox.pack(pady=10)

tk.Button(root, text="🗑️ Xóa món", command=delete_item).pack()

# ---- Total ----
label_total = tk.Label(root, text="Tổng tiền: 0 VND", font=("Arial", 12, "bold"))
label_total.pack(pady=10)

root.mainloop()
