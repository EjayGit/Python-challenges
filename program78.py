# accept a sentence and calculate the number of letters and digits.

sentence = str(input("Enter the sentence: "))

letters = 0
digits = 0

for char in sentence:
    if char.isdigit():
        digits += 1
    elif char.isalpha():
        letters += 1

print(f'Letters: {letters}\nDigits: {digits}')