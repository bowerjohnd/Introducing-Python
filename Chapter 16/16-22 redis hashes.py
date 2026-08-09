import redis
c = redis.Redis()


print("----")
print( c.hmset('song', {'do': 'a deer', 're': 'about a deer'}) )
# hmset works, but is deprecated. interpreter wants hset instead
#print( c.hset('song', {'do': 'a deer', 're': 'about a deer'}) )
# hset did not work with the dict, using deprecated hmset for this file
print("----")

print( c.hset('song', 'mi', 'a note to follow re') )
print( c.hget('song', 'mi') )
print( c.hmget('song', 're', 'do') )  
print( c.hkeys('song') )
print( c.hvals('song') )
print( c.hlen('song') )

print( c.hgetall('song') )

print( c.hsetnx('song', 'fa', 'a note that rhymes with ls') )