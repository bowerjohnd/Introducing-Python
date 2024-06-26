from random import choice

print(choice( [23, 9, 46, 'bacon', 0x123abc] ))
print(choice( ('a', 'one', 'and-a', 'two') ))
print(choice( range(100) ))
print(choice( 'alphabet' ))

print("---")

from random import sample

print(sample( [23, 9, 46, 'bacon', 0x123abc], 3 ))
print(sample( ('a', 'one', 'and-a', 'two'), 2 ))
print(sample( range(100), 4 ))
print(sample( 'alphabet', 7 ))

print("---")

from random import randint

print(randint(38, 74))
print(randint(38, 74))
print(randint(38, 74))

print("---")

from random import randrange

print(randrange(38, 74))
print(randrange(38, 74, 10))
print(randrange(38, 74, 10))

print("---")

from random import random

print(random())
print(random())
print(random())