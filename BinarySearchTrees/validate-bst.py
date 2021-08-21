"""
 Write a function that takes in a potentially invalid Binary Search Tree (BST) and a returns a boolean representing
 whether the BST is valid.
 You can assume that there will only be one closest value.
 Each BST node has an integer value, a left child not and a right child node. A node is said to be a valid BST node
 if and only if it satisfies the BST property: its value is strictly greater than the values of every node to its left;
 its value is less than or equal to the values of every node to its right; and its children node are either valid BST
 nodes themselves or None/NULL.
"""


# Recursive method
# Time : O(n) | Space : O(d) d-> depth of tree
##############################
# Idea is to check whether the current node value is between minimum and maximum values based on position.
# A node in right subtree must be strictly greater than its immediate parent node and strictly less than the root node
# A node in left subtree must be strictly less than its parent node and strictly greater than its left child
#
# Initialize minimum valve to - infinity and maximum to + infinity
# call validateNode with tree, minimum and maximum as parameters  -> validateNode(node, minimum, maximum)
#
# Declare a function --> validateNode(node, minimum, maximum)
#   If the current node is null
#       return True
#   If the node's value doesn't falls between minimum and maximum value
#       return False
#   validate the left subtree by calling validateNode(node.left, minimum, node.value as maximum)
#   validate the right subtree by calling validateNode(node.right, node.value, maximum)
#   return validateLeft and validateRight
##############################


# This is an input class. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def validateBst(tree):
    min_value = float("-inf")
    max_value = float("inf")
    return validateNode(tree, min_value, max_value)


def validateNode(node, minimum, maximum):
    if node:
        if minimum <= node.value < maximum:
            validateLeft = validateNode(node.left, minimum, node.value)
            return validateLeft and validateNode(node.right, node.value, maximum)
        else:
            return False
    else:
        return True


def validateBstHelper(tree, minValue, maxValue):
    if tree is None:
        return True
    if tree.value < minValue or tree.value >= maxValue:
        return False
    validateLeft = validateBstHelper(tree.left, minValue, tree.value)
    return validateLeft and validateBstHelper(tree.right, tree.value, maxValue)
