# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    length = len(arr) -1 
    while length > 0:
        largest = arr[0]
        largest_index = 0
        for i in range(0, length):
            if arr[i] > largest:
                largest = arr[i] 
                largest_index = i
            if i == length:
                arr[largest_index] = arr[i]
                arr[i] = largest
        # cur_index = i
        # smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        # Your code here


        # TO-DO: swap
        # Your code here

    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    # Your code here


    return arr


# STRETCH: implement the Count Sort function below
def count_sort(arr, maximum=-1):
    # Your code here


    return arr
