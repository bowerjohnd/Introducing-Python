empty_tuple = ()

print(empty_tuple)

print("")

one_marx = "Groucho",
print(one_marx)

print("")

one_marx = ("Groucho",)
print(one_marx)

print("")

one_marx = ("Groucho")		# not a tuple without a ','
print(one_marx)
print(type(one_marx))

print("")

marx_tuple = "Groucho", "Chico", "Harpo"
print(marx_tuple)

one_marx = "Groucho",
print(type(one_marx))
print(type("Groucho",))
print(type(("Groucho",)))

print("")

marx_tuple = ("Groucho", "Chico", "Harpo")
a, b, c = marx_tuple
print(a)
print(b)
print(c)

print("")

password = "swordfish"
icecream = "tuttifrutti"
password, icecream = icecream, password
print(password)
print(icecream)