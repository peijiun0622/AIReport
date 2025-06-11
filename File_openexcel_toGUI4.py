import pandas as pd
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

# 模擬讀取 Excel 的繳款單檔名
filenames = [
    "amf0340_1_hinet.rar",
    "amf0340_2_hinet.rar",
    "amf0340_3a_hinet.rar",
    "amf0340_3c_hinet.rar",
    "amf0340_3d_hinet.rar",
    "amf0340_3e_hinet.rar",
    "amf0340_5_2_hinet.rar",
    "amf0340_6_hinet.rar"
]

# 建立主視窗
root = tk.Tk()
root.title("繳款單輸入介面")
root.geometry("600x600")

canvas = tk.Canvas(root)
scrollbar = ttk.Scrollbar(root, orient="vertical", command=canvas.yview)
scrollable_frame = ttk.Frame(canvas)

scrollable_frame.bind(
    "<Configure>",
    lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
)

canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
canvas.configure(yscrollcommand=scrollbar.set)

canvas.pack(side="left", fill="both", expand=True)
scrollbar.pack(side="right", fill="y")

entry_vars = {}

def validate_numeric(P):
    return P.isdigit() or P == ""

vcmd = (root.register(validate_numeric), '%P')

for name in filenames:
    row = ttk.Frame(scrollable_frame)
    row.pack(fill="x", pady=5, padx=10)

    # 標籤
    ttk.Label(row, text=name, width=30).pack(side="left")

    # 狀態下拉式選單
    combo_var = tk.StringVar()
    combo = ttk.Combobox(row, textvariable=combo_var, values=["OK", "缺件", "錯誤", "補件中"], width=10)
    combo.set("OK")
    combo.pack(side="left", padx=5)

    # 數值輸入框
    number_var = tk.StringVar()
    entry = ttk.Entry(row, textvariable=number_var, width=10, validate="key", validatecommand=vcmd)
    entry.pack(side="left", padx=5)

    entry_vars[name] = {
        "狀態": combo_var,
        "件數": number_var
    }

# 送出按鈕
def on_submit():
    results = []
    for name, fields in entry_vars.items():
        status = fields["狀態"].get()
        count = fields["件數"].get()
        results.append({
            "繳款單檔名": name,
            "狀態": status,
            "件數": count
        })

    df = pd.DataFrame(results)

    # 儲存成 Excel 與 CSV
    df.to_excel("output_result.xlsx", index=False)
    df.to_csv("output_result.csv", index=False, encoding='utf-8-sig')

    messagebox.showinfo("送出成功", "資料已儲存為 Excel 與 CSV！")

ttk.Button(root, text="送出", command=on_submit).pack(pady=10)

root.mainloop()