blist = [1, 2, 3, 255]
the_bytes = bytes(blist)
print(the_bytes)

the_byte_array = bytearray(blist)
print(the_byte_array)

print(b'\x61')
print(b'\x01abc\xff')

#the_bytes[1] = 127

print(the_byte_array)
the_byte_array[1] = 127
print(the_byte_array)

the_bytes = bytes(range(0,256))
the_byte_array = bytearray(range(0,256))
print(the_bytes)