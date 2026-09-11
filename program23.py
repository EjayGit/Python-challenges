# Find the HCF of 2 numbers

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

def gcd(num1, num2):
    return num1 if num2 == 0 else gcd(num2, num1%num2)

print(f'The HCF of {num1} and {num2} is {gcd(num1, num2)}.')