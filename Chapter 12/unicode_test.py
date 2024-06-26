import unicodedata

def unicode_test(value) :
	name = unicodedata.name(value)
	value2 = unicodedata.lookup(name)
	print('value="%s", name="%s", value2="%s"' % (value, name, value2))

unicode_test('A')
unicode_test('\u00a2')
unicode_test('\u20ac')
unicode_test('\u2603')

place = 'café'
print(place)

print(unicodedata.name('\u00e9'))
#print(unicodedata.lookup('E WITH ACUTE, LATIN SMALL LETTER'))
print(unicodedata.lookup('LATIN SMALL LETTER E WITH ACUTE'))

place = 'caf\u00e9'
print(place)
place = 'caf\N{LATIN SMALL LETTER E WITH ACUTE}'
print(place)

u_umlaut = '\N{LATIN SMALL LETTER U WITH DIAERESIS}'
print(u_umlaut)

drink = 'Gew' + u_umlaut + 'rztraminer'
print('Now I can finally have my', drink, 'in a', place)

print( len('$') )
print( len('\U0001f47b') )

print( chr(233) )
print( chr(0xe9) )
print( chr(0x1fc6) )