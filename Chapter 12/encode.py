snowman = '\u2603'
print(len(snowman))

ds = snowman.encode('utf-8')
print(len(ds))
print(ds)

#ds = snowman.encode('ascii')
print(snowman.encode('ascii', 'ignore'))
print(snowman.encode('ascii', 'replace'))
print(snowman.encode('ascii', 'backslashreplace'))
print(snowman.encode('ascii', 'xmlcharrefreplace'))

