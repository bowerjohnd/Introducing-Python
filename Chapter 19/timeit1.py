# 19-22 using timeit to measure performance

from timeit import timeit
print(timeit('num = 5; num *= 2', number=1))