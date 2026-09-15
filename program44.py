# Check if a number is a Happy Number

num = int(input("Enter the number: "))

def seenTwice(seen):
    # if there are any numbers duplicated in seen, return True.
    if len(seen) == len(set(seen)):
        return False
    else:
        return True

def isHappy(num):
    # Init store for prev seen numbers
    seen = []
    seen.append(num)

    # while not in seen
    while not seenTwice(seen):
        sum = 0
        for i in range(0, len(str(seen[len(seen)-1]))):
            sum = sum + int(str(seen[-1])[i]) ** 2
        seen.append(sum)

    if int(1) in seen:
        return True
    else: 
        return False
                

print(f'The number {num} is Happy: {isHappy(num)}')