# Solve a quadratic eqn
import math

a = float(input('Enter the coefficient a: '))
b = float(input('Enter the coefficient b: '))
c = float(input('Enter the coefficient c: '))
while a == 0:
    a = float(input('"a" cannot be zero. Enter the coefficient a: '))
det = b**2 - 4*a*c
if det > 0:
    print(f'The second root is: {(-b + math.sqrt(det))/(2*a)}')
    print(f'The first root is: {(-b - math.sqrt(det))/(2*a)}')
elif det == 0:
    root = (-b + math.sqrt(det))/(2*a)
else:
    real = -b / (2*a)
    img = math.sqrt(abs(det)) / (2*a)
    print(f'The first root is: {real} + {img}i')
    print(f'The second root is: {real} - {img}i')