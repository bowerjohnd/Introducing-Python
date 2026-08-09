import redis
c = redis.Redis()

# clear existing keys to ensure a clean run 
# google reponse to failed to run
#       previous examples use / mixed data sounds logical, maybe?
c.delete('zoo', 'better_zoo', 'fowl_zoo', 'fabulous_zoo', 'zoo_sale')

print( c.sadd('zoo', 'duck', 'goat', 'turkey') )
print( c.scard('zoo') )
print( c.smembers('zoo') )

print( c.srem('zoo', 'turkey') )

print( c.sadd('better_zoo', 'tiger', 'wolf', 'duck') )

print( c.sinter('zoo', 'better_zoo') )
print( c.sinterstore('fowl_zoo', 'zoo', 'better_zoo') )

print( c.smembers('fowl_zoo') )

print( c.sunion('zoo', 'better_zoo') )
print( c.sunionstore('fabulous_zoo', 'zoo', 'better_zoo') )

print( c.smembers('fabulous_zoo') )

print( c.sdiff('zoo', 'better_zoo') )
print( c.sdiffstore('zoo_sale', 'zoo', 'better_zoo') )

print( c.smembers('zoo_sale') )th ls') )