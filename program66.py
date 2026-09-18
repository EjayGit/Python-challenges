# Check if a string contains any special character using regex.

import re

string = str(input("Enter the string: "))
pattern = r'[!@#$%^&*()_+{}\[\]:;<>,.?~\\\/\'"\-=]'

def containsPattern(pattern, string):
    if re.search(pattern, string):
        return True
    else:
        return False

print(f'The string contains one or more symbols: {containsPattern(pattern, string)}.')