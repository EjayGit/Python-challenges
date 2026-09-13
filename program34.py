# Positive array rotation.

arr = [1,2,3,4,5,6,7,8,9]
rot = int(input("Enter the rotational value: "))
newArr = []

# start counting from 'rot' in array to end and append to new array.
for element in range(rot+1, len(arr)+1):
    newArr.append(element)

# start counting from beginning of array for 'rot' and append to new array.
for element in range(1, rot+1):
    newArr.append(element)

print(newArr)