# Extract Unique dictionary values.

# Sample dictionary
my_dict = {
 'a': 10,
 'b': 20,
 'c': 10,
 'd': 30,
 'e': 20
}

mySet = set()

for value in my_dict.values():
    mySet.add(value)

print(mySet)