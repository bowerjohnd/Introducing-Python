import csv

with open('villains', 'rt') as fin: # context manager
	cin = csv.reader(fin)
	#villains = [row for row in cin] # a list comprehension

print(villains)