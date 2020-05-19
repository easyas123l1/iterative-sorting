def linear_search(arr, target):
    # Your code here
    for i in range(len(arr)):
        if arr[i] == target:
            return i

    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):
    high = len(arr)-1
    low = 0
    while True: 
        middle = (high + low) // 2
        if arr[middle] == target:
            return middle
        if high==low: 
            return -1
        if arr[middle] > target:
            low = middle 
        else:
            high = middle 
    return -1


