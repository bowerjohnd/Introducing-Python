import redis

# Default redis.Redis() is the same as below
conn = redis.Redis('localhost', 6379)

print( conn.keys('*') )

print( conn.set('secret', 'ni!') )
print( conn.set('carats', 24) )
print( conn.set('fever', '101.5') )

print( conn.get('secret') )
print( conn.get('carats') )
print( conn.get('fever') )

# set if not exist
print( conn.setnx('secret', 'icky-icky-icky-ptang-zoop-boing!') ) # where's that from???
print( conn.get('secret') )

# get value, then change value
print( conn.getset('secret', 'icky-icky-icky-ptang-zoop-boing!') )
print( conn.get('secret') ) 

print( conn.getrange('secret', -6, -1) )
print( conn.setrange('secret', 0, 'ICKY') )
print( conn.get('secret') )

print( conn.mset( {'pie': 'cherr', 'cordial': 'sherry'}) )

print( conn.mget(['fever', 'carats']) )
print( conn.delete('fever') )

print("")

print( conn.incr('carats') )
print( conn.incr('carats', 10) )

print( conn.decr('carats') )
print( conn.decr('carats', 15) )

print( conn.set('fever', '101.5') )

print( conn.incrbyfloat('fever') )
print( conn.incrbyfloat('fever', 0.5) )

print( conn.incrbyfloat('fever', -2.0) ) # no decr, use negative to decrease