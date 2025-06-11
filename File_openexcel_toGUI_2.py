import pandas as pd
import tkinter as tk
from tkinter import ttk

# 讀取 Excel 檔案
df = pd.read_excel("C:/Users/user/eclipse-workspace/AIReport/input_DATA/11403labor.xls")

# 取得非空白的繳款單檔名
filenames = df["繳款單檔名"].dropna().tolist()

# 建立主視窗
root = tk.Tk()
root.title("繳款單檔名輸入")
root.geometry("500x600")

# 標題
ttk.Label(root, text="繳款單檔名與輸入框", font=("Arial", 14, "bold")).pack(pady=10)

# 使用 Frame 來放置每一列 Label + Entry
container = ttk.Frame(root)
container.pack(fill="both", expand=True, padx=20)

# 字典：儲存每個輸入框對應的變數
entry_vars = {}

# 為每個檔名建立一組 Label 和 Entry
for name in filenames:
    row = ttk.Frame(container)
    row.pack(fill="x", pady=3)

    # 標籤：顯示檔名
    label = ttk.Label(row, text=name, width=30)
    label.pack(side="left")

    # 輸入框：可輸入數值或文字
    var = tk.StringVar()
    entry = ttk.Entry(row, textvariable=var, width=20)
    entry.pack(side="left")

    # 存進字典（方便日後取得使用者輸入）
    entry_vars[name] = var

# 執行主迴圈
root.mainloop()