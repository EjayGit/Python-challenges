# Addition
num1 = float(input("Enter the first number for addition: "))
num2 = float(input("Enter the second number for addition: "))
print(f'The result of {num1} + {num2} is: {num1+num2}')

# Division
num1 = float(input("Enter the first number for division: "))
num2 = float(input("Enter the second number for division: "))
while num1 == 0:
    num1 = float(input("This number cannot be zero. Please enter a new number: "))
while num2 == 0:
    num2 = float(input("This number cannot be zero. Please enter a new number: "))
print(f'The result of {num1} / {num2} is: {num1/num2}')