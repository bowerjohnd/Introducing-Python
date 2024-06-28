eacute1 = 'é'						# UTF-8, pasted
eacute2 = '\u00e9'					# Unicode code point
eacute3 = '\N{LATIN SMALL LETTER E WITH ACUTE}'		# Unicode name
eacute4 = chr(233)					# decimal byte value
eacute5 = chr(0xe9)					# hex byte value
print(eacute1, eacute2, eacute3, eacute4, eacute5)

print(eacute1 == eacute2 == eacute3 == eacute4 == eacute5)

import unicodedata

print(unicodedata.name(eacute1))
print(ord(eacute1))			# as a decimal integer
print(0xe9)				# Unicode hex integer

eacute_combined1 = "e\u0301"
eacute_combined2 = "e\N{COMBINING ACUTE ACCENT}"
eacute_combined3 = "e" + "\u0301"
print(eacute_combined1, eacute_combined2, eacute_combined3)

# eacute_combined in the book printed 1 character, mine printed the e and accent separately

print(eacute_combined1 == eacute_combined2 == eacute_combined3)
print(len(eacute_combined1))
print(eacute1 == eacute_combined1)

import unicodedata

eacute_normalized = unicodedata.normalize('NFC', eacute_combined1)
print(len(eacute_normalized))
print(eacute_normalized == eacute1)
print(unicodedata.name(eacute_normalized))
print(unicodedata.name(eacute1))

