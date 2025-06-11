import pandas as pd

main_data = {
    '繳款單檔名': [
        'amf0340_1_hinet.rar',
        'amf0340_2_hinet.rar',
        'amf0340_3a_hinet.rar',
        'amf0340_3c_hinet.rar',
        'amf0340_3d_hinet.rar',
        'amf0340_3e_hinet.rar',
        'amf0340_5_2_hinet.rar',
        'amf0340_6_hinet.rar'
    ],
    '件數': [None] * 8,
    '繳款單及清單總張數': [None] * 8
}
short_name_map = {
    'CKSP-1': 'amf0340_1_hinet.rar',
    'CKNP': 'amf0340_2_hinet.rar',
    'CKNL-3a': 'amf0340_3a_hinet.rar',
    'CKNL-3c': 'amf0340_3c_hinet.rar',
    'CKNL-3d': 'amf0340_3d_hinet.rar',
    'CKNL-3e': 'amf0340_3e_hinet.rar',
    'CKNP-52': 'amf0340_5_2_hinet.rar',
    'CKSP-6': 'amf0340_6_hinet.rar'
}
count_data = {
    'CKSP-1': (200000, 361659),
    'CKNP': (1655, 3041),
    'CKNL-3a': (2, 4),
    'CKNL-3c': (1, 94),
    'CKNL-3d': (1, 306),
    'CKNL-3e': (1, 130),
    'CKNP-52': (2173, 2173),
    'CKSP-6': (61185, 61320)
}
main_df = pd.DataFrame(main_data)
print(main_df)

for code, (count, total_pages) in count_data.items():
    filename = short_name_map[code]  # 用代碼找到檔名
    # 找出主表中對應檔案那一列，填入件數和總張數
    main_df.loc[main_df['繳款單檔名'] == filename, '件數'] = count
    main_df.loc[main_df['繳款單檔名'] == filename, '繳款單及清單總張數'] = total_pages

print(main_df)