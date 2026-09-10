# Swap two variables
var1 = float(input("Enter the first variable: "))
var2 = float(input("Enter the second variable: "))
print(f'The first variable is {var1}, and the second variable is {var2}.')
temp = var1
var1 = var2
var2 = temp
print(f'The first variable is {var1}, and the second variable is {var2}.')