import pandas as pd

# 定義兩個 CSV 檔案的資料（模擬您的輸入）
selected_output_data = {
    '繳款單檔名': [
        'amf0340_1_hinet.rar', 'amf0340_2_hinet.rar', 'amf0340_3c_hinet.rar',
        'amf0340_3d_hinet.rar', 'amf0340_3e_hinet.rar', 'amf0340_5_1_hinet.rar',
        'amf0340_5_2_hinet.rar', 'amf0340_6_hinet.rar'
    ],
    '選擇的檔案': [
        '0613CKSP-1.txt', '0613CKNP.txt', '0613CKNL-3c.txt', '0613CKNL-3d.txt',
        '0613CKNL-3e.txt', '0613CKSP-51.txt', '0613CKSP-52.txt', '0613CKSP-6.txt'
    ]
}

output_data = {
    '檔名': [
        '0613CKNL-3c.txt', '0613CKNL-3d.txt', '0613CKNL-3e.txt', '0613CKNP.txt',
        '0613CKSP-1.txt', '0613CKSP-2.txt', '0613CKSP-3.txt', '0613CKSP-51.txt',
        '0613CKSP-52.txt', '0613CKSP-6.txt'
    ],
    '總封數': [1, 1, 1, 1640, 200000, 200000, 84179, 1, 1, 26],
    '總張數': [96, 306, 129, 2999, 359853, 359353, 146996, 1, 1, 26]
}

# 轉為 DataFrame
df_selected = pd.DataFrame(selected_output_data)
df_output = pd.DataFrame(output_data)

# 比對檔名
selected_files = set(df_selected['選擇的檔案'])
output_files = set(df_output['檔名'])

# 找出交集、僅 selected_output、僅 output 的檔名
common_files = selected_files & output_files
only_selected = selected_files - output_files
only_output = output_files - selected_files

# 建立結果 DataFrame
result = []

# 處理交集檔案（兩者皆有）
for file in common_files:
    row_output = df_output[df_output['檔名'] == file].iloc[0]
    row_selected = df_selected[df_selected['選擇的檔案'] == file].iloc[0]
    result.append({
        '檔名': file,
        '繳款單檔名': row_selected['繳款單檔名'],
        '總封數': row_output['總封數'],
        '總張數': row_output['總張數'],
        '來源': '兩者皆有'
    })

# 處理僅 selected_output 的檔案
for file in only_selected:
    row_selected = df_selected[df_selected['選擇的檔案'] == file].iloc[0]
    result.append({
        '檔名': file,
        '繳款單檔名': row_selected['繳款單檔名'],
        '總封數': None,
        '總張數': None,
        '來源': '僅 selected_output'
    })

# 處理僅 output 的檔案
for file in only_output:
    row_output = df_output[df_output['檔名'] == file].iloc[0]
    result.append({
        '檔名': file,
        '繳款單檔名': None,
        '總封數': row_output['總封數'],
        '總張數': row_output['總張數'],
        '來源': '僅 output'
    })

# 轉為 DataFrame
result_df = pd.DataFrame(result)

# 排序（可選，按檔名排序）
result_df = result_df.sort_values(by='檔名')

# 寫入 Excel
result_df.to_excel('filename_comparison.xlsx', index=False, engine='openpyxl')

print("比對完成，結果已寫入 'filename_comparison.xlsx'。")