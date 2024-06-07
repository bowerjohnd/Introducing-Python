marxes = ['Groucho', 'Chico', 'Harpo']
print(', '.join(marxes)) 	# string.join

print("")

friends = ['Harry', 'Hermione', 'Ron']
print(friends)
separator = ' * '
joined = separator.join(friends)
print(joined)
separated = joined.split(separator)
print(separated)
print(separated == friends)

print("")

marxes = ['Groucho', 'Chico', 'Harpo']
sorted_marxes = sorted(marxes)
print(sorted_marxes)
print(marxes)

print("")

marxes.sort()
print(marxes)

print("")

numbers = [2,1,4.0,3]
numbers.sort(reverse=True)
print(numbers)

print("")

marxes = ['Groucho', 'Chico', 'Harpo']
print(marxes)
print(len(marxes))

print("")

a = [1,2,3]
print(a)
b = a
print(b)
a[0] = 'surprise'
print(a)
print(b)

print("")

a = [1,2,3]
b = a.copy()
c = list(a)
d = a[:]

a[0] = 'integers lists are boring'
print(a)
print(b)
print(c)
print(d)

print("")

a = [1, 2 , [8, 9]]
b = a.copy()
c = list(a)
d = a[:]

print(a)
print(b)
print(c)
print(d)

a[2][1] = 10
print(a)
print(b)
print(c)
print(d)

print("")

import copy
a = [1, 2 , [8, 9]]
b = copy.deepcopy(a)
print(a)
print(b)
a[2][1] = 10
print(a)
print(b)

print("")

a = [7, 2]
b = [7, 2, 9]
print(a == b)
print(a <= b)
print(a < b)
