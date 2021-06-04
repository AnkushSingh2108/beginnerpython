import datetime
d = datetime.datetime(2017,4,7)
print("0->>",d)
import time
t = time.time()
print(t)
print("1->>",time.localtime(t))
print("2->>",time.asctime())
print("3->>",datetime.datetime.now)
# y = datetime.datetime.now
# z = y.year()
# print("4->>", z)
