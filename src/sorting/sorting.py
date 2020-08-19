# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    arrC = []
    while(arrA and arrB):
        if(arrA[0] > arrB[0]): arrC.append(arrB.pop(0)) 
        else: arrC.append(arrA.pop(0))
    if(arrA): arrC += arrA
    else: arrC += arrB
    return arrC
    """
    elements = len(arrA) + len(arrB) #10
    merged_arr = [0] * elements #[0,0,0,0,0,0,0,0,0,0,0]
    """

# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    if (arr == [] or arr[-1] == arr[0]): return arr # if arr has no elements or 1 element return arr
    return merge(merge_sort(arr[::2]), merge_sort(arr[1::2])) # else take the ordered halves and compare them in merge



# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input
"""
def merge_in_place(arr, start, mid, end):
    # Your code here


def merge_sort_in_place(arr, l, r):
    # Your code here
"""
