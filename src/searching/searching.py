def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
        else:
            i == len(arr) - 1

    return -1  # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        middle = (left + right) // 2
        temp_match = arr[middle]

        if target == temp_match:
            return middle
        elif target < temp_match:
            right = middle - 1
        else:
            left = middle + 1

    return -1  # not found

#                 ------Notes-------
# The array must be sorted for the binary search to work
# divides array in half and compares it to the target
#  if the target is less than the middle
#    set the right pointer to the index - 1 from the middle
#  if target is greater than the middle
#    set the left pointer to the index + 1 from the middle
# reset middle pointer
# middle = (left + right) // 2 <--floored
