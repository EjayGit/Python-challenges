# Define a class with a generator which can iterate the numbers, which are divisible by 7, between a given range 0 and n.

class DivisibleBySeven:
    def __init__(self, n):
        self.n = n
    
    def testDivisible(self):
        for num in range(0, self.n+1):
            if num % 7 == 0:
                yield num

n = int(input("Enter the integer: "))

for num in DivisibleBySeven(n).testDivisible():
    print(num)