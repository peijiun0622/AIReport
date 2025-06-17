import tkinter as tk
import tkinter.ttk as ttk
import pandas as pd
from tkinter import messagebox
import os
import csv
import re

# 讀取 Excel
df = pd.read_excel("C:/Users/user/eclipse-workspace/AIReport/input_DATA/11405lib.xls")
filenames = df["繳款單檔名"].dropna().tolist()

# 取得資料夾中的所有檔案名稱並建立映射
totalfile = os.listdir("C:/Users/user/eclipse-workspace/AIReport/move_DATA")
result = []
file_mapping = {}  # 建立 result 到 totalfile 的映射
for name in totalfile:
    match = re.match(r'\d{4}(.*)\.txt', name)
    if match:
        extracted = match.group(1)
        result.append(extracted)
        file_mapping[extracted] = name  # 儲存映射，例如 {'CKNL-3c': '0613CKNL-3c.txt'}

# 讀取 labor_CODE.csv
with open('labor_CODE.csv', mode='r', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    data_dict = {row['Filename']: row['Code'] for row in reader}

def save_to_csv():
    output_path = os.path.abspath("output_DATA/selected_output.csv")
    with open(output_path, mode="w", encoding="utf-8-sig", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["繳款單檔名", "選擇的檔案"])
        for filename, combobox in comboboxes.items():
            selected_file = combobox.get()
            writer.writerow([filename, selected_file])
    print(f"已將選擇結果寫入 {output_path}")
    messagebox.showinfo("完成", f"已儲存：\n{output_path}")

# 建立主視窗
root = tk.Tk()
root.title("測試")

# 建立框架
frame1 = ttk.Frame(root)
frame1.pack(padx=10, pady=10)
frame2 = ttk.Frame(root)
frame2.pack(padx=10, pady=10)

# 建立 Label 與 Combobox 的配對
labels = {}
comboboxes = {}

for filename in filenames:
    row_frame = ttk.Frame(frame1)
    row_frame.pack(fill="x", pady=5)
    labels[filename] = ttk.Label(row_frame, text=filename, width=40)
    labels[filename].pack(side="left")
    combobox = ttk.Combobox(row_frame, values=totalfile, width=40)
    combobox.bind("<<ComboboxSelected>>", lambda e: save_to_csv())
    if filename in data_dict:
        default_code = data_dict[filename]
        # 檢查 default_code 是否在 result 中
        if default_code in result:
            # 從 file_mapping 取得對應的完整檔案名稱
            combobox.set(file_mapping.get(default_code, "請選擇檔案"))
        else:
            combobox.set("請選擇檔案")
    else:
        combobox.set("請選擇檔案")
    combobox.pack(side="left")
    comboboxes[filename] = combobox

b1 = ttk.Button(frame2, text="確定", width=40, command=save_to_csv)
b1.pack(side="bottom")

root.mainloop()