import time

c = 0
try:
    print("Script started.")  # 添加 flush=True

    while True:
        c += 1
        print(c)  # 输出当前计数，立即刷新
        time.sleep(1)
except Exception as e:
    print(f"Error occurred: {e}")
