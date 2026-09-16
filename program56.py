# Remove empty lists from a list.

list_of_lists = [[1, 2, 3], [], [4, 5], [], [6, 7, 8], []]

def isEmptyList(element):
    if element == []:
        return True

def removeEmpty(myList):
    newList = []
    # for each element in the list
    for element in myList:
        # check for an empty list
        if isEmptyList(element):
            # if empty list remove element
            continue
        else:
            newList.append(element)
    # return new list
    return newList

print(f'The new List is: {removeEmpty(list_of_lists)}.')