class TeenyClass() :
	def __init__(self, name) :
		self.name = name

teeny = TeenyClass('itsy')
print(teeny.name)

from dataclasses import dataclass
@dataclass
class TeenyDataClass :
	name: str

teeny = TeenyDataClass('bitsy')
print(teeny.name)

print("")

from dataclasses import dataclass
@dataclass
class AnimalClass :
	name: str
	habitat: str
	teeth: int = 0

snowman = AnimalClass('yeti', 'Himilayas', 46)
duck = AnimalClass(habitat='lake', name='duck')
print(snowman)
print(duck)

print(duck.habitat)
print(snowman.teeth)

print("")
