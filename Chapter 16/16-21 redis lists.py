import redis
c = redis.Redis()


print( c.lpush('zoo', 'bear') )
print( c.lpush('zoo', 'alligator', 'duck') )

print( c.linsert('zoo', 'before', 'bear', 'beaver') )
print( c.linsert('zoo', 'after', 'bear', 'cassowary') )

print( c.lset('zoo', 2, 'marmoset') )

print( c.rpush('zoo', 'yak') )

print( c.lindex('zoo', 3) )

print( c.lrange('zoo', 0, 2) )

print( c.ltrim('zoo', 1, 4) )

print( c.lrange('zoo', 0, -1) )