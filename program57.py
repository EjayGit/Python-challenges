#  Clone or Copy a list.

original_list = [1, 2, 3, 4, 5]

# 1. Using Using the Slice Operator
newList = original_list[:]
print(newList)

# 2. Using the list() constructor
newList = list(original_list)
print(newList)

# 3. Using List Comprehension
