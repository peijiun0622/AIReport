class SimpleContext:
    def __init__(self):
        print("🔧 初始化：__init__() 被呼叫了")

    def __enter__(self):
        print(f"🚪 進入：__enter__(), self 是 {self}")
        return self

    def __exit__(self, exc_type, exc_val, tb):
        print(f"🚪 離開：__exit__(), self 是 {self}")

with SimpleContext() as ctx:
    print("🧱 在 with 區塊中")