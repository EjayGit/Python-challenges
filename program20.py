# Find Armstrong number in an interval.

lower = int(input("Enter the lower boundary: "))
upper = int(input("Enter the upper boundary: "))

def isArmstrong(num):
    # Calculate how many digits there are
    strDigits = str(num)
    digits = len(strDigits)
    sum = 0

    # For each digit
    for i in strDigits:
        # sum its value to the power of the number of digits.
        sum = sum + int(i)**digits

    if sum == num:
        return True
    else:
        return False

for i in range(lower, upper+1):
    if isArmstrong(i):
        print(i)