# accept a comma separated sequence of words as input and prints the words in a comma-separated sequence after sorting them alphabetically

# Input
words = str(input("Enter the comma separated words here: "))

# Split the str into a list
wordsList = words.split(',')

# Sort the list into alphabetical order
wordsList.sort()

# join elements into a single comma separated string.
print(','.join(wordsList))