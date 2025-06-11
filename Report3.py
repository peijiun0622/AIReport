import os
import shutil
import re
import chardet
from tkinter import Tk, Frame, Button, Label, Entry, Text, Scrollbar, VERTICAL, RIGHT, Y, END, messagebox
from tkinter import filedialog

import class_un_file

def select_directory():
    # 使用文件對話框選擇資料夾
    directory_path = filedialog.askdirectory()
    if directory_path:
        # 將選擇的資料夾路徑顯示在輸入框中
        dir_path_entry.delete(0, 'end')
        dir_path_entry.insert(0, directory_path)

        # 清空文本框
        file_list_text.delete(1.0, END)

        # 列出資料夾中的所有檔案
        try:
            files = os.listdir(directory_path)
            total = 0  # 初始化計數器
            for file in files:
                total += 1  # 累加計數器
                file_list_text.insert(END, file + '\n')

            # 顯示檔案總數並詢問是否執行 out.py
            result = messagebox.askyesno("檔案總數", f"共 {total} 個檔案。是否正確？")
            if result:
                # 執行 input_write()
                input_write(directory_path)
            else:
                # 顯示再檢查檔案
                messagebox.showinfo("提示", "再檢查檔案")

        except Exception as e:
            file_list_text.insert(END, f"Error: {e}")

def input_write(folder_path):
    # 獲取父目錄
    outputparent_directory = os.path.dirname(folder_path)

    # 使用 os.path.join 來組合路徑
    output_folder_path = os.path.join(outputparent_directory, 'output_DATA')
    outputfile_path = os.path.join(output_folder_path, 'output.txt')

    # 確保資料夾存在
    if not os.path.exists(output_folder_path):
        os.makedirs(output_folder_path)

    # 使用 FileManager 類別來創建文件
        output_parent = class_un_file.FileManager(output_folder_path)
        output_parent.create_file('output.txt')

          # 輸出完整的路徑
    
    else:
        output_parent.remove_file(outputfile_path, 'output.txt')
        print(outputfile_path)
        
    pattern = r"總計裝封數\s+(\d+).*?總計列印張數\s+(\d+)"

    files_and_dirs = os.listdir(folder_path)

    for i in range(len(files_and_dirs)):
        print("Files in folder:", files_and_dirs[i])

        file_path = os.path.join(folder_path, files_and_dirs[i])

        if os.path.isfile(file_path):
            # 讀取前幾個位元組來檢測編碼
            with open(file_path, 'rb') as f:
                raw_data = f.read(100)
                result = chardet.detect(raw_data)
                encoding = result['encoding']
                print(f"檢測到的編碼：{encoding}")

            # 使用檢測到的編碼讀取檔案
            with open(file_path, 'r', encoding=encoding) as f:
                for line in f:
                    match = re.search(pattern, line)
                    if match:
                        pack_count = match.group(1)
                        print_count = match.group(2)

                        # 使用 'a' 模式附加寫入結果到檔案
                        with open(outputfile_path, 'a', encoding='utf-8') as file:
                            file.write(f"{files_and_dirs[i]},{pack_count},{print_count}\n")
                    else:
                        print("未找到匹配的數字")

            # 移動檔案到 move_DATA 資料夾
            move_folder_path = os.path.join(outputparent_directory, 'move_DATA')
            if not os.path.exists(move_folder_path):
                os.makedirs(move_folder_path)

            # 使用 shutil.move 來移動檔案
            destination_path = os.path.join(move_folder_path, files_and_dirs[i])
            shutil.move(file_path, destination_path)
            print(f"{files_and_dirs[i]} 已移動到 {move_folder_path}")

# 創建主視窗
root = Tk()
root.title("REPORT")
root.geometry("500x400")

# 創建側邊欄框架
sidebar_frame = Frame(root, bg="lightgray", height=100)
sidebar_frame.pack(side="top", fill="x")

# 在側邊欄框架中添加標籤和按鈕
Label1 = Label(sidebar_frame, text="資料夾路徑:")
Label1.pack(side="left", pady=5, padx=5)

# 創建一個輸入框來顯示選擇的資料夾路徑
dir_path_entry = Entry(sidebar_frame, width=40)
dir_path_entry.pack(side="left", pady=5, padx=5)

# 創建一個按鈕來打開資料夾選擇對話框
button1 = Button(sidebar_frame, text="選擇資料夾", command=select_directory)
button1.pack(side="left", pady=5, padx=5)

# 創建主內容框架
main_frame = Frame(root, bg="white")
main_frame.pack(side='bottom', fill="both", expand=True)

# 創建一個文本框來顯示資料夾中的檔案
file_list_text = Text(main_frame, wrap='none')
file_list_text.pack(side='left', fill='both', expand=True)

# 創建一個滾動條
scrollbar = Scrollbar(main_frame, orient=VERTICAL, command=file_list_text.yview)
scrollbar.pack(side=RIGHT, fill=Y)

# 將文本框與滾動條關聯
file_list_text.config(yscrollcommand=scrollbar.set)

# 啟動主迴圈
root.mainloop()