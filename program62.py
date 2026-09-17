# Check if a given string is binary string or not.

inputStr = "1001100"

def checkBinary(inputStr):
    # for each char in str, check if 0 or 1.
    for i in range(0, len(inputStr)):
        # if any char is not 0 or 1, return False
        if inputStr[i] != "0" and inputStr[i] != "1":
            return False
    # otherwise return True
    return True

print(f'The string {inputStr} is binary: {checkBinary(inputStr)}')