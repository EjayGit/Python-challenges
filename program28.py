# Find the Factorial using Recursion

num = int(input("Enter the number: "))
while num < 0:
    num = int(input("The number must be equal to or greater to 0: "))

def fac(n):
    if n == 0:
        return 1
    else:
        return (n*fac(n-1))

print(fac(num))