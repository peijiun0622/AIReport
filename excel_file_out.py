import tkinter as tk
import tkinter.ttk as ttk
import pandas as pd
from tkinter import messagebox
import os
import csv
from datetime import datetime

# 取得當前西元年份
gregorian_year = datetime.now().year  # 例如 2025

# 轉換為民國年份
roc_year = gregorian_year - 1911  # 2025 - 1911 = 114

# 輸出結果
print(f"民國 {roc_year} 年")  # 輸出：民國 114 年

# 讀取 Excel
df = pd.read_excel("C:/Users/user/eclipse-workspace/AIReport/input_DATA/11403labor.xls")
filenames = df["繳款單檔名"].dropna().tolist()

# 取得資料夾中的所有檔案名稱
totalfile = os.listdir("C:/Users/user/eclipse-workspace/AIReport/input_DATA")

#這行是以讀取模式（mode='r'）和 UTF-8 編碼打開名為 'labor_CODE.csv' 的檔案，並將檔案對象命名為 file
with open('labor_CODE.csv', mode='r', encoding='utf-8') as file:
    #使用 csv.DictReader 來讀取這個 CSV 檔案，這個方法會自動把每一行轉成一個字典（key 為欄位名稱，value 為該行對應欄位的值）
    reader = csv.DictReader(file)
    #print(type(reader))
   #這是一個字典生成式，會遍歷每一行 row，然後用 row['Filename'] 當作 key，row['Code'] 當作 value，組成一個新的字典 data_dict
    #是的，data_dict = {row['Filename']: row['Code'] for row in reader} 這裡的 'Filename' 和 'Code' 是指 labor_CODE.csv 檔案中 CSV 標題列（header）裡的欄位名稱。

#csv.DictReader 會自動把第一列當作欄位名稱，然後每一行資料會以欄位名稱作為 key，對應欄位的資料作為 value，形成一個字典。因此這兩個字串必須和 CSV 檔案的標題完全一致，才能正確取得對應欄位的資料。

    data_dict = {row['Filename']: row['Code'] for row in reader}

print(f"data_dict={data_dict}")

def save_to_csv():
    output_path = os.path.abspath("output_DATA/selected_output.csv")  # 絕對路徑
    with open(output_path, mode="w", encoding="utf-8-sig", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["繳款單檔名", "選擇的檔案"])  # 標題列

#這行代表：遍歷 comboboxes 這個字典（dict），其中 key 是 filename（檔案名稱），value 是 combobox（下拉選單元件）
#這些名稱說明你正在 comboboxes 字典中儲存一組對應關係：

#filename（鍵）：應該是每個檔案的名稱。

#combobox（值）：是那個對應檔案的 Combobox 控制元件。
        for filename, combobox in comboboxes.items():
           # 這行取得目前 combobox（下拉選單）被選中的值，存到 selected_file 變數裡。
            selected_file = combobox.get()
            #這行將 filename 和 selected_file 這兩個值，組成一個列表（list），然後寫入 CSV 檔案的一行
            writer.writerow([filename, selected_file])

    print(f"已將選擇結果寫入 {output_path}")
    messagebox.showinfo("完成", f"已儲存：\n{output_path}")


# 建立主視窗
root = tk.Tk()
root.title("測試")

# 建立框架
frame1 = ttk.Frame(root)
frame1.pack(padx=10, pady=10)
frame2= ttk.Frame(root)
frame2.pack(padx=10, pady=10)
# 建立 Label 與 Combobox 的配對
labels = {}
comboboxes = {}

for filename in filenames:
    row_frame = ttk.Frame(frame1)  # 建一個水平列容器
    row_frame.pack(fill="x", pady=5)

    # Label 顯示繳款單檔名
    labels[filename] = ttk.Label(row_frame, text=filename, width=40)
    labels[filename].pack(side="left")

    # Combobox 顯示所有檔案供選擇

    #combobox = ttk.Combobox(row_frame, values=totalfile, width=40, command=save_to_csv)
    #這行是建立一個下拉式選單 (Combobox)：

#ttk.Combobox: 是 tkinter.ttk 模組提供的下拉選單元件。

#row_frame: 是這個下拉選單所屬的父容器（可能是某個 Frame）。

#values=totalfile: 設定下拉選單的選項內容，totalfile 應該是一個列表（如：["file1.csv", "file2.csv", "file3.csv"]）。

#width=40: 設定下拉選單的寬度（以字元為單位）。

