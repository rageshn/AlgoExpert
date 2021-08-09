"""
 Write a function that takes in an array of integers and returns an array of length 2 representing the
 largest range of integers contained in that array.
 The first number in the output array should be the first number in the range, while the second number
 should be the last number in the range.
 A range of numbers is defined as a set of numbers that come right after each other in the set of real integers.
 For instance, the output array [2, 6] represents the range {2, 3, 4, 5, 6} which is a range of length 5.
 Note that numbers don't need to be sorted or adjacent in the input array in order to form a range.
 You can assume that there will only be one largest range.
"""


# Using Sorting and Temporary Space
# Time: O(n*log(n)) | Space: O(n)
###################################
# Sort the array in ascending order
# Initialize ranges and single_range as empty list
# Loop through every element in the array
#   If current element is not the last element
#       If the next element is same or one less than the current element
#           If the current element in not in single_range, append it to the list
#       else
#           Append the current element to single_range if its not already in.
#           Append single_range to ranges list, and initialize single_range to empty list
#   else
#       if the previous element is same or one less than the current element
#           If the current element not in single_range, append the element
#           Append single_range to ranges list
#       else
#           if there are values in single_range, append it to ranges list
#           else
#               if the current element is not available in single_range, append it
#               Append single_range to ranges list
##################################


def largestRange(array):
    array.sort()
    arr_length = len(array)
    ranges = []
    single_range = []
    for index, value in enumerate(array):
        if index != arr_length - 1:
            after = array[index + 1]
            if value + 1 == after or value == after:
                if value not in single_range:
                    single_range.append(value)
            else:
                if value not in single_range:
                    single_range.append(value)
                ranges.append(single_range)
                single_range = []
        else:
            before = array[index - 1]
            if before + 1 == value or before == value:
                if value not in single_range:
                    single_range.append(value)
                ranges.append(single_range)
            else:
                if single_range:
                    ranges.append(single_range)
                else:
                    if value not in single_range:
                        single_range.append(value)
                    ranges.append(single_range)

    max_range_index = -1
    max_range_len = -1
    for index, value in enumerate(ranges):
        if len(value) > max_range_len:
            max_range_index = index
            max_range_len = len(value)

    value = ranges[max_range_index]
    result = [value[0], value[len(value) - 1]]
    return result


# Using HashTable
# Time: O(n) | Space: O(n)
###########################
# Initialize a dictionary which denotes whether the item is visited or not (seen)
# Loop through the array and add all unique items and mark them as False (un visited)
# Initialize ranges as empty list
# Loop through the array
#   Get the range from getRange function
#   Append the range to the ranges list
#
# Loop through ranges list and get the range with max length -> range
# Assign result = [min(range), max(range)]
# return result
#
#
# Declare a function getRange(current_element, seen):
#   Initialize single_range as empty list
#   Assign current element to temp
#   -- Traverse to Left of current element
#   If the temp is available in seen and set to False,
#       Set the value in seen to True (visited)
#       Append temp to single_range
#       Decrement temp by 1
#   Loop till the condition fails
#
#   -- Traverse to right of current element
#   If the temp is available in seen and set to False,
#       Set the value in seen to True (visited)
#       Append temp to single_range
#       Decrement temp by 1
#   Loop till the condition fails
#   return single_range
###########################


def largestRange(array):
    seen = {}
    for index, value in enumerate(array):
        if value not in seen:
            seen[str(value)] = False

    ranges = []
    for index, value in enumerate(array):
        range_temp = getRange(value, seen)
        if range_temp:
            ranges.append(range_temp)

    max_range_index = -1
    max_range_len = -1
    for index, value in enumerate(ranges):
        if len(value) > max_range_len:
            max_range_index = index
            max_range_len = len(value)

    value = ranges[max_range_index]
    result = [min(value), max(value)]
    return result


def getRange(value, seen):
    single_range = []
    temp = value
    while True:
        # Traverse Left
        if (str(temp) in seen) and (not seen[str(temp)]):
            seen[str(temp)] = True
            single_range.append(temp)
            temp -= 1
        else:
            break

    temp = value + 1
    while True:
        # Traverse right
        if (str(temp) in seen) and (not seen[str(temp)]):
            seen[str(temp)] = True
            single_range.append(temp)
            temp += 1
        else:
            break

    return single_range

