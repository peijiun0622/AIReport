class Room:
    def __enter__(self):
        print("💡 開燈（__enter__）")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print("💡 關燈（__exit__）")
        if exc_type:
            print(f"⚠️ 發生錯誤：{exc_type.__name__} - {exc_value}")
            return True  # 表示錯誤已處理，不拋出
        
with Room() as room:
    print("在房間裡活動")
    raise ValueError("不小心踢到桌角！")