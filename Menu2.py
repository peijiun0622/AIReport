from tkinter import Tk, Menu
import subprocess

def run_report():
    # 使用 subprocess 執行 Report.py
    subprocess.run(['python', 'Report4.py'])

# 創建主視窗
root = Tk()
root.title('功能表')

# 創建功能表
menubar = Menu(root)
root.config(menu=menubar)
menu_file = Menu(menubar, tearoff=0)
menubar.add_cascade(label='功能表項目', menu=menu_file)
menu_file.add_command(label='作業量統計表', command=run_report)

# 開始主循環
root.mainloop()