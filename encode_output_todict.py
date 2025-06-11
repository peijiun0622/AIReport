import csv
import chardet
# 讀取原始資料
input_path = 'C:/Users/user/eclipse-workspace/AIReport/output_DATA/output.csv'

def read_csv_as_dict(filepath, convert_numeric=True, sample_size=10000):
    """自動偵測編碼並讀取 CSV 成為字典列表"""
    with open(filepath, 'rb') as f:
        raw = f.read(sample_size)
        encoding = chardet.detect(raw)['encoding']
    
    data = []
    with open(filepath, newline='', encoding=encoding) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if convert_numeric:
                for key in row:
                    value = row[key].strip()
                    if value.isdigit():
                        row[key] = int(value)
                    else:
                        try:
                            row[key] = float(value)
                        except ValueError:
                            row[key] = value
            data.append(row)
    return data

def write_dict_to_csv(filepath, data, encoding='utf-8-sig'):
    """將字典列表寫入 CSV 檔案"""
    if not data:
        raise ValueError("資料為空，無法寫入 CSV。")

    fieldnames = data[0].keys()

    with open(filepath, mode='w', newline='', encoding=encoding) as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)
data = read_csv_as_dict(input_path)
# 做一點修改（例如：加總張數欄位 +100）
for row in data:
    if isinstance(row['總張數'], int):
        row['總張數'] += 100

# 寫回新的檔案
output_path = 'C:/Users/user/eclipse-workspace/AIReport/output_DATA/output_modified.csv'
write_dict_to_csv(output_path, data)

print("CSV 檔已成功寫入！")
