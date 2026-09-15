# Remove punctuation from a string.

# Define punctuation
punc = '''!@#$%^&*()_+-=[]{};:'",./<>?\|"'''

string = str(input("Enter the string: "))

# for each char in string, delete char if same as any in punc
newString = ''
for char in string:
    if char not in punc:
        newString = newString+char

print(newString)