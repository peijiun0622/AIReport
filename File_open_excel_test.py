import pandas as pd

# 讀取 Excel 檔案
df = pd.read_excel("C:/Users/user/eclipse-workspace/AIReport/input_DATA/11403labor.xls")  # 改成你的 Excel 檔路徑

# 顯示所有欄位名稱
#print("欄位名稱：", df.columns.tolist())

# 讀取特定欄位，例如「繳款單檔名」
print("繳款單檔名")
print("===========")
filenames = df["繳款單檔名"].dropna().tolist()

# 印出結果
for name in filenames:
   print(name)
    #print(filenames[1])