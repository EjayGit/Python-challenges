# Find the largest number in a list.

myList = [30, 10, -45, 35, 20]

def largestNum(myList):
    largest = myList[0]
    for num in myList:
        if num > largest:
            largest = num
    return largest

print(f'The largest number in the list is: {largestNum(myList)}.')