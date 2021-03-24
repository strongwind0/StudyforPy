import time

# time.gmtime() 返回的是英国格林威治时间及本初子午线所在的时间
# time。localtime() 返回的是本地时间

start = time.perf_counter()
print(time.time())
print(time.ctime())
t = time.gmtime()
print(t)
print(time.strftime('%Y-%m-%d %H:%M:%S', t))
t2 = '2021-3-15 23:09:01'
print(time.strptime(t2, "%Y-%m-%d %H:%M:%S"))
print(time.strptime('2021-3-25 23:09:01', "%Y-%m-%d %H:%M:%S"))
t3 = time.strptime(t2, "%Y-%m-%d %H:%M:%S")
print(t3)
print(time.strftime('%Y-%m-%d %H:%M:%S', t3))
end = time.perf_counter()
print(end - start)
