import os
from pathlib import Path

def create_folder(path):
    """創建資料夾，如果不存在"""
    folder_path = Path(path)
    if not folder_path.exists():
        os.makedirs(folder_path)
        print(f"已創建資料夾：{folder_path}")

def remove_folder(path):
    """移除資料夾及其內容"""
    folder_path = Path(path)
    if folder_path.exists() and folder_path.is_dir():
        for item in folder_path.iterdir():
            if item.is_dir():
                remove_folder(item)  # 遞迴移除子資料夾
            else:
                item.unlink()  # 移除檔案
        folder_path.rmdir()
        print(f"已移除資料夾：{folder_path}")

def create_file(path):
    """創建檔案，如果不存在"""
    file_path = Path(path)
    if not file_path.exists():
        file_path.touch()
        print(f"已創建檔案：{file_path}")

def remove_file(path):
    """移除檔案"""
    file_path = Path(path)
    if file_path.exists() and file_path.is_file():
        file_path.unlink()
        print(f"已移除檔案：{file_path}")