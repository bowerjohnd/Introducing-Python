small_birds = ['hummingbirds', 'finch']
extinct_birds = ['dodo', 'passenger pigeon', 'Norwegian Blue']
carol_birds = [3, 'French hens', 2, 'turtledoves']
all_birds = [small_birds, extinct_birds, carol_birds]

print(all_birds)
print("")
print(all_birds[1])
print(all_birds[1][0])

print("")

number_thing = (number for number in range(1, 6))
print(type(number_thing))