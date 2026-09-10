# Print the Fibonacci sequence.
terms = int(input("How many terms would you like to print? "))
while terms < 2:
    terms = int(input("terms must be an integer equal to or greater than 2: "))
n1 = 0
n2 = 1
sum = 0
print(n1)
print(n2)
# for each term to be printed
for term in range(1, terms-1):
    # sum n1 and n2
    sum = n1 + n2
    print(sum)
    # refresh values
    n1, n2 = n2, sum