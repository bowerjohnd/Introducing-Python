# Only useful in Python versions before 3.7

quotes = {
	'Moe': 'A wise guy, huh?',
	'Larry': 'Ow!',
	'Curly': 'Nyuk nyuk!',
	}

for stooge in quotes :
	print(stooge)

print("---")

from collections import OrderedDict
quotes = OrderedDict([
	('Moe', 'A wise guy, huh?'),
	('Larry', 'Ow!'),
	('Curly', 'Nyuk nyuk!'),
	])

for stooge in quotes :
	print(stooge)