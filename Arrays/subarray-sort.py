"""
  Write a function that takes in an array of at least two integers and that
  returns an array of the starting and ending indices of the smallest subarray
  in the input array that needs to be sorted in place in order for the entire
  input array to be sorted (in ascending order).

  If the input array is already sorted, the function should return [-1, -1]
"""

# Using additional array to store unsorted elements
# Time: O(n) | Space: O(n)
###########################
# Initialize unsorted as empty list
# If the array length is less than 3
#   if first element > second element
#       return [0, 1]
#   else return [-1, -1]
#
# For every element in the array
#   if index == 0:
#       set condition = current element < next element
#   else if index == last array index:
#       set condition = previous element < current element
#   else
#       set condition = previous element <= current element <= next element
#
#   if condition:
#       continue with the loop
#   else
#      Add current element to the unsorted list
#
# If unsorted list is empty, return [-1, -1]
# Get the minimum and maximum element from unsorted list
#
# Loop through the array
#   Get the actual index of the minimum and maximum unsorted element as start and end
#
# return [start, end]
#############################


def subarraySort(array):
    arr_length = len(array)
    unsorted = []

    if arr_length < 3:
        if array[0] > array[1]:
            return [0, 1]
        else:
            return [-1, -1]

    for index, value in enumerate(array):
        if index == 0:
            after = array[index + 1]
            condition = value <= after
        elif index == arr_length - 1:
            before = array[index - 1]
            condition = before <= value
        else:
            before = array[index - 1]
            after = array[index + 1]
            condition = before <= value <= after

        if condition:
            continue
        else:
            unsorted.append(value)

    if len(unsorted) < 1:
        return [-1, -1]
    min_un_sorted = min(unsorted)
    max_un_sorted = max(unsorted)

    i = 0
    j = arr_length - 1
    start = j
    end = i
    while j >= 0 and i <= arr_length - 1:
        if array[i] > min_un_sorted:
            start = min(start, i)
        if array[j] < max_un_sorted:
            end = max(end, j)
        i += 1
        j -= 1

    return [start, end]


# Using constant space
# Time: O(n) | Space: O(1)
###########################
# Declare a function -> isOutOfOrder(index, current element, array)
#   if index = 0, return current_element > array[index + 1]
#   if index = last index, return current_element < array[index - 1]
#   return current_element > array[index + 1] or current_element < array[index - 1]
#
# Initialize minOutOfOrder as positive infinity
# Initialize maxOutOfOrder as Negative infinity
# Loop through the array
#   Set current_element = array[index]
#   if isOutOfOrder(index, current_element, array):
#       minOutOfOrder = min(minOutOfOrder, current_element)
#       maxOutOfOrder = max(maxOutOfOrder, current_element)
#
# if minOutOfOrder equals positive infinity
#   return [-1, -1]
#
# Set left_index = 0
# while minOutOfOrder >= array[left_index], increment left_index by 1
# Set right_index = len(array) - 1
# while maxOutOfOrder <= array[right_index], decrement right_index by 1
#
# return [left_index, right_index]
###########################


def subarraySort(array):
    minOutOfOrder = float("inf")
    maxOutOfOrder = float("-inf")
    for i in range(len(array)):
        current_element = array[i]
        if isOutOfOrder(i, current_element, array):
            minOutOfOrder = min(minOutOfOrder, current_element)
            maxOutOfOrder = max(maxOutOfOrder, current_element)

    if minOutOfOrder == float("inf"):
        return [-1, -1]

    left_index = 0
    while minOutOfOrder >= array[left_index]:
        left_index += 1

    right_index = len(array) - 1
    while maxOutOfOrder <= array[right_index]:
        right_index -= 1

    return [left_index, right_index]


def isOutOfOrder(i, current_element, array):
    if i == 0:
        return current_element > array[i + 1]
    if i == len(array) - 1:
        return current_element < array[i - 1]
    return current_element > array[i + 1] or current_element < array[i - 1]
