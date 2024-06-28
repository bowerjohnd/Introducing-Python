import string
import re

printable = string.printable
print(len(printable))
print(printable[0:50])
print(printable[50:])

print('')

print(re.findall('\d', printable))	# find all digits

print('')

print(re.findall('\w', printable))	# find all alphanumeric

print('')

print(re.findall('\s', printable))	# find all whitespace

print('')

x = 'abc' + '-/*' + '\u00ea' + '\u0115'

print(re.findall('\w', x))