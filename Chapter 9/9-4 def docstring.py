def echo(anything) :
	'echo returns its input argument'
	return anything

def print_if_true(thing, check) :
	'''
	Prints the first argument if a second is true.
	The operation is:
		1. Check whether the *second* argument is true.
		2. If it is, print the *first* argument.
	'''
	if check :
		print(thing)
help(echo)
print(echo.__doc__)

print("----------------------")

help(print_if_true)
print("----------------------")
print(print_if_true.__doc__)

