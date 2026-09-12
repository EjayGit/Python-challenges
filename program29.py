# Calculate your body mass index.

weight = float(input("Enter your weight (kg): "))
height = float(input("Enter your height (m): "))

print(f'Your BMI is {round(weight/(height**2),2)}.')