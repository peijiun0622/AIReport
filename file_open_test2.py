class MyContext:
    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type:
            print(f"錯誤：{exc_type.__name__}: {exc_value}")
        return False  # 或寫 None，錯誤會繼續拋出

with MyContext():
    raise ValueError("Oops!")  # 模擬錯誤