import tkinter as tk
from tkinter import filedialog

class FileOpener(tk.Toplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.title("Open File")
        self.geometry("400x300")
        self.file_list_text = tk.Text(self)
        self.file_list_text.pack(expand=True, fill='both')
        self.scrollbar = tk.Scrollbar(self, orient=tk.VERTICAL, command=self.file_list_text.yview)
        self.scrollbar.pack(side='right', fill='y')
        self.file_list_text.config(yscrollcommand=self.scrollbar.set)
        self.open_file_button = tk.Button(self, text="Open File", command=self.open_file)
        self.open_file_button.pack()

    def open_file(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            with open(file_path, 'r') as file:
                content = file.read()
                self.file_list_text.delete(1.0, tk.END)
                self.file_list_text.insert(tk.END, content)

# 使用 FileOpener 類別
root = tk.Tk()
file_opener = FileOpener(root)
root.mainloop()