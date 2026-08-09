import time
now = time.time()  # epoch time
print(now)

import redis
c = redis.Redis()


#print( c.zadd('logins', 'smeagol', now) )
# google says zadd requires dict now:

print( c.zadd( 'logins', {'smeagol': now} ) )
print( c.zadd( 'logins', {'sauron': now+(5*60)} ) )         # 5 minutes
print( c.zadd( 'logins', {'bilbo': now+(2*60*60)} ) )       # 2 hours
print( c.zadd( 'logins', {'treebeard': now+(24*60*60)} ) )  # 24 hours

print( c.zrank('logins', 'bilbo') )
print( c.zscore('logins', 'bilbo') )

print("")

print( c.zrange('logins', 0, -1) )

print("")

print( c.zrange('logins', 0, -1, withscores=True) )