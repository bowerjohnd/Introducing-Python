# imports are not working for me after installing construct per instructions in book

from construct import Struct, Magic, UBInt32, Const, String
# adapted from code at https://github.com/construct

fmt = Struct('png',
	#Magic(b'\x89PNC\r\n\x1a\n'),
	UBInt32('length'),
	Const(String('type', 4), b'IHDR'),
	UBInt32('width'),
	UBInt32('height')
	)

data = b'\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR' + \
	b'\x00\x00\x00\x9a\x00\x00\x00\x8d\x08\x02\x00\x00\x00xc0'

result = fmt.parse(data)
print(result)