def dive() :
	return dive()

# dive()

def flatten(lol) :
	for item in lol :
		if isinstance(item, list) :
			for subitem in flatten(item) :
				yield subitem
		else :
			yield item
lol = [1, 2, [3,4,5], [6,[7,8,9], []]]
print(flatten(lol))
print( list(flatten(lol)) )

print("")

def flatten(lol) :
	for item in lol :
		if isinstance(item, list) :
			yield from flatten(item)
		else :
			yield item
print( list(flatten(lol)) )