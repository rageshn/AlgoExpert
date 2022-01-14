"""
 Write a function that takes in an array of unique integers and returns its powerset.
 The powerset P(X) of a set 'X' is the set of all subsets of 'X'. For example, the powerset of [1, 2] is
 [[], [1], [2], [1,2]].
 Note that the sets in the powerset do not need to be in any particular order.
"""


# Recursive approach
# Time: O(n * 2^n) | Space: O(n * 2^n)
######################################
# This approach is based on a choice of whether we include the current value to the subset or
# not include it to the current subset.
# Both choice will generate a new subset, and it can be added to the list.
#
#                                   [1, 2, 3]
#                              1 /             \ []
#                             [1]               []
#                         2 /    \ []       2 /    \ []
#                     [1, 2]      [1]      [2]      []
#                  3 /      \[]  3/ \[]  []/  \3  []/ \ 3
#             [1,2,3]    [1, 2] [1] [1,3] [2][2,3] [] [3]
#
#
# Initialize subsets = []
# Call generate_subsets by passing 0, array, empty list for current subset & subsets list --> generate_powersets(0, array, [], subsets)
# return subsets
#
# Declare a function --> generate_powersets(index, array, current_subset, subsets)
#   Append the copy of current_subset to subsets list (This is to avoid mutating the original subset)
#   Loop the array from index till the end --> i
#       Append the element at 'i' to current_subset (array[i])
#       Recursively call generate_subset(i + 1, array, current_subset, subsets)
#       Remove the element (array[i]) from current_subset
######################################


def powerset(array):
    subsets = []
    generate_powersets(0, array, [], subsets)
    return subsets


def generate_powersets(index, array, current_subset, subsets):
    subsets.append(current_subset[:])
    for i in range(index, len(array)):
        current_subset.append(array[i])
        generate_powersets(i + 1, array, current_subset, subsets)
        current_subset.remove(array[i])


# Iterative approach
# Time: O(n * 2^n) | Space: O(n * 2^n)
######################################
# Initialize subsets = empty list which holds a empty list
# Loop through every element in array
#   Loop through the index of subsets till the end
#       Set current_subset = subsets[i]
#       Append current_subset + [element] to subsets list
# return subsets
######################################


def powerset(array):
    subsets = [[]]
    for element in array:
        for i in range(len(subsets)):
            current_subset = subsets[i]
            subsets.append(current_subset + [element])
    return subsets
