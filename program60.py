#  removing 𝑖th character from a string.

string = 'HellOo Universe'
characterNum = 5

def removeChar(string, character):
    newString = string[:character-1]
    newString = newString + string[character:]
    return newString

print(f'The new string is: {removeChar(string, characterNum)}.')