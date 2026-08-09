import redis
c = redis.Redis()

import time

key = 'now you see it'

print( c.set(key, 'but not for long') )
print( c.expire(key, 5) ) # seconds

print( c.ttl(key) )

print( c.get(key) )

time.sleep(6)

print( c.get(key) )