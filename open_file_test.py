class MyFile:
    def __init__(self, filename):
        self.filename = filename
        self.opened = False

    def open(self):
        print(f"{self.filename} 已開啟")
        self.opened = True

    def close(self):
        if self.opened:
            print(f"{self.filename} 已關閉")
            self.opened = False

    def __enter__(self):
        self.open()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print("離開區塊")
        if exc_type:
            print(f"有錯誤發生：{exc_value}")
        self.close()  # ✅ 這裡是關鍵！
        return False  # 不吃掉錯誤

# 使用方式
with MyFile("demo.txt") as f:
    print("執行中")
    # raise ValueError("測試錯誤")