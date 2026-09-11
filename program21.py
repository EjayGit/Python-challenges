# Sum natural numbers

lower = int(input("Enter the lower boundary: "))
while lower <1:
    lower = int(input("The lower boundary must be greater than 0: "))
upper = int(input("Enter the upper boundary: "))
while upper < lower:
    upper = int(input(f'The upper boundary must be greater than {lower}: '))

sum = 0
for i in range(lower, upper+1):
    sum = sum + i
print(f'The sum of the Natural numbers is {sum}.')