"""
Write a function that takes in an array of integers and returns a boolean representing whether the array is monotonic.
An array is said to be monotonic, if its elements from left to right, are entirely non-increasing or entirely non-decreasing.
Empty arrays and arrays of one element are monotonic.
"""


# Naive approach (Looping twice)
# Time: O(n) | Space: O(1)
#############################
# Initialize two pointers each for increasing and decreasing flow.
# If array length is 0 or 1, return True
# Loop the array with incremental pointers till the end
#     If the prev element at 'i' is lesser than the one at 'j'
#         If the end is reached, return True
#         else, increment pointers
#
# Loop the array using decremental pointers till the end
#     If the prev element at 'i' is greater than the one at 'j'
#         If the end is reached, return True
#         else, increment pointers
#
# return False
#############################


def isMonotonic(array):
    incr_i = 0
    incr_j = incr_i + 1
    decr_i = 0
    decr_j = decr_i + 1
    array_len = len(array)

    if array_len == 0 or array_len == 1:
        return True

    while incr_j <= (array_len - 1) and array[incr_i] <= array[incr_j]:
        if incr_j == (array_len - 1):
            return True
        else:
            incr_i += 1
            incr_j += 1

    while decr_j <= (array_len - 1) and array[decr_i] >= array[decr_j]:
        if decr_j == (array_len - 1):
            return True
        else:
            decr_i += 1
            decr_j += 1

    return False


# Using direction logic
# Time: O(n) | Space: O(1)
###########################
# If the array length is less than 2, return True
# Initialize variable direction as difference between element at first index and 0th index.
# This direction variable will be used to check whether the array is increasing or decreasing.
# Loop through the array till the end, with variable i
#     If direction is 0 (Both elements are equal)
#         Update direction to difference between elements at array[i] and array[i-1]
#         continue
#     If the direction breaks
#         return False
# return True
#
# Break Direction:
# Get the difference between current element and previous element
# If the current direction > 0 (i.e., elements are increasing)
#     return difference < 0 (would be false for increasing array)
# else, return difference > 0
###########################


def isMonotonic(array):
    if len(array) <= 2:
        return True

    direction = array[1] - array[0]
    for i in range(2, len(array)):
        if direction == 0:
            direction = array[i] - array[i - 1]
            continue
        if breaksDirection(direction, array[i - 1], array[i]):
            return False

    return True


def breaksDirection(direction, previousInt, currentInt):
    difference = currentInt - previousInt
    if direction > 0:
        return difference < 0
    return difference > 0
