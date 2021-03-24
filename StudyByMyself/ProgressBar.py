import time

# for i in range(101):
#     print("\r{:>3}%".format(i), end="")
#     time.sleep(3/(101-i))

scale = 50
print("开始".center(scale//2, '-'))
start = time.perf_counter()
for i in range(scale+1):
    a = '*'*i
    b = '.'*(scale-i)
    c = (i/scale)*100
    dur = time.perf_counter() - start
    print("\r{:>3.0f}% [{}->{}] 已用时间:{:.3f}s".format(c, a, b, dur), end="")
    time.sleep(25/(101-i))
print("\n", "完成".center(scale//2, '-'))
