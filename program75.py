# Takes 2 digits, X,Y as input and generates a 2-dimensional
# array. The element value in the i-th row and j-th column 
# of the array should be i*j.

# Get input
digits = str(input("Enter the input dimensions [X, Y]: "))

# split input into list
digitList = digits.split(',')

# Create an array of zeros (digitList[0] x digitList[1])
Arr = [[0 for _ in range(int(digitList[1]))] for _ in range(int(digitList[0]))]

# Cycle through all positions and input result of i*j.
for i in range(0, int(digitList[0])):
    for j in range(0, int(digitList[1])):
        Arr[i][j] = i*j

# print result
print(Arr)