# Find the smallest number in a list.

myList = [30, 10, -45, 5, 20]

def smallestNum(myList):
    smallest = myList[0]
    for num in myList:
        if num<smallest:
            smallest = num
    return smallest
        
print(f'The smallest number in myList is: {smallestNum(myList)}')