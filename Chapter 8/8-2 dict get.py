some_pythons = { 
	'Graham': 'Chapman',
	'John': 'Cleese',
	'Eric': 'Idle',
	'Terry': 'Gilliam',
	'Michael': 'Palin',
	'Terry': 'Jones',
	}
print(some_pythons)

print("")

print(some_pythons['John'])
#print(some_pythons['Groucho'])

print('Groucho' in some_pythons)

print(some_pythons.get('Groucho', 'Not a Python'))
print(some_pythons.get('Groucho'))

print("")

signals = {'green': 'go', 'yellow': 'go faster', 'red': 'smile for the camera'}
print(signals.keys())

print(list( signals.keys() ))
print(list( signals.values() ))
print(list( signals.items() ))
print(len(signals))

