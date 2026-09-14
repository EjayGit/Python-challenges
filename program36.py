# Check if an array is Monotonic

arr1 = [1, 2, 2, 3] # Monotonic (non-decreasing)
arr2 = [3, 2, 1] # Monotonic (non-increasing)
arr3 = [1, 3, 2, 4] # Not monotonic

def isMonotonic(arr):
    increasing = decreasing = True
    for i in range(1, len(arr)):
        if arr[i] < arr[i-1]:
            increasing = False
        elif arr[i] > arr[i-1]:
            decreasing = False
    
    return increasing or decreasing

print(f'Array 1 is monotonic: {isMonotonic(arr1)}')
print(f'Array 2 is monotonic: {isMonotonic(arr2)}')
print(f'Array 3 is monotonic: {isMonotonic(arr3)}')