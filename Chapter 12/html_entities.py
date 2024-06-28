import html

print(html.unescape("&egrave;"))
print(html.unescape("&#233;"))
print(html.unescape("&#xe9;"))

from html.entities import html5

print(html5["egrave"])
print(html5["egrave;"])

char = '\u00e9'
dec_value = ord(char)
print(html.entities.codepoint2name[dec_value])

place = 'caf\u00e9'
byte_value = place.encode('ascii', 'xmlcharrefreplace')
print(byte_value)
print(byte_value.decode())

