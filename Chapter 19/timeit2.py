# 19-23 using timeit to measure performance

from timeit import repeat
print(repeat('num = 5; num *= 2', number=1, repeat=5))