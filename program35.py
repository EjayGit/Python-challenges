# Split arr and add first part to end.

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
split = int(input("Enter the split position: "))

firstPart = arr[:split]
secondPart = arr[split:]
newArr = secondPart + firstPart
print(newArr)