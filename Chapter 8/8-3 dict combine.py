first = {'a': 'agony', 'b': 'bliss'}
second = {'b': 'bagels', 'c': 'candy'}

print({**first, **second})

third = {'d': 'donuts'}

print({**first, **second, **third})

print("")

pythons = {
	'Chapman': 'Graham',
	'Cleese': 'John',
	'Gilliam': 'Terry',
	'Idle': 'Eric',
	'Jones': 'Terry',
	'Palin': 'Michael',
	}
print(pythons)

others = {'Marx': 'Groucho', 'Howard': 'Moe'}

pythons.update(others)
print(pythons)

print("")

first = {'a': 1, 'b': 2}
second = {'b': 'platypus'}
first.update(second)
print(first)

print("")
