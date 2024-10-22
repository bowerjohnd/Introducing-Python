import xml.etree.ElementTree as et

tree = et.ElementTree(file='16-6 menu.xml')
root = tree.getroot()


print("")
print(root.tag)
print("")

for child in root:
	print('tag:', child.tag, 'attributes:', child.attrib)
	for grandchild in child:
		print('\ttag:', grandchild.tag, 'attributes:', grandchild.attrib)

print("")

print("Menu sections:",  len(root)) # number of menu sections
print("Breakfast items:", len(root[0])) # number of breakfast items