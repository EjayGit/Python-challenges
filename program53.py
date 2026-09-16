# Find N largest elements from a list.

myList = numbers = [30, 10, 45, 5, 20, 50, 15, 3, 345, 54, 67, 87, 98, 100, 34]

n = int(input("Enter the number: "))

myList.sort()
for i in range(0, n):
    print(myList[-(i+1)])