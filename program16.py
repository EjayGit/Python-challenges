# Find the factorial of a number.

num = int(input("Enter an integer: "))
factorial = 1
# for each number from num to 1
for i in range(num,1,-1):
    # multiply the number with the next in the sequence.
    factorial = factorial * i
print(factorial)