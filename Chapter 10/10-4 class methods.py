class A() :
	count = 0
	def __init__(self) :
		A.count += 1
	def exclaim(self) :
		print("I'm an A!")
	@classmethod
	def kids(cls) :
		print("A has", cls.count, "little objects.")

easy_a = A()
breezy_a = A()
wheezy_a = A()
A.kids()

print("")

class CoyoteWeapon() :
	@staticmethod
	def commercial() :
		print("This CoyoteWeapon has been brought to you by Acme")

CoyoteWeapon.commercial()

print("")

class Quote() :
	def __init__(self, person, words) :
		self.person = person
		self.words = words
	def who(self) :
		return self.person
	def says(self) :
		return self.words + '.'

class QuestionQuote(Quote) :
	def says(self) :
		return self.words + '?'

class ExclamationQuote(Quote) :
	def says(self) :
		return self.words + '!'

hunter = Quote('Elmer Fudd', "I'm hunting wabbits")
print(hunter.who(), 'says:', hunter.says())

hunted1 = QuestionQuote('Bugs Bunny', "What's up, doc")
print(hunted1.who(), 'says:', hunted1.says())

hunted2 = ExclamationQuote('Daffy Duck', "It's rabbit season")
print(hunted2.who(), 'says:', hunted2.says())

print("")

class BabblingBrook() :
	def who(self) :
		return 'Brook'
	def says(self) :
		return 'Babble'

brook = BabblingBrook()

def who_says(obj) :
	print(obj.who(), 'says', obj.says())

who_says(hunter)
who_says(hunted1)
who_says(hunted2)
who_says(brook)