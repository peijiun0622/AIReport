import pandas as pd
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

# 讀取 Excel 檔案
df = pd.read_excel("C:/Users/user/eclipse-workspace/AIReport/input_DATA/11403labor.xls")

# 取得非空白的繳款單檔名
filenames = df["繳款單檔名"].dropna().tolist()

# 建立主視窗
root = tk.Tk()
root.title("繳款單輸入介面")
root.geometry("600x600")

# 滾動視窗支援（如果檔名很多）
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

# 儲存輸入框變數
entry_vars = {}

# 每個檔名一行 Label + Entry
for name in filenames:
    row = ttk.Frame(scrollable_frame)
    row.pack(fill="x", pady=3, padx=10)

    label = ttk.Label(row, text=name, width=30)
    label.pack(side="left")

    var = tk.StringVar()
    entry = ttk.Entry(row, textvariable=var, width=30)
    entry.pack(side="left")

    entry_vars[name] = var

# 處理送出按鈕的函式
def on_submit():
    result = []
    for name, var in entry_vars.items():
        user_input = var.get()
        result.append((name, user_input))
    
    # 顯示結果（可改為寫入 CSV）
    print("使用者輸入結果：")
    for name, value in result:
        print(f"{name}: {value}")

    messagebox.showinfo("完成", "資料已送出！")

# 送出按鈕
submit_btn = ttk.Button(root, text="送出", command=on_submit)
submit_btn.pack(pady=10)

# 執行主迴圈
root.mainloop()