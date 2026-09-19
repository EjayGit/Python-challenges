# Sort Python Dictionaries by Key or Value.

sample_dict = {'apple': 3, 'cherry': 2, 'banana': 1, 'date': 4}

# By Key
print(sample_dict.items()) # This is what sample_dict.items() returns.
sortedDict = dict(sorted(sample_dict.items()))
print(sortedDict)


# By Value
sortedDict = dict(sorted(sample_dict.items(), key=lambda item: item[1] )) # Hovering over the key shows you what key is -> a tuple with a str in position 0 and int in position 1. Hence item: item[1] as we want the ints.
print(sortedDict)