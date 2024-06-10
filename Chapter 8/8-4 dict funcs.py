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

del pythons['Marx']
print(pythons)

print("")

print(len(pythons))
pythons.pop('Palin')
print(pythons)

print(len(pythons))
#pythons.pop('Palin')
print(pythons)

pythons.pop('First', 'Hugo')
print(pythons)

print(len(pythons))

print("")

pythons.clear()
print(pythons)
pythons = {}
print(pythons)

print("")

pythons = {
	'Chapman': 'Graham', 
	'Cleese': 'John',
	'Jones': 'Terry',
	'Palin': 'Michael',
	'Idle': 'Eric',
	}
print('Chapman' in pythons)
print('Palin' in pythons)
print('Gilliam' in pythons)

print("")

signals = {
	'green': 'go',
	'yellow': 'go faster',
	'red': 'smile for the camera',
	}
save_signals = signals
signals['blue'] = 'confuse everyone'
print(save_signals)

print("")

signals.pop('blue')
print(signals)

original_signals = signals.copy()
signals['blue'] = 'confuse everyone'
print(signals)
print(original_signals)

print("")

signals = {
	'green': 'go',
	'yellow': 'go faster',
	'red': ['stop', 'smile'],
	}
signals_copy = signals.copy()
print(signals)
print(signals_copy)

print("")

signals['red'][1] = 'sweat'
print(signals)
print(signals_copy)

print("")

import copy
signals = {
	'green': 'go',
	'yellow': 'go faster',
	'red': ['stop', 'smile'],
	}
signals_copy = copy.deepcopy(signals)

print(signals)
print(signals_copy)

signals['red'][1] = 'sweat'

print(signals)
print(signals_copy)

print("")

a = {1:1, 2:2, 3:3}
b = {3:3, 1:1, 2:2}
print(a == b)
#print(a <= b)

a = {1: [1,2], 2:[1], 3:[1]}
b = {1: [1,1], 2:[1], 3:[1]}
print(a == b)
