# Count occurrences of an element in a list.

num = int(input("Enter the number to count: "))

myList = my_list = [1, 2, 3, 4, 2, 5, 2, 3, 4, 6, 5]

def countOccurences(myList, num):
    count = 0
    # for each element in list
    for element in myList:
        # if element == num
        if element == num:
            # count ++
            count += 1
    return count

print(f'The number of times {num} appears in the list is: {countOccurences(myList, num)}.')