from collections import defaultdict
food_counter = defaultdict(int)

for food in ['spam', 'spam', 'eggs', 'spam'] :
	food_counter[food] += 1

for food, count in food_counter.items() :
	print(food, count)

print("---")

dict_counter = {}
for food in ['spam', 'spam', 'eggs', 'spam'] :
	if not food in dict_counter :
		dict_counter[food] = 0
	dict_counter[food] += 1

for food, count in dict_counter.items() :
	print(food, count)

print("---")

from collections import Counter

breakfast = ['spam', 'spam', 'eggs', 'spam']
breakfast_counter = Counter(breakfast)
print(breakfast_counter)

print(breakfast_counter.most_common())
print(breakfast_counter.most_common(1))

print("---")

print(breakfast_counter)

lunch = ['eggs', 'eggs', 'bacon']
lunch_counter = Counter(lunch)
print(lunch_counter)

print(breakfast_counter + lunch_counter)
print(breakfast_counter - lunch_counter)
print(lunch_counter - breakfast_counter)
print(breakfast_counter & lunch_counter)
print(breakfast_counter | lunch_counter)
