"""
 You're given an array of integers where each integer represents a jump of its value in the array.
 For instance, the integer 2 represents a jump of two indices forward in the array; the integer -3 represents a
 jump of three indices backward in the array.
 If a jump spills past the array's bounds, it wraps over to the other side. For instance, a jump of -1 at index 0
 brings us to the last index in the array. Similarly, a jump of 1 at the last index in the array brings us to
 index 0.
 Write a function that returns a boolean representing whether the jumps in the array form a single cycle.
 A single cycle occurs if, starting at any index in the array and following the jumps, every element in the array
 is visited exactly once before landing back on the starting index.
"""


# Using visited count approach
# Time: O(n) | Space: O(1)
###########################
# Initialize number of elements visited to 0
# Initialize current index to 0
# Loop till number of elements visited is less than array length
#   If number of elements visited > 0 and current index == 0 (Reaching the starting point again)
#       return False
#   Increment number of elements visited by 1
#   Get the next index to visit and assign it to current index --> get_next_index(current_index, array)
# return current index == 0
#
# Declare a function --> get_next_index(current_index, array)
#   Get the jump value -> array[current_index]
#   Set next index = (current_index + jump) % len(array)  -> Used if the element value is very high
#   If the next index is a positive integer
#       return next index
#   else if next index is a negative integer
#       set next index = next index + len(array) ->
#       return next index
###########################


def hasSingleCycle(array):
    num_element_visited = 0
    current_index = 0
    while num_element_visited < len(array):
        if num_element_visited > 0 and current_index == 0:
            return False
        num_element_visited += 1
        current_index = get_next_index(current_index, array)
    return current_index == 0


def get_next_index(current_index, array):
    jump = array[current_index]
    next_index = (current_index + jump) % len(array)
    if next_index >= 0:
        return next_index
    else:
        return next_index + len(array)
