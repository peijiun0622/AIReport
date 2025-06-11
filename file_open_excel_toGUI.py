import pandas as pd
import tkinter as tk
from tkinter import ttk

# 讀取 Excel 檔案（請改成你的路徑）
df = pd.read_excel("C:/Users/user/eclipse-workspace/AIReport/input_DATA/11403labor.xls")

# 取得繳款單檔名欄位（去掉空白）
filenames = df["繳款單檔名"].dropna().tolist()

# 建立主視窗
root = tk.Tk()
root.title("繳款單檔名顯示")
root.geometry("400x400")

# 加入標題
title_label = ttk.Label(root, text="繳款單檔名列表", font=("Arial", 14, "bold"))
title_label.pack(pady=10)

# 將所有檔名逐一放入 Label
for name in filenames:
    lbl = ttk.Label(root, text=name, font=("Arial", 12))
    lbl.pack(anchor='w', padx=20)

# 啟動 GUI 主迴圈
root.mainloop()
