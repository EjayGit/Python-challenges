# Find sum of elements in a list.

myList = [12, 23, 34, 45, 56, 67, 78, 89]

def sumList(myList):
    sum = 0
    for num in myList:
        sum += num
    return sum

print(f'The sum of the list is: {sumList(myList)}.')