# Determine if a number is a Harshad number.

num = int(input("Enter the number: "))

def isHarshad(num):
    # sum digits
    sum = 0
    for i in range(0, len(str(num))):
        sum = sum + int(str(num)[i])

    # if num mod sum == 0 then return True
    if num % sum == 0:
        return True
    # else return False
    else:
        return False

print(isHarshad(num))