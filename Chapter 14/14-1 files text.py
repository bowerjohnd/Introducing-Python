fout = open('oops.txt', 'wt')
print('Oops, I created a file.', file=fout)
fout.close()

poem = '''There was a young lady named Bright,
Whose speed was far faster than light;
She started one day
In a relative way,
And returned on the previous night.'''

print( len(poem) )

fout = open('relativity', 'wt')
fout.write(poem)
fout.close()

fout = open('relativity', 'wt')
print(poem, file=fout)
fout.close()

fout = open('relativity', 'wt')
print(poem, file=fout, sep='', end='')
fout.close()

fout = open('relativity', 'wt')
size = len(poem)
offset = 0
chunk = 100
while True:
	if offset > size:
		break
	fout.write(poem[offset:offset+chunk])
	offset += chunk
fout.close()

#fout = open('relativity', 'xt')

try:
	fout = open('relativity', 'xt')
	fout.write('stomp stomp stomp')
except FileExistsError:
	print('relativity already exists!. That was a clsoe one.')

print('')

fin = open('relativity', 'rt')
poem = fin.read()
fin.close()
print(len(poem))

poem = ''
fin = open('relativity', 'rt')
chunk = 100
while True :
	fragment = fin.read(chunk)
	if not fragment :
		break
	poem += fragment
fin.close()
print(len(poem))

print('')

poem = ''
fin = open('relativity', 'rt')
while True :
	line = fin.readline()
	if not line :
		break
	poem += line
fin.close()
print(len(poem))

print('')

poem = ''
fin = open('relativity', 'rt')
for line in fin :
	poem += line
fin.close()
print(len(poem))

print('')

fin = open('relativity', 'rt')
lines = fin.readlines()
fin.close()
print(len(lines), 'lines read')

for line in lines :
	print(line, end='')

