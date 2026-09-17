# Find uncommon words from two strings.

string1 = "This is the first string"
string2 = "This is the second string"

def findUncommon(string1, string2):
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
    uncommonList = []
    for word in list1:
        if word not in commonList:
            uncommonList.append(word)
    for word in list2:
        if word not in commonList:
            uncommonList.append(word)
            
    return uncommonList

print(findUncommon(string1, string2))