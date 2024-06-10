word = 'letters'

letter_counts = {letter: word.count(letter) for letter in word}
print(letter_counts)

print("")

letter_counts = {letter: word.count(letter) for letter in set(word)}
print(letter_counts)

print("")

vowels = 'aeiou'
word = 'onomatopoeia'

vowel_counts = {
	letter: word.count(letter) 
	for letter in set(word)
	if letter in vowels
	}
print(vowel_counts)