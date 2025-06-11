'''
Created on 2025年4月18日

@author: user
'''
from tkinter import Tk, Frame, Button, Label, Entry
from tkinter import filedialog

def select_file():
    # 使用文件對話框選擇檔案
    file_path = filedialog.askopenfilename()
    # 將選擇的檔案路徑顯示在輸入框中
    file_path_entry.delete(0, 'end')  # 清空輸入框
    file_path_entry.insert(0, file_path)

# 創建主視窗
root = Tk()
root.title("REPORT")
root.geometry("500x300")

# 創建側邊欄框架
sidebar_frame = Frame(root, bg="lightgray", height=100)
sidebar_frame.pack(side="top", fill="x")

# 在側邊欄框架中添加標籤和按鈕
Label1 = Label(sidebar_frame, text="檔案路徑:")
Label1.pack(side="left", pady=5, padx=5)

# 創建一個輸入框來顯示選擇的檔案路徑
file_path_entry = Entry(sidebar_frame, width=40)
file_path_entry.pack(side="left", pady=5, padx=5)

# 創建一個按鈕來打開文件對話框
button1 = Button(sidebar_frame, text="選擇檔案", command=select_file)
button1.pack(side="left", pady=5, padx=5)

# 創建主內容框架
main_frame = Frame(root, bg="white")
main_frame.pack(side='bottom', fill="both", expand=True)

# 啟動主迴圈
root.mainloop()