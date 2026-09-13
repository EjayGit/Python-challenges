# Find the cubed sum of the first n natural numbers.

num = int(input("Enter the limiting natural number: "))
sum = 0

for i in range(1, num+1):
    sum = sum + i**3

print(f'The cube sum of natural numbers up to {num} is: {sum}.')