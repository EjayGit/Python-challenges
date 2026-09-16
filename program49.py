# Multiply all elements in a list.

myList = [10, 20, 30, 40, 50]


def mulList(myList):
    sum = 1
    for num in myList:
        sum *= num
    return sum

print(f'The value of the elements multiplied is: {mulList(myList)}')