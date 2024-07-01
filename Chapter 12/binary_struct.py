import struct

valid_png_header = b'\x89PNG\r\n\x1a\n'
data = b'\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR' + \
	b'\x00\x00\x00\x9a\x00\x00\x00\x8d\x08\x02\x00\x00\x00\xc0'

if data[:8] == valid_png_header :
	width, height = struct.unpack('>LL', data[16:24])
	print('Valid PNG, width', width, 'height', height)
else :
	print('Not a valid PNG') 

print(data[16:20])
print(data[20:24])

print("")

print(0x9a)
print(0x8d)

print("")

print( struct.pack('>L', 154) )
print( struct.pack('>L', 141) )

print("")

print( struct.unpack('>2L', data[16:24]) )
print( struct.unpack('>16x2L6x', data) )