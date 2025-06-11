class MyContext:
    def __enter__(self):
        print(">>> 進入 __enter__()")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print(">>> 離開 __exit__()")
        if exc_type:
            print(f"!!! 捕捉到錯誤: {exc_type.__name__}, {exc_value}")
        return False  # 若傳回 True，錯誤會被吞掉，不會往外拋

with MyContext() as ctx:
    print(">>> with 區塊中")
    raise ValueError("這是一個測試錯誤")