# Find all duplicate characters in a string.

inputStr = 'A very long sentence'

def findDuplicates(inputStr):
    duplicates = []
    for char1 in range(0,len(inputStr)):
        for char2 in range(char1+1, len(inputStr)):
            if inputStr[char1] == inputStr[char2] and inputStr[char1] not in duplicates and inputStr[char1] != " ":
                duplicates.append(inputStr[char1])
                break
    return duplicates

print(f'Duplicate characters are: {findDuplicates(inputStr)}.')