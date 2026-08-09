# Introducing Python, 2nd Edition, often uses the interpreter
#	excessive print() are for running it as a script
#	as the interpreter usually echoes results of each line
#



import memcache

db = memcache.Client(['localhost:11211'])

print( db.set('marco', 'polo') )
print( db.get('marco') )

print( db.set('ducks', 0) )
print( db.get('ducks') )

print( db.incr('ducks', 2) )
print( db.get('ducks') )


