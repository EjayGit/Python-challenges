# Find the largest element in an array.

arr = [1, 2, 3, 4, 5, 6, 8, 9, 7, 4]
largestNum = 0

for element in arr:
    if element > largestNum:
        largestNum = element

print(f'The largest number in {arr} is: {largestNum}.')