# Write a program to check the validity of password input by users using regex. Following are the criteria for checking the password:
# 1. At least 1 letter between [a-z]
# 2. At least 1 number between [0-9]
# 3. At least 1 letter between [A-Z]
# 4. At least 1 character from [$#@]
# 5. Minimum length of transaction password: 6
# 6. Maximum length of transaction password: 12
# Your program should accept a sequence of comma separated passwords and will check them according to the above criteria. Passwords that match the criteria are to be printed, each separated by a comma.

import re

pattern = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[$#@]).{6,12}$"