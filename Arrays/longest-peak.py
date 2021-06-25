"""
Write a function that takes in an array of integers and returns the length of the longest peak in the array.
A peak is defined as adjacent integers in the array that are strictly increasing until they reach a tip
(the highest value in the peak), at which point they become strictly decreasing. At least three integers are required to
form a peak.
For example, the integers 1, 4, 10, 2 form a peak, but the integers 4, 0, 10 don't and neither do the integers 1, 2, 2, 0.
Similarly, the integers 1, 2, 3 don't form a peak because there aren't any strictly decreasing integers after the 3.
"""

# Iterative approach
# Time: O(n) | Space: O(1)
#############################
# Initialise longest peak length to 0
# Set index to 1
# Loop through elements in the array
#    If array[index - 1] < array[index] and array[index + 1] > array[index]
#        set is_peak as True
#    else
#        set is_peak to False
#    If is_peak is False, continue with the loop
#    Set left index as index - 2
#    Loop till left index >= 0 and array[left index] < array[left index + 1]:
#       decrement left index by 1
#    Set right index as index + 2
#    Loop till right index < len(array) and array[right index] < array[right index - 1]
#       increment right index by 1
#    Set the current peak length as right index - left index - 1
#    Set longest peak length as max between longest peak length and current peak length
#    Set index as right index
# return longest peak length
#############################


def longestPeak(array):
    # Write your code here.
    longest_peak_length = 0
    index = 1
    while index < len(array) - 1:
        is_peak = array[index - 1] < array[index] and array[index] > array[index + 1]
        if not is_peak:
            index += 1
            continue

        left_index = index - 2
        while left_index >= 0 and array[left_index] < array[left_index + 1]:
            left_index -= 1
        right_index = index + 2
        while right_index < len(array) and array[right_index] < array[right_index - 1]:
            right_index += 1

        current_peak_length = right_index - left_index - 1
        longest_peak_length = max(longest_peak_length, current_peak_length)
        index = right_index
    return longest_peak_length