#state="readonly": 表示只能選擇選單中的項目，不能手動輸入。
    combobox = ttk.Combobox(row_frame, values=totalfile, width=40, state="readonly")

#是設定事件綁定，意思是：

#bind("<<ComboboxSelected>>", ...): 當使用者從下拉選單中選擇了一個項目時，會觸發 <<ComboboxSelected>> 事件。

#lambda e: save_to_csv(): 當事件發生時（使用者選擇了一個選項），會呼叫 save_to_csv() 函式。lambda e: 是匿名函式，用來接收事件對象 e（雖然這裡沒用到）。

    combobox.bind("<<ComboboxSelected>>", lambda e: save_to_csv())
    
    # 預設值設定：如果 filename 存在於 data_dict，則取對應的 Code
    #判斷變數 filename（通常是一個檔名字串）是否存在於之前建立的字典 data_dict 的鍵（key）中。
    if filename in data_dict:
        #如果存在，就從 data_dict 裡取出對應 filename 的值（即該檔案對應的 code），並存到變數 default_code。
        default_code = data_dict[filename]
        #將 combobox（下拉選單）設定為 default_code，讓下拉選單顯示對應的預設值。
        #combobox.set(f"{roc_year}{default_code}.txt")
        combobox.set(default_code)
    else:
        combobox.set("請選擇檔案")  # 其他檔案的預設值
    
    combobox.pack(side="left")
    #把這個 combobox 物件以 filename 當作鍵，存入 comboboxes 這個字典中，方便後續根據檔名找到對應的下拉選單元件。

    #總結：這段程式碼是將每個檔名對應的下拉選單元件配置到視窗中，並且用字典 comboboxes 管理這些元件，方便後續操作和讀取使用者選擇
    #將這個 combobox（下拉選單元件）物件，以 filename 當作鍵，存入 comboboxes 這個字典中。

#這裡的 combobox 不是存 filename 對應的 Code 值，而是 tkinter 的 Combobox 元件本身。這樣做的目的是方便後續程式能夠根據 filename 快速找到對應的 Combobox 元件，進而讀取或設定該元件的選項值。
  #換句話說：

#data_dict 是儲存 filename 對應的 Code（資料內容）的字典。

#comboboxes 是儲存 filename 對應的 Combobox 元件（GUI 控件）的字典。

#這兩者分別管理資料和介面元件，方便程式在不同階段操作：

#讀取資料時用 data_dict[filename] 取得對應的 Code。

#操作介面時用 comboboxes[filename] 取得對應的 Combobox 元件，像是設定預設選項或取得使用者選擇的值。

#因此，comboboxes[filename] = combobox 是將 GUI 元件與檔名做綁定管理，而不是存資料值  

  #comboboxes["檔案1.txt"] = combobox  # 將 "檔案1.txt" 對應的 Combobox 物件存入字典
#後續你可以透過 comboboxes["檔案1.txt"].get() 獲取該下拉選單的當前選擇值。

  
    comboboxes[filename] = combobox
    #print(comboboxes[filename])
    #你印出 comboboxes[filename] 後看到的結果像是：
    #!frame.!frame.!combobox
#!frame.!frame2.!combobox
#!frame.!frame3.!combobox
#print(type(comboboxes[filename]))
#print(comboboxes[filename].get())

#for filename in comboboxes:
   # print(f"{filename}: {comboboxes[filename].get()}")  # 使用 .get() 獲取選擇值
#這是 tkinter GUI 元件（widget）的內部路徑名稱（widget path name），代表每個 combobox 元件在 GUI 視窗中的層級結構位置。

#具體來說：

#!frame 表示最外層的 Frame 容器元件。

#!frame2、.!frame3 等是這個 Frame 底下不同的子 Frame。

#!combobox 是在該 Frame 裡的 Combobox 元件。

#這個字串是 tkinter 自動分配給每個元件的識別名稱，用來區分不同的 GUI 元件。印出來看到這樣的結果，表示你成功取得了對應的 Combobox 元件物件，而不是單純的字串或其他資料。

#你可以利用這個 Combobox 物件呼叫它的方法，例如 .get()、.set() 來讀取或設定選項值，而不需要理會它的內部路徑名稱。

#總結：這些印出來的字串是 tkinter Combobox 元件的識別路徑，代表你確實存取到了 GUI 控件物件。




b1=ttk.Button(frame2,text="確定", width=40, command=save_to_csv)
b1.pack(side="bottom")
    

root.mainloop()