empty_set = set()
print(empty_set)

even_numbers = {0,2,4,6,8}
print(even_numbers)
odd_numbers = {1,3,5,7,9}
print(odd_numbers)

print("")

print(set('letters'))

print(set( ['Dasher', 'Dancer', 'Prancer', 'Mason-Dixon'] ))
print(set( ('Ummagumma', 'Echoes', 'Atom Heart Mother') ))
print(set( {'apple': 'red', 'orange': 'orange', 'cherry': 'red'} ))

print("")

reindeer = set( ['Dasher', 'Dancer', 'Prancer', 'Mason-Dixon'] )
print(len(reindeer))

print("")

s = set((1,2,3))
print(s)
s.add(4)
print(s)

s.remove(3)
print(s)

print("")
