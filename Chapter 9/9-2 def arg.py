def echo(anything) :
	return anything + ' ' + anything

print(echo('Rumplestiltskin'))

def commentary(color) :
	if color == 'red' :
		return "It's a tomato."
	elif color == "green" :
		return "It's a green pepper."
	elif color == 'bee purple' :
		return "I don't know what it is, but only bees can see it."
	else :
		return "I've never heard of the color " + color + "."

comment = commentary('blue')
print(comment)
print(commentary('red'))
print(commentary('green'))
print(commentary('bee purple'))

def do_nothing() :
	pass
print(do_nothing())

print("")

thing = None
if thing :
	print("It's some thing")
else :
	print("It's no thing")

if thing is None :
	print("It's nothing")
else :
	print("It's something")

print("")

def whatis(thing) :
	if thing is None :
		print(thing, "is None")
	elif thing :
		print(thing, "is True")
	else :
		print(thing, "is False")
whatis(None)
whatis(True)
whatis(False)

whatis(0)
whatis(0.0)
whatis('')
whatis("")
whatis('''''')
whatis(())
whatis([])
whatis({})
whatis(set())
whatis(0.00001)
whatis([0])
whatis([''])
whatis(' ')

print("")

def menu(wine, entree, dessert) :
	return {'wine': wine, 'entree': entree, 'dessert': dessert}

print( menu('chardonnay', 'chicken', 'cake') )
print( menu('beef', 'bagel', 'bordeaux') )
print( menu(entree='beef', dessert='bagel', wine='bordeaux') )
print( menu('frontenac', dessert='flan', entree='fish') )

print("")

def menu(wine, entree, dessert='pudding') :
	return {'wine': wine, 'entree': entree, 'dessert': dessert}

print( menu('chardonnay', 'chicken') )
print( menu('dunkelfelder', 'duck', 'doughnut') )

print("")

def buggy(arg, result=[]) :
	result.append(arg)
	print(result)

buggy('a')
buggy('b')	# expect ['b']

def works(arg) :
	result = []
	result.append(arg)
	return result

print(works('a'))
print(works('b'))

def nonbuggy(arg, result=None) :
	if result is None :
		result = []
	result.append(arg)
	print(result)

nonbuggy('a')
nonbuggy('b')