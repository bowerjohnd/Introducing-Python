animal = 'fruitbat'
def print_global() :
	print('inside print_global:', animal)

print('at the top level:', animal)
print_global()

print("")

def change_and_print_global() :
	print('inside change_and_print_global:', animal)
	animal = 'wombat'
	print('after the change:', animal)

# change_and_print_global()

print("")

def change_local() :
	animal = 'wombat'
	print('inside change_local:', animal, id(animal))
change_local()
print(animal)
print(id(animal))

print("")

animal = 'fruitbat'
def change_and_print_global() :
	global animal
	animal = 'wombat'
	print('inside change_and_print_global:', animal)

print(animal)
change_and_print_global()
print(animal)

print("")

animal = 'fruitbat'
def change_local() :
	animal = 'wombat' # local variable
	print('locals:', locals())
print(animal)
change_local()
print('globals:', globals()) 
print(animal)

print("")

def amazing() :
	'''This is the amazing function.
	Want to see it again?'''
	print('This function is named:', amazing.__name__)
	print('And its doctstring is:', amazing.__doc__)
amazing()
