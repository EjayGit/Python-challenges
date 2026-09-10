# Print all primes in a range of 10 numbers.

lower = int(input("Enter the lower bound: "))
upper = int(input("Enter the upper bound: "))

def isPrime(num):
    notPrime = False
    if num == 1:
        notPrime = True
    for i in range(2, num):
        if num % i == 0:
            notPrime = True
            break
    return notPrime

def findPrimes(lower, upper):
    primes = []
    # for each number within bounds, check to see if it is a prime number.
    for i in range(lower, upper):
        if not isPrime(i):
            primes.append(i)

    return primes

print(findPrimes(lower, upper))