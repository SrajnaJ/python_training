#assign1:
squares_of_evens = [x**2 for x in range(1, 21) if x % 2 == 0]
print(squares_of_evens)

#assign2:
words = ["apple", "banana", "orange", "grape", "umbrella", "kiwi", "elephant", "dog"]
vowel_words = [word for word in words if word[0].lower() in "aeiou"]
print(vowel_words)
