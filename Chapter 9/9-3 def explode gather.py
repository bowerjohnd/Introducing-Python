def print_args(*args) :
	print('Positional tuple:', args)

print_args()

print_args(3,2,1, 'wait!', 'uh...')

print("")

def print_more(required1, required2, *args) :
	print('Need this one:', required1)
	print('Need this one too:', required2)
	print('All the rest:', args)

print_more('cap', 'gloves', 'scarf', 'monocle', 'mustache wax')

print("")

print_args(2,5,7,'x')
args = (2,5,7,'x')
print_args(args)
print_args(*args)

# *args

print("")

def print_kwargs(**kwargs) :
	print('Keyword arguments:', kwargs)

print_kwargs()
print_kwargs(wine='merlot', entree='mutton', dessert='macaroon')

# **kwparams

print("")

def print_data(data, *, start=0, end=100) :
	for value in (data[start:end]) :
		print(value)
data = ['a', 'b', 'c', 'd', 'e', 'f']
print_data(data)
print("")
print_data(data, start=4)
print("")
print_data(data, end=2)

print("")

outside = ['one', 'fine', 'day']
def mangle(arg) :
	arg[1] = 'terrible!'

print(outside)
mangle(outside)
print(outside)

print("")

