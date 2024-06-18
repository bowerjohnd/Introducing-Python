def edit_story(words, func) :
	for word in words :
		print(func(word))

stairs = ['thud', 'meow', 'thud', 'hiss']

def enliven(word) :
	return word.capitalize() + '!'
edit_story(stairs, enliven)

print("")

edit_story(stairs, lambda word: word.capitalize() + '!')

print("")

print(sum(range(1, 101)))

def my_range(first=0, last=10, step=1) :
	number = first
	while number < last :
		yield number
		number += step

print(my_range)

ranger = my_range(1, 5)
print(ranger)

for x in ranger :
	print(x)

for try_again in ranger :
	print("-" + try_again)

print("")

genobj = (pair for pair in zip(['a', 'b'], ['1', '2']))
print(genobj)
for thing in genobj :
	print(thing)