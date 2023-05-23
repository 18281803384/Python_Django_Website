# 作者: ZengCheng
# 时间: 2023/5/23
import time


# ------- 获取当前时间函数 ------- #
def format_time():
    times = time.time()
    local_time = time.localtime(times)
    correct_time = time.strftime("%Y-%m-%d %H:%M:%S", local_time)
    return correct_time
