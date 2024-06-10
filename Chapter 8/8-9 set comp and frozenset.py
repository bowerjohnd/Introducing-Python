a_set = {number for number in range(1,6) if number % 3 == 1}
print(a_set)

print("")

print(frozenset( [3, 2, 1]) )
print(frozenset( set([2, 1, 3]) ))
print(frozenset( {1, 2, 3} ))
print(frozenset( (2, 3, 1) ))

fs = frozenset( [3, 2, 1] )
print(fs)

#fs.add(4)

print("")

marx_list = ['Groucho', 'Chico', 'Harpo']
marx_tuple = ('Groucho', 'Chico', 'Harpo')
marx_dict = {'Groucho': 'banjo', 'Chico': 'piano', 'Harpo': 'harp'}
marx_set = {'Groucho', 'Chico', 'Harpo'}

print(marx_list[2])
print(marx_tuple[2])
print(marx_dict['Harpo'])
print('Harpo' in marx_list)
print('Harpo' in marx_tuple)
print('Harpo' in marx_dict)
print('Harpo' in marx_set)

print("")

marxes = ['Groucho', 'Chico', 'Harpo']
pythons = ['Chapman', 'Cleese', 'Gilliam', 'Jones', 'Palin']
stooges = ['Moe', 'Curly', 'Larry']

tuple_of_lists = marxes, pythons, stooges
print(tuple_of_lists)

print("")

list_of_lists = [marxes, pythons, stooges]
print(list_of_lists)

print("")

dict_of_lists = {'Marxes': marxes, 'Pythons': pythons, 'Stooges': stooges}
print(dict_of_lists)

print("")

houses = {
	(44.79, -93.14, 285): 'My House',
	(38.89, -77.03, 13): 'The White House',
	}
print(houses)