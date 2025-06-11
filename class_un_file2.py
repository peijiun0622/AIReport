import os
from pathlib import Path
import csv
import chardet
import pandas as pd

class FileManager:
    def __init__(self, base_path):
        self.base_path = Path(base_path)

    def create_folder(self, folder_name):
        folder_path = self.base_path / folder_name
        if not folder_path.exists():
            os.makedirs(folder_path)
            print(f"已創建資料夾：{folder_path}")

    def remove_folder(self, folder_name):
        folder_path = self.base_path / folder_name
        if folder_path.exists() and folder_path.is_dir():
            for item in folder_path.iterdir():
                if item.is_dir():
                    self._remove_path(item)
                else:
                    item.unlink()
            folder_path.rmdir()
            print(f"已移除資料夾：{folder_path}")

    def _remove_path(self, path):
        """遞迴移除資料夾或檔案"""
        if path.is_dir():
            for item in path.iterdir():
                self._remove_path(item)
            path.rmdir()
        else:
            path.unlink()

    def create_file(self, file_name):
        file_path = self.base_path / file_name
        if not file_path.exists():
            file_path.touch()
            print(f"已創建檔案：{file_path}")

    def remove_file(self, file_name):
        file_path = self.base_path / file_name
        if file_path.exists() and file_path.is_file():
            file_path.unlink()
            print(f"已移除檔案：{file_path}")

# ⬇️ 獨立 class：MyFile context manager
class MyFile:
    def __init__(self, filepath, mode='r'):
        self.filepath = Path(filepath)
        self.mode = mode
        self.file = None
        self.encoding = 'utf-8'  # 預設編碼

    def _is_binary_file(self):
        """根據副檔名判斷是否為二進位檔案"""
        return self.filepath.suffix.lower() in [
            '.jpg', '.png', '.gif', '.pdf', '.zip', '.exe', '.mp3', '.mp4'
        ]

    def _is_csv_file(self):
        return self.filepath.suffix.lower() == '.csv'

    def _is_excel_file(self):
        return self.filepath.suffix.lower() in ['.xlsx', '.xls']

    def _is_txt_file(self):
        return self.filepath.suffix.lower() == '.txt'

    def detect_encoding(self):
        """偵測文字檔案的編碼"""
        try:
            with open(self.filepath, 'rb') as f:
                raw_data = f.read(2048)
                result = chardet.detect(raw_data)
                return result['encoding'] or 'utf-8'
        except Exception:
            return 'utf-8'

    def __enter__(self):
        # 決定是否需要自動偵測文字編碼
        if 'r' in self.mode and not self._is_binary_file():
            self.encoding = self.detect_encoding()

        # Excel 檔案使用 pandas 開啟
        if self._is_excel_file():
            if 'r' in self.mode:
                return pd.read_excel(self.filepath)
            elif 'w' in self.mode:
                self.file = pd.ExcelWriter(self.filepath, engine='openpyxl')
                return self.file

        # CSV 檔案使用 csv 模組開啟
        elif self._is_csv_file():
            self.file = open(self.filepath, self.mode, newline='', encoding=self.encoding)
            if 'r' in self.mode:
                self.reader = csv.reader(self.file)
                return self.reader
            elif 'w' in self.mode:
                self.writer = csv.writer(self.file)
                return self.writer

        # 其他文字 / 二進位檔案
        else:
            open_kwargs = {'mode': self.mode}
            if not self._is_binary_file():
                open_kwargs['encoding'] = self.encoding
            self.file = open(self.filepath, **open_kwargs)
            return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            if isinstance(self.file, pd.ExcelWriter):
                self.file.close()
            else:
                self.file.close()