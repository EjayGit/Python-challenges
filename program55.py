# Print odd numbers in a List

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def isOdd(number):
    if number % 2 != 0:
        return True

for number in numbers:
    if isOdd(number):
        print(f'The number {number} is odd.')