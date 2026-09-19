# check order of character in string.

# Input strings
inputString = "hello world"
referenceString = "helo wrd"

def checkCharOrder(inputString, referenceString):
    inputDict = dict.fromkeys(inputString)
    refDict = dict.fromkeys(referenceString)
    return inputDict == refDict

print(checkCharOrder(inputString, referenceString))