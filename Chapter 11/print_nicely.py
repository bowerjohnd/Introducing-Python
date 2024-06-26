from collections import OrderedDict
from pprint import pprint

quotes = OrderedDict([
	('Moe', 'A wise guy, huh?'),
	('Larry', 'Ow!'),
	('Curly', 'Nyuk nyuk!'),
	])

print(quotes)

print("---")

pprint(quotes)		# supposed to try to align everything nicely

