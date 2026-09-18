# Convert key-values list to flat dictionary.

key_values_list = [('a', 1), ('b', 2), ('c', 3), ('d', 4)]

myDict = {}

for key, val in key_values_list:
    myDict[key] = val

print(myDict)