marx_list = ["Groucho", "Chico", "Harpo"]
print(tuple(marx_list))

print("")

print( ("Groucho",) + ("Chico", "Harpo") )

print("")

print(("yada", ) * 3)

print("")

a = (7, 2)
b = (7, 2, 9)
print(a == b)
print(a <= b)
print(a < b)

print("")

words = ("fres", "out", "of", "ideas")
for word in words :
	print(word)

print("")

t1 = ("Fee", "Fie", "Foe")
t2 = ("Flop",)
t1 += t2
print(t1)

print("")

t1 = ("Fee", "Fie", "Foe")
t2 = ("Flop",)
print(id(t1))
t1 += t2
print(id(t1))

print("")
