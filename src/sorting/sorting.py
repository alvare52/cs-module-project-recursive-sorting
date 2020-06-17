# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    # 
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements

    # Your code here


    return merged_arr

# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    # Your code here

    # check if empty or if only one thing in array
    if len(arr) == 0 or len(arr) == 1:
        print("empty or 1 item array")
        return arr

    # check if only 2 things in array
    if len(arr) == 2:
        if arr[0] < arr[1]:
            print("left side was smaller (2 items)")
            return arr
        else:
            temp = arr[1]
            arr[1] = arr[0]
            arr[0] = temp
            print("right side was smaller, or identical (2 items)")
            return arr

    # 3, 6, 8, 2, 5, 4, 1
    # [3, 6, 8] [2] [5, 4, 1]
    # middle
    middle = len(arr) // 2 
    # left 
    left = arr[:middle]
    right = arr[middle:]
    # right

    return arr

my_list = []
print(merge_sort(my_list))

# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input
def merge_in_place(arr, start, mid, end):
    # Your code here
    pass


def merge_sort_in_place(arr, l, r):
    # Your code here
    pass

