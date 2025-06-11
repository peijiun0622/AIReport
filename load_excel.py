import pandas as pd
import tkinter as tk
from tkinter import filedialog, ttk

# 模擬檔案名稱（你可改成自動讀資料夾內容）
file_names = [
    "1114CKNL-3c.txt",
    "1114CKNL-3d.txt",
    "1114CKNL-3e.txt",
    "1114CKNP-52.txt",
    "1114CKNP-A.txt"
]

# 從檔名中提取前綴（例如：1114）
def get_prefixes(names):
    return sorted(set(name[:4] for name in names))

# 提取不含前綴的簡稱（例如：CKNL-3c）
def strip_prefix(name, prefix):
    return name.replace(prefix, "").replace(".txt", "")

# 載入 Excel 並對應簡稱
def load_excel():
    file_path = filedialog.askopenfilename(filetypes=[("C:/Users/user/eclipse-workspace/AIReport/input_DATA/11403labor", "*.xlsx *.xls")])
    if file_path:
        df = pd.read_excel(file_path)
        mapping.clear()
        for _, row in df.iterrows():
            mapping[str(row["檔名簡稱"])] = row["繳款單檔名"]
        update_table()

# 更新資料顯示
def update_table(*args):
    selected_prefix = prefix_var.get()
    for row in tree.get_children():
        tree.delete(row)
    
    for name in file_names:
        if name.startswith(selected_prefix):
            short_name = strip_prefix(name, selected_prefix)
            matched = mapping.get(short_name, "❌ 無對應")
            tree.insert("", "end", values=(name, short_name, matched))

# 建立 GUI
root = tk.Tk()
root.title("檔案對應繳款單工具")
root.geometry("700x400")

# 下拉式選單
prefix_var = tk.StringVar()
prefix_menu = ttk.Combobox(root, textvariable=prefix_var, values=get_prefixes(file_names))
prefix_menu.bind("<<ComboboxSelected>>", update_table)
prefix_menu.pack(pady=10)

# 載入 Excel 按鈕
load_btn = tk.Button(root, text="載入 Excel 簡稱對應表", command=load_excel)
load_btn.pack()

# Treeview 表格
columns = ("原始檔案", "簡稱", "繳款單檔名")
tree = ttk.Treeview(root, columns=columns, show="headings")
for col in columns:
    tree.heading(col, text=col)
    tree.column(col, width=200)
tree.pack(expand=True, fill='both')

# 對應字典
mapping = {}

root.mainloop()