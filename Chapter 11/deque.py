def palindrome(word) :
	from collections import deque
	dq = deque(word)
	while len(dq) > 1 :
		if dq.popleft() != dq.pop() :
			return False
	return True

print(palindrome('a'))
print(palindrome('racecar'))
print(palindrome(''))
print(palindrome('radar'))
print(palindrome('halibut'))

print("---")

def another_palindrome(word) :
	return word == word[::-1]

print(another_palindrome('radar'))
print(another_palindrome('halibut'))
