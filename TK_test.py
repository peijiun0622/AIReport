import os


import tkinter as tk
import tkinter.ttk as ttk
import pandas as pd

df=pd.read_excel("C:/Users/user/eclipse-workspace/AIReport/input_DATA/11403labor.xls")
filenames=df["繳款單檔名"].dropna().tolist()
#for filename in filenames:
    #print(filename)

root=tk.Tk()
root.title("測試")
frame1=ttk.Frame(root)
frame1.pack()
labels={}
Comboboxs={}
totalfile=os.listdir("C:/Users/user/eclipse-workspace/AIReport/input_DATA")
for filename in filenames:
    labels[filename]=ttk.Label(frame1,text=filename)
    
    labels[filename].pack(padx=10,pady=10)


    for files in totalfile:
    #Comboboxs[]=ttk.Combobox(frame1,values=files)
        combobox = ttk.Combobox(frame1, values=totalfile)
        combobox.pack(padx=10, pady=10)
        combobox.set("請選擇檔案") 
    
    
    #print(files)
root.mainloop()