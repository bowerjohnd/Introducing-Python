marxes = ["Groucho", "Chico", "Harpo"]
marxes.append("Zeppo")
print(marxes)

print("")

marxes = ["Groucho", "Chico", "Harpo"]
print(marxes)
marxes.insert(2, "Gummo")
print(marxes)
marxes.insert(10, "Zeppo")
print(marxes)

print("")

print(["blah"] * 3)

print("")

marxes = ["Groucho", "Chico", "Harpo", "Zeppo"]
others = ["Gummo", "Karl"]
marxes.extend(others)
print(marxes)

print("")

marxes = ["Groucho", "Chico", "Harpo", "Zeppo"]
others = ["Gummo", "Karl"]
marxes += others
print(marxes)

print("")

marxes = ["Groucho", "Chico", "Harpo", "Zeppo"]
others = ["Gummo", "Karl"]
marxes.append(others)
print(marxes)

print("")

marxes = ["Groucho", "Chico", "Harpo"]
marxes[2] = "Wanda"
print(marxes)

print("")

numbers = [1,2,3,4]
numbers[1:3] = [8,9]
print(numbers)

numbers = [1,2,3,4]
numbers[1:3] = [7,8,9]
print(numbers)

numbers = [1,2,3,4]
numbers[1:3] = []
print(numbers)

numbers = [1,2,3,4]
numbers[1:3] = (98, 99, 100)
print(numbers)

numbers = [1,2,3,4]
numbers[1:3] = "wat?"
print(numbers)

print("")

marxes = ["Groucho", "Chico", "Harpo", "Gummo", "Karl"]
print(marxes)
print(marxes[-1])
del marxes[-1]
print(marxes)

del marxes[1]
print(marxes)

print("")

marxes = ["Groucho", "Chico", "Harpo"]
print(marxes)
marxes.remove("Groucho")
print(marxes)

print("")

marxes = ["Groucho", "Chico", "Harpo", "Zeppo"]
print(marxes)
marxes.pop()
print(marxes)
marxes.pop(1)
print(marxes)

print("")

work_quotes = ['Working hard?', 'Quick question!', 'Number one priorities!']
print(work_quotes)
work_quotes.clear()
print(work_quotes)
