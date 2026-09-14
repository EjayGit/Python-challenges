# Sort words in alphabetical order.

string = input("Enter a string: ").lower()

wordsList = string.split()

sortedWords = sorted(wordsList)

print(f'The words in order are: ')
for word in sortedWords:
    print(word)