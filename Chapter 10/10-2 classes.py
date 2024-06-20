class Cat :
	def __init__(self, name) :
		self.name = name

furball = Cat('Grump')
print('Our latest addition: ', furball.name)

print("")

class Car() :
	pass
class Yugo(Car) :
	pass

print(issubclass(Yugo, Car))

give_me_a_car = Car()
give_me_a_yugo = Yugo()

print("")

class Car() :
	def exclaim(self) :
		print("I'm a Car!")
class Yugo(Car) :
	pass

give_me_a_car = Car()
give_me_a_yugo = Yugo()

give_me_a_car.exclaim()
give_me_a_yugo.exclaim()

print("")

class Yugo(Car) :
	def exclaim(self) :
		print("I'm a Yugo! Much like a Car, but more Yugo-ish.")

give_me_a_yugo = Yugo()

give_me_a_car.exclaim()
give_me_a_yugo.exclaim()

print("")

class Person() :
	def __init__(self, name) :
		self.name = name

class MDPerson(Person) :
	def __init__(self, name) :
		self.name = "Doctor " + name

class JDPerson(Person) :
	def __init__(self, name) :
		self.name = name + ", Esquire"

person = Person('Fudd')
doctor = MDPerson('Fudd')
lawyer = JDPerson('Fudd')
print(person.name)
print(doctor.name)
print(lawyer.name)

print("")

class Yugo(Car) :
	def exclaim(self) :
		print("I'm a Yugo! Much like a Car, but more Yugo-ish.")
	def need_a_push(self) :
		print("A little help here?")

give_me_a_yugo = Yugo()
give_me_a_yugo.need_a_push()

print("")

class Person() :
	def __init__(self, name) :
		self.name = name

class EmailPerson(Person) :
	def __init__(self, name, email) :
		super().__init__(name)
		self.email = email
bob = EmailPerson('Bob Frapples', 'bob@frapples.com')

print(bob.name)
print(bob.email)

print("")

class Animal() :
	def says(self) :
		return 'I speak!'

class Horse(Animal) :
	def says(self) :
		return 'Neigh!'

class Donkey(Animal) :
	def says(self) :
		return 'Hee-Haw!'

class Mule(Donkey, Horse) :
	pass

class Hinny(Horse, Donkey) :
	pass

print(Mule.mro())
print(Hinny.mro())

mule = Mule()
hinny = Hinny()

print(mule.says())
print(hinny.says())

print("")

class PrettyMixin() :
	def dump(self) :
		import pprint
		pprint.pprint(vars(self))

class Thing(PrettyMixin) :
	pass

t = Thing()
t.name = "Nyarlathotep"
t.feature = "ichor"
t.age = "eldritch"
t.dump()

a_car = Car()
a_car.exclaim()
Car.exclaim(a_car)