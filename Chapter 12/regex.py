import re

result = re.match('You', 'Young Frankenstein')
print(result)

youpattern = re.compile('You')
print(youpattern)
result = youpattern.match('Young Frankenstein')
print(result)

source = 'Young Frankenstein'
m = re.match('You', source)	#match starts at the beginning of source
if m :				#match returns an object; do this to see what matched
	print(m.group())

m = re.match('Frank', source)
if m :
	print(m.group())
else :
	print("no match")

if m := re.match('Frank', source) :	# walrus operator
	print(m.group())
else :
	print("no match")

m = re.search('Frank', source)
if m :
	print(m.group())

m = re.match('.*Frank', source)
if m :
	print(m.group())

m = re.search('Frank', source)
if m :					# search returns an object
	print(m.group())

m = re.findall('n', source)
print(m) 				# findall returns a list
print('Found', len(m), 'matches')

m = re.findall('n.', source)		# n. find n with 1 character after
print(m)

m = re.findall('n.?', source)		# n.? means the . is optional
print(m)

m = re.split('n', source)
print(m)				# split returns a list

m = re.sub('n', '?', source)
print(m)				# sub returns a string

