tasks = 'get gloves,get mask,give cat vitamins,call ambulance'
print(tasks.split(','))

print(tasks.split())

crypto_list = ['Yeti', 'Bigfoot', 'Loch Ness Monster']
crypto_string = ', '.join(crypto_list)
print('Found and signing book deals:', crypto_string)

setup = "a duck goes into a bar..."
print(setup.replace('duck', 'marmoset'))
print(setup)

print(setup.replace('a ', 'a famous ', 100))

print(setup.replace('a', 'a famous', 100))

world = "    earth    "
print(world)
print(world.strip())
print(world.strip(' '))
print(world.lstrip())
print(world.rstrip())
print(world.strip('!'))

blurt = "What the...!!?"
print(blurt.strip('.?!'))

import string
print(string.whitespace)	# I get male and female symbols, book shows ' \t\n\r\x0b\x0c'.
print(string.punctuation)	# This works.

print(blurt.strip(string.punctuation))

prospector = "What in tarnation ...??!!"
print(prospector.strip(string.whitespace + string.punctuation))