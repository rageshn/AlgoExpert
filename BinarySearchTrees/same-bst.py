"""
 An array of integers is said to represent the Binary Search Tree (BST) obtained by inserting each integer in the array,
 from left to right, into the BST.
 Write a function that takes in two arrays of integers and determines whether these arrays represent the same BST.
 Note that you're not allowed to construct any BSTs in your code.
 Each BST node has an integer value, a left child not and a right child node. A node is said to be a valid BST node
 if and only if it satisfies the BST property: its value is strictly greater than the values of every node to its left;
 its value is less than or equal to the values of every node to its right; and its children node are either valid BST
 nodes themselves or None/NULL.
"""

# Using additional arrays
# Time: O(n^2) | Space: O(n^2)
###############################
# If both arrays has no elements
#   return True
# If both arrays has unequal lengths
#   return False
# If both array's first element are not equal
#   return False
#
# All element smaller than root, will be in left subtree
# All elements greater than or equal to root will be in right subtree
# Set left subtree of first array = call getSmaller(first array) --> getSmaller()
# Set left subtree of second array = call getSmaller(second array) --> getSmaller()
# Set right subtree of first array = call getBiggerOrEqual(first array) --> getBiggerOrEqual()
# Set right subtree of second array = call getBiggerOrEqual(second array) --> getBiggerOrEqual()
# recursively call sameBsts function for both left subtrees and right subtrees and return the result
#
# Declare a function --> getSmaller(array)
#   Set smaller = empty array
#   Loop through the array from 1st index till end
#       If the current element < root (element at 0th index)
#           Append current element to smaller
#   return smaller
#
# Declare a function --> getBiggerOrEqual(array)
#   Set bigger = empty array
#   Loop through the array from 1st index till end
#       If the current element >= root (element at 0th index)
#           Append current element to bigger
#   return bigger
###############################


def sameBsts(arrayOne, arrayTwo):
    if len(arrayOne) == 0 and len(arrayTwo) == 0:
        return True
    if len(arrayOne) != len(arrayTwo):
        return False
    if arrayOne[0] != arrayTwo[0]:
        return False

    left_subtree_one = getSmaller(arrayOne)
    left_subtree_two = getSmaller(arrayTwo)
    right_subtree_one = getBiggerOrEqual(arrayOne)
    right_subtree_two = getBiggerOrEqual(arrayTwo)

    return sameBsts(left_subtree_one, left_subtree_two) and sameBsts(right_subtree_one, right_subtree_two)


def getSmaller(array):
    smaller = []
    for i in range(1, len(array)):
        if array[i] < array[0]:
            smaller.append(array[i])
    return smaller


def getBiggerOrEqual(array):
    bigger = []
    for i in range(1, len(array)):
        if array[i] >= array[0]:
            bigger.append(array[i])
    return bigger


# Not using extra spaces
# Time: O(n^2) | Space: O(d)
#############################
# Declare a function --> validate_bst(array_one, array_two, root_index_one, root_index_two, minimum, maximum)
#   If any of the root_indices (root_index_one or root_index_two) equals -1
#       return root_index_one == root_index_two
#
#   If the elements at root_index are not equal in both arrays
#       return False
#
#   Get the left subtree root index from first & second array
#   Get the right subtree root index from first & second array
#   Set left_root_index_one = call get_index_of_first_smaller() with first array, root_index_one and minimum value
#   Set left_root_index_two = call get_index_of_first_smaller() with second array, root_index_two and minimum value
#   Set right_root_index_one = call get_index_of_first_bigger_or_equal() with first array, root_index_one and maximum value
#   Set right_root_index_two = call get_index_of_first_bigger_or_equal() with second array, root_index_two and maximum value
#
#   Set current_value = Element at the root_index_one in array_one
#   Set are_left_same = recursively call validate_bst(array_one, array_two, left_root_index_one, left_root_index_two, minimum, current_value)
#   Set are_right_same = recursively call validate_bst(array_one, array_two, right_root_index_one, right_root_index_two, current_value, maximum)
#   return are_left_same and are_right_same
#
# Declare a function --> get_index_of_first_smaller(array, starting_index, min_value)
#   -- This method returns the index of the next smaller value (smaller than root node - 0th index) in the array
#   Loop through the array from starting_index + 1 till end of the array
#       If the current element < element at starting_index (root) and its greater than min_value
#           return current index
#   return -1
#
# Declare a function --> get_index_of_first_bigger_or_equal(array, starting_index, max_value)
#   -- This method returns the index of the next bigger value (greater than or equal to root node - 0th index) in the array
#   Loop through the array from starting_index + 1 till end of the array
#       If the current element >= element at starting_index (root) and its less than maximum value
#           return current index
#   return -1
#############################


def sameBsts(arrayOne, arrayTwo):
    return validate_bst(arrayOne, arrayTwo, 0, 0, float("-inf"), float("inf"))


def validate_bst(array_one, array_two, root_index_one, root_index_two, minimum, maximum):
    if root_index_one == -1 or root_index_two == -1:
        return root_index_one == root_index_two

    if array_one[root_index_one] != array_two[root_index_two]:
        return False

    left_root_index_one = get_index_of_first_smaller(array_one, root_index_one, minimum)
    left_root_index_two = get_index_of_first_smaller(array_two, root_index_two, minimum)
    right_root_index_one = get_index_of_first_bigger_or_equal(array_one, root_index_one, maximum)
    right_root_index_two = get_index_of_first_bigger_or_equal(array_two, root_index_two, maximum)

    current_value = array_one[root_index_one]
    are_left_same = validate_bst(array_one, array_two, left_root_index_one, left_root_index_two, minimum, current_value)
    are_right_same = validate_bst(array_one, array_two, right_root_index_one, right_root_index_two, current_value, maximum)
    return are_left_same and are_right_same


def get_index_of_first_smaller(array, starting_index, min_value):
    for i in range(starting_index + 1, len(array)):
        if array[i] < array[starting_index] and array[i] >= min_value:
            return i
    return -1


def get_index_of_first_bigger_or_equal(array, starting_index, max_value):
    for i in range(starting_index + 1, len(array)):
        if array[i] >= array[starting_index] and array[i] < max_value:
            return i
    return -1
