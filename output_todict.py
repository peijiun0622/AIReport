import chardet
import csv
import os
import re
import class_un_file

file_path = 'C:/Users/user/eclipse-workspace/AIReport/output_DATA/output.csv'

# 偵測編碼
with open(file_path, 'rb') as f:
    #從檔案 f 中讀取最多 10,000 個位元組（bytes）。
    #只要一小段文字就足以判斷檔案的編碼格式（例如 UTF-8、Big5、cp950）。
    #這行使用 chardet 套件來偵測文字編碼：

#它會分析 raw_data 的內容，回傳一個字典結果，例如：
#{'encoding': 'Big5', 'confidence': 0.99, 'language': 'Chinese'}
    encoding = chardet.detect(f.read(10000))['encoding']

# 讀取 CSV
data = []
with open(file_path, newline='', encoding=encoding) as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        row['總封數'] = int(row['總封數'])
        row['總張數'] = int(row['總張數'])
        #將這一筆轉換後的資料（row 字典）加入 data 這個列表中。
        data.append(row)

# 顯示結果
for item in data:
    print(item)