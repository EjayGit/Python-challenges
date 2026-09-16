# print even numbers from a list.

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def isEven(number):
    if number%2 == 0:
        return True

for number in numbers:
    if isEven(number):
        print(f'The number {number} is even.')