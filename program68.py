# Find the sum of all items in a dictionary.

# Sample dictionary
my_dict = {
 'a': 10,
 'b': 20,
 'c': 30,
 'd': 40,
 'e': 50
}

sum = 0

for value in my_dict.values():
    sum += value

print(sum)