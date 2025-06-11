
import re
import os
import chardet



folder_path = "C:/Users/user/eclipse-workspace/AIReport/input_DATA"
# 要寫入的檔案路徑
outputfile_path = "C:/Users/user/eclipse-workspace/AIReport/output_DATA/output.txt"


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
                    #print("總計裝封數:", pack_count)
                    #print("總計列印張數:", print_count)
                    
                    # 使用 'a' 模式附加寫入結果到檔案
                    with open(outputfile_path, 'a', encoding='utf-8') as file:
                        file.write(f"{files_and_dirs[i]},{pack_count},{print_count}\n")
                else:
                    print("未找到匹配的數字")