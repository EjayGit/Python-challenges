# Calculate the Armstrong number

num = int(input("Enter the number: "))

# Calculate how many digits there are
strDigits = str(num)
digits = len(strDigits)
sum = 0

# For each digit
for i in strDigits:
    # sum its value to the power of the number of digits.
    sum = sum + int(i)**digits

if sum == num:
    print(f'{num} is an Armstrong number!')
else:
    print(f'{num} is not an Armstrong number...')