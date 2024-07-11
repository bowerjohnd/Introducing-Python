import time

now = time.time()
print(now)
print(time.ctime(now))

print("")

print(time.localtime(now))
print(time.gmtime(now))

print("")

now = time.localtime()
print(now)

print(now[0])
print(list( now[x] for x in range(9) ))


#tm = time.localtime(now)
print(time.mktime(now))

