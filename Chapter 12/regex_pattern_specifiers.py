import re

source = '''I wish I may, I wish I might
Have a dish of fish tonight.'''

# ^ = at beginning
# $ = at end
# . = everything
# \ = escape special characters and punctuation

print( re.findall('wish', source) )		# wish anywhere
print( re.findall('wish|fish', source) )	# wish or fish anywhere
print( re.findall('^wish', source) )		# wish at beginning
print( re.findall('^I wish', source) )		# I wish at beginning
print( re.findall('fish$', source) )		# fish at end
print( re.findall('fish tonight.$', source) )	# fish tonight and everything at end

print( re.findall('fish tonight\.$', source) )	# fish tonight. specifically at end
print( re.findall('[wf]ish', source) )		# w or f followed by ish
print( re.findall('[wsh]+', source) )		# one or more of w, s, or h
print( re.findall('ght\W', source) )		# ght followed by non-alphanumeric
print( re.findall('I (?=wish)', source) )	# I followed by wish
print( re.findall('(?<=I) wish', source) )	# wish preceeded by I

print( re.findall('\bfish', source) )		# conflicts between python string and regex
print( re.findall(r'\bfish', source) )		# raw ignores python string escapes

print("")

m = re.search(r'(. dish\b).*(\bfish)', source)
print(m.group())
print(m.groups())

m = re.search(r'(?P<DISH>. dish\b).*(?P<FISH>\bfish)', source)
print(m.group())
print(m.groups())
print(m.group('DISH'))
print(m.group('FISH'))