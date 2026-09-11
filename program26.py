# Build a simple 4 operation calculator.

num1 = float(input("Enter the first value: "))
operation = int(input("Would you like to add (enter 1), subtract (enter 2), multiply (enter 3), or divide (enter 4)? "))
while operation < 1 or operation > 4:
    int(input("Would you like to add (enter 1), subtract (enter 2), multiply (enter 3), or divide (enter 4)? "))
num2 = float(input("Enter the second value: "))

def add(num1, num2):
    return num1 + num2

def sub(num1, num2):
    return num1 - num2

def mul(num1, num2):
    return num1 * num2

def div(num1, num2):
    return num1 / num2

if operation == 1:
    print(add(num1, num2))
elif operation == 2:
    print(sub(num1, num2))
elif operation == 3:
    print(mul(num1, num2))
elif operation == 4:
    print(div(num1, num2))
else:
    print("whoopsy")