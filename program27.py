# Print the Fibonacci sequence using recursion.

lower = int(input("Enter the lower value: "))
upper = int(input("Enter the upper value: "))

def fib(n):
    if n <= 1:
        return n
    else:
        return (fib(n-1) + fib(n-2))

for i in range(lower, upper):
    print(fib(i))