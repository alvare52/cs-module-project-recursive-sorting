# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, start, end):
    # Your code here
    first = 0
    last = (len(arr) - 1)

    found = False
    found_index = -1

    # if first <= last and not found:
    #     return 
    while first <= last and not found:
        middle = (first + last) // 2

        if arr[middle] == target:
            found_index = middle
            found = True
            print("Found")
            return found_index

        else: 
            if target < arr[middle]:
                last = middle - 1
            else:
                first = middle + 1
    # return found_index
    print("NOT Found")
    return -1


# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find 
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively 
# or iteratively
def agnostic_binary_search(arr, target):
    # Your code here
    pass

my_list = [1, 2, 3, 4, 5]
print(binary_search(my_list, 2, 0, len(my_list) - 1))