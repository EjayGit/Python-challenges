# Calculate and print the value according to the given formula:
# 𝑄 = sqrt(2𝐶𝐷/H)
# Where
C = 50
# And 
H = 30
# inputs should be comma separated i.e. input = "100,150,180"
nums = "100,150,180"
# nums = str(input("Enter the input: "))

numList = nums.split(',')

results = []
for num in numList:
    results.append(((2*C*int(num))/(H))**0.5)

print(','.join(map(str,results)))