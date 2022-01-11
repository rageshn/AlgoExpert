"""
 Write a function that takes in an array of unique integers and returns an array of all permutations of those integers
 in no particular order.
 If the input array is empty, the function should return an empty array.
"""


# Creating new array for every permutation
# Time: O(n^2 * n!) | Space: O(n * n!)
######################################
# This approach removes the current number from the array and creates new array to hold every combination.
# Initialize permutations = empty list
# Call permutations_helper by passing array, empty list and permutations list --> permutations_helper(array, [], permutations)
# return permutations
#
# Declare a function --> permutations_helper(array, current_permutation, permutations)
#   If the array is empty and there are elements in current_permutation list
#       Append current_permutation to permutations list
#   else
#       Loop through the elements in the array
#           Assign new_array = All elements in 'array' except for the current element
#           Assign new_permutation = Append current element to current_permutation list
#           Recursively call permutations_helper(new_array, new_permutation, permutations)
######################################


def getPermutations(array):
    permutations = []
    permutations_helper(array, [], permutations)
    return permutations


def permutations_helper(array, current_permutation, permutations):
    if not array and current_permutation:
        permutations.append(current_permutation)
    else:
        for i in range(len(array)):
            new_array = array[:i] + array[i + 1:]  # O(n)
            new_permutation = current_permutation + [array[i]]  # O(n)
            permutations_helper(new_array, new_permutation, permutations)


# Swapping the values
# Time: O(n * n!) | Space: O(n * n!)
####################################
# In this approach we iterate through each element in the array, swap the current element and next element.
#
# Initialize permutations = empty list
# Call permutations_helper by passing 0, array and permutations list --> permutations_helper(0, array, permutations)
# return permutations
#
# Declare a function --> permutations_helper(i, array, permutations)
#   If i == last index of array
#       Append the current array snapshot to permutations list
#   else
#       Loop through every element in array from i till the end --> j
#           swap the values at i & j --> swap(array, i, j)
#           Recursively call permutations_helper(i + 1, array, permutations)
#           swap the values at i & j --> re-swap the values back
#
# Declare a function --> swap(array, i, j)
#   Set the values at i with j and j with i
####################################


def getPermutations(array):
    permutations = []
    permutations_helper(0, array, permutations)
    return permutations


def permutations_helper(i, array, permutations):
    if i == len(array) - 1:
        permutations.append(array[:])
    else:
        for j in range(i, len(array)):
            swap(array, i, j)
            permutations_helper(i + 1, array, permutations)
            swap(array, i, j)


def swap(array, i, j):
    array[i], array[j] = array[j], array[i]
