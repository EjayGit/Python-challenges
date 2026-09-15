# Print all Disarium numbers between 1 and 100.

lower = 1
upper = 1000

def isDisarium(num):
    # Convert to string
    string = str(num)

    # for each char calculate the value to the power of its position.
    sum = 0
    for i in range(0, len(string)):
        sum = sum + int(string[i])**(i+1)
    # If the sum is equal to the input num, then return True, otherwise return False.
    if sum == num:
        return True
    else:
        return False

for i in range(lower, upper):
    if isDisarium(i):
        print(i)
    else:
        continue