# Insertion at the beginning of dict.

myDict = {'b':2, 'c':3, 'd':4}

newKeyVal = {'a':1}

newKeyVal.update(myDict)

myDict = newKeyVal

print(myDict)

