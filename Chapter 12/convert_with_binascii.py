import binascii

valid_png_header = b'\x89PNC\r\n\x1a\n'

print(valid_png_header)
first = binascii.hexlify(valid_png_header)
print(first)
second = binascii.unhexlify(first)
print(second)
