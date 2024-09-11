bdata = bytes(range(0, 256))
print(len(bdata))

fout = open('bfile', 'wb')
print(fout.write(bdata))
fout.close()

fout = open('bfile', 'wb')
size = len(bdata)
offset = 0
chunk = 100
while True :
	if offset > size :
		break
	fout.write(bdata[offset:offset+chunk])
	offset += chunk
fout.close()

print('')

fin = open('bfile', 'rb')
bdata = fin.read()
print(len(bdata))
fin.close()

print('')

with open('relativity', 'rt') as fin :
	poem = fin.read()
with open('newRelativity', 'wt') as fout :
	fout.write(poem)

#file is closed automatically
#print(fin.read())

print('')

fin = open('bfile', 'rb')
print(fin.tell())
print(fin.seek(255))
bdata = fin.read()
print(len(bdata))
print(bdata[0])
fin.close()

print('')

import os
print(os.SEEK_SET)
print(os.SEEK_CUR)
print(os.SEEK_END)

fin = open('bfile', 'rb')
print(fin.seek(-1, 2))
print(fin.tell())

bdata = fin.read()
print(len(bdata))
print(bdata[0])

fin.close()

print('')

fin = open('bfile', 'rb')
print(fin.seek(254, 0))
print(fin.tell())
print(fin.seek(1, 1))
print(fin.tell())

bdata = fin.read()
print(len(bdata))
print(bdata[0])

fin.close()

