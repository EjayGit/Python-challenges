# Find common words from two Strings.

string1 = "This is the first string"
string2 = "This is the second string"

def findCommon(string1, string2):
    # convert strings to lists.
    list1 = string1.split()
    list2 = string2.split()
    commonList = []
    # for each element in list1.
    for element1 in list1:
        if element1 not in commonList:
            # check for existence in list2.
            for element2 in list2:
                if element1 == element2:
                    commonList.append(element2)
                    break
    return commonList

print(f'Common words are: {findCommon(string1, string2)}.')