import os
from pathlib import Path

class FileManager:
    def __init__(self, base_path):
        self.base_path = Path(base_path)

    def create_folder(self, folder_name):
        """創建資料夾，如果不存在"""
        folder_path = self.base_path / folder_name
        if not folder_path.exists():
            os.makedirs(folder_path)
            print(f"已創建資料夾：{folder_path}")

    def remove_folder(self, folder_name):
        """移除資料夾及其內容"""
        folder_path = self.base_path / folder_name
        if folder_path.exists() and folder_path.is_dir():
            for item in folder_path.iterdir():
                if item.is_dir():
                    self.remove_folder(item)  # 遞迴移除子資料夾
                else:
                    item.unlink()  # 移除檔案
            folder_path.rmdir()
            print(f"已移除資料夾：{folder_path}")

    def create_file(self, file_name):
        """創建檔案，如果不存在"""
        file_path = self.base_path / file_name
        if not file_path.exists():
            file_path.touch()
            print(f"已創建檔案：{file_path}")

    def remove_file(self, file_name):
        """移除檔案"""
        file_path = self.base_path / file_name
        if file_path.exists() and file_path.is_file():
            file_path.unlink()
            print(f"已移除檔案：{file_path}")
    
class MyFile:
    def __init__(self, filepath, mode):
        self.filepath = filepath
        self.mode = mode
        self.file = None

    def __enter__(self):
        self.file = open(self.filepath, self.mode)
        return self.file  # 回傳給 with 語句中的 as 變數

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()