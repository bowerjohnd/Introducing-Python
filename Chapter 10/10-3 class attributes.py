class Duck :
	def __init__(self, input_name) :
		self.name = input_name

fowl = Duck('Daffy')
print(fowl.name)

fowl.name = 'Daphne'
print(fowl.name)

print("")

class Duck :
	def __init__(self, input_name) :
		self.hidden_name = input_name
	def get_name(self) :
		print('inside the getter')
		return self.hidden_name
	def set_name(self, input_name) :
		print('inside the setter')
		self.hidden_name = input_name

don = Duck('Donald')
print(don.get_name())
don.set_name('Donna')
print(don.get_name())

print("")

class Duck :
	def __init__(self, input_name) :
		self.hidden_name = input_name
	def get_name(self) :
		print('inside the getter')
		return self.hidden_name
	def set_name(self, input_name) :
		print('inside the setter')
		self.hidden_name = input_name
	name = property(get_name, set_name)

don = Duck('Donal')
print(don.get_name())
don.set_name('Donna')
print(don.get_name())

print(don.name)
don.name = 'Donna'
print(don.name)

print("")

class Duck :
	def __init__(self, input_name) :
		self.hidden_name = input_name
	@property
	def name(self) :
		print('inside the getter')
		return self.hidden_name
	@name.setter
	def name(self, input_name) :
		print('inside the setter')
		self.hidden_name = input_name

fowl = Duck('Howard')
print(fowl.name)
fowl.name = 'Donald'
print(fowl.name)

print("")

class Circle() :
	def __init__(self, radius) :
		self.radius = radius
	@property
	def diameter(self) :
		return 2 * self.radius

c = Circle(5)
print(c.radius)
print(c.diameter)

c.radius = 7
print(c.diameter)

# c.diameter = 20

print("")

class Duck() :
	def __init__(self, input_name) :
		self.__name = input_name
	@property
	def name(self) :
		print('inside the getter')
		return self.__name
	@name.setter
	def name(self, input_name) :
		print('inside the setter')
		self.__name = input_name

fowl = Duck('Howard')
print(fowl.name)
fowl.name = 'Donald'
print(fowl.name)
# print(fowl.__name)	# 'Duck' has no attribute '__name' error
print(fowl._Duck__name)

print("")

class Fruit :
	color = 'red'
blueberry = Fruit()
print(Fruit.color)
print(blueberry.color)

blueberry.color = 'blue'
print(blueberry.color)
print(Fruit.color)

Fruit.color = 'orange'
print(Fruit.color)
print(blueberry.color)

new_fruit = Fruit()
print(new_fruit.color)

print("")

