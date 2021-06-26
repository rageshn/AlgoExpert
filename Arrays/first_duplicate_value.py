"""
 Given an array of integers between 1 and n, inclusive, where n is the length of the array, write a function that
 returns the first integer that appears more than once (when the array is read from left to right).
 In other words, out of all integers that might occur more than once in the input array, your function should return the
 one whose first duplicate value has the minimum index.
 If no integer appears more than once, your function should return -1.
 Note that, you're allowed to mutate the input array.
"""


# Bruteforce approach
# Time: O(n^2) | Space: O(1)
##############################
# Initialize min_second_index = array length
# Loop through the elements in the array with index i
#   Loop through the elements in the array with index j starting from i + 1
#       if array[i] == array[j]
#           min_second_index = min(min_second_index, j)
# if min_second_index == len(array)
#   return -1
# return array[min_second_index]
##############################


def firstDuplicateValue(array):
    min_second_index = len(array)
    for i in range(len(array)):
        for j in range(i+1, len(array)):
            if array[i] == array[j]:
                min_second_index = min(min_second_index, j)

    if min_second_index == len(array):
        return -1

    return array[min_second_index]


# Using external array
# Time: O(n) | Space: O(n)
############################
# Initialize seen as empty array
# Loop through the elements in array
#   If element not in seen
#       Add element to seen
#   else
#       return element
# return -1
#############################


def firstDuplicateValue(array):
    seen = []
    for val in array:
        if val not in seen:
            seen.append(val)
        else:
            return val
    return -1


# Using absolute value
# Time: O(n) | Space: O(1)
############################
# Loop through the elements in the array
#   Set abs_value to abs(element)
#   if array[abs_value -1] is less than 0
#       return abs_value
#   array[abs_value - 1] = array[abs_value - 1] * -1
# return -1
#############################


def firstDuplicateValue(array):
    for value in array:
        abs_value = abs(value)
        if array[abs_value - 1] < 0:
            return abs_value
        array[abs_value - 1] *= -1
    return -1

