# 19-21 using time to measure performance

from time import time, sleep

t1 = time()
sleep(1.0)
print(time() - t1)