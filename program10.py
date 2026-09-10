# swap vars without temp var

a = 1
b = 3
b, a = a, b
print(f'a:{a}, b:{b}')