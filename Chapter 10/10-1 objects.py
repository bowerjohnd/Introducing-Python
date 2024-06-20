class Cat() :
	pass

a_cat = Cat()
another_cat = Cat()

print(a_cat)
print(another_cat)

print("")

a_cat.age = 3
a_cat.name = "Mr. Fuzzybuttons"
a_cat.nemesis = another_cat

print(a_cat.age)
print(a_cat.name)
print(a_cat.nemesis)

print("")

a_cat.nemesis.name = "Mr. Bigglesworth"
print(a_cat.nemesis.name)

print("")

