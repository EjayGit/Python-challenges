# accept a sequence of whitespace separated words as input and prints the words after removing all duplicate words and sorting them alphanumerically.

# Input
words = str(input("Enter the words here: "))

# put into list of strings
wordsList = list(set(words.split(' ')))

# sort
wordsList.sort()

print(' '.join(wordsList))