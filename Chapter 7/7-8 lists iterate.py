cheeses = ['brie', 'gjetost', 'havarti']
for cheese in cheeses :
	print(cheese)

print("")

cheeses = ['brie', 'gjetost', 'havarti']
for cheese in cheeses :
	if cheese.startswith('g') :
		print("I won't eat anything that starts with 'g'")
		break
	else :
		print(cheese)

print("")

cheeses = ['brie', 'gjetost', 'havarti']
for cheese in cheeses :
	if cheese.startswith('x') :
		print("I won't eat anything that starts with 'g'")
		break
	else :
		print(cheese)
else :
	print("Didn't find anything that started with 'x'")

print("")

cheeses = []
for cheese in cheeses :
	print('This shop has some lovely', cheese)
	break
else :	# no break means no cheese
	print('This is not much of a cheese shop, is it?')

print("")

days = ['Monday', 'Tuesday', 'Wednesday']
fruits = ['banana', 'orange', 'peach']
drinks = ['coffee', 'tea', 'beer']
desserts = ['tiramisu', 'ice cream', 'pie', 'pudding']

for day, fruit, drink, dessert in zip(days, fruits, drinks, desserts) :
	print(day, ": drink", drink, "- eat", fruit, "- enjoy", dessert)

print("")

english = 'Monday', 'Tuesday', 'Wednesday'
french = 'Lundi', 'Mardi', 'mercredi'
print(list( zip(english, french) ))
print(dict( zip(english, french) ))

print("")

number_list = []
number_list.append(1)
number_list.append(2)
number_list.append(3)
number_list.append(4)
number_list.append(5)
print(number_list)


number_list = []
for number in range(1, 6) :
	number_list.append(number)
print(number_list)

number_list = list(range(1, 6))
print(number_list)

number_list = [number for number in range(1,6)]
print(number_list)

number_list = [number-1 for number in range(1, 6)]
print(number_list)

print("")

a_list = [number for number in range(1, 6) if number % 2 == 1]
print(a_list)

a_list = []
for number in range(1, 6) :
	if number % 2 == 1 :
		a_list.append(number)
print(a_list)

print("")

rows = range(1, 4)
cols = range(1, 3)
for row in rows :
	for col in cols:
		print(row, col)

cells = [(row, col) for row in rows for col in cols]
for cell in cells:
	print(cell)

for row, col in cells :
	print(row, col)

print("")


