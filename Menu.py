from tkinter import Tk, Frame, Button, Label, Entry, Text, Scrollbar, VERTICAL, RIGHT, Y, Menu,END
from tkinter import filedialog
def open_file():

# 創建主視窗
    root = Tk()
    root.title('功能表')
    menubar=Menu(root)
    root.config(menubar)
    menu_file=Menu(menubar,tearoff=0)
    menubar.add_cascade(label='File',menu=menu_file)
    menu_file.add_command(label='作業量統計表',command=open_file)

    root.mainloop()