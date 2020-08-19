# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, start, end):
    if (start <= end): 
        mid = round(start + (( end-start)/2))                   #get halfway point
        if (arr[mid] == target): return mid                     #if halfway is target return index
        elif(target < arr[mid]):
            return binary_search(arr, target, start, mid - 1)   #if target is less than mid, mid is now the new end 
        else: return binary_search(arr, target, mid + 1, end)   #if target is greater than mid, mid is not the new start 
    else: return -1

# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find 
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively 
# or iteratively
"""
def agnostic_binary_search(arr, target):
    # Your code here

"""
