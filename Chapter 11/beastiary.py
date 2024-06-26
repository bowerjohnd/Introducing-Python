from collections import defaultdict

def no_idea() :
	return 'Huh?'

beastiary = defaultdict(no_idea)
beastiary['A'] = 'Abominable Snowman'
beastiary['B'] = 'Basilisk'
print(beastiary['A'])
print(beastiary['B'])
print(beastiary['C'])

beastiary = defaultdict(lambda: 'Uh.. Huh?')
print(beastiary['E'])

