"""
 The pre-order traversal of a Binary Tree is a traversal technique that starts at the tree's root node
 and visits nodes in the following order:
 1. Current Node
 2. Left subtree
 3. Right subtree
 Given a non-empty array of integers representing the pre-order traversal of a Binary Search Tree (BST),
 write a function that creates the relevant BST and returns its root node.
 The input array will contain the values of BST nodes in the order in which these nodes would be visited
 with a pre-order traversal.
 Each BST node has an integer value, a left child not and a right child node. A node is said to be a valid BST node
 if and only if it satisfies the BST property: its value is strictly greater than the values of every node to its left;
 its value is less than or equal to the values of every node to its right; and its children node are either valid BST
 nodes themselves or None/NULL.
"""


# Brute force approach
# Time: O(n^2) | Space: O(n)
############################
# If the array doesnt have any elements
#   return None
#
# Set current_value to element at 0 index
# Set right subtree root index = array length
#
# Loop through the array from first index to end
#   Set value = Element at current index
#   If value >= current_value
#       Set right subtree root index = current index
#       break
#
# Set left sub tree = call reConstructBST with array from 1 till right sub tree root index
# Set right sub tree = call reConstructBST with array from right subtree root index till end
# return the BST node with current_value, left subtree, right sub tree
############################


class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.right = right
        self.left = left


def reConstructBST(preOrderTraversalValues):
    if len(preOrderTraversalValues) == 0:
        return None

    current_value = preOrderTraversalValues[0]
    right_subtree_root_index = len(preOrderTraversalValues)

    for index in range(1, len(preOrderTraversalValues)):
        value = preOrderTraversalValues[index]
        if value >= current_value:
            right_subtree_root_index = index
            break

    left_sub_tree = reConstructBST(preOrderTraversalValues[1:right_subtree_root_index])
    right_sub_tree = reConstructBST(preOrderTraversalValues[right_subtree_root_index:])
    return BST(current_value, left_sub_tree, right_sub_tree)


# With range values
# Time: O(n) | Space: O(h)
############################
# Declare a class TreeInfo
#   Assign self.root_index to root_index
#
# Create tree_info object with 0 as root_index
# call reConstructFromRange with -infinity, +infinity, array, tree info object
#
# Declare a function --> reConstructFromRange(lower_bound, upper_bound, array, tree_info)
#   If tree_info.root_index == length of array
#       return None
#   Set root_value = element in array at tree_info.root_index
#   If the root_value is not with in lower and upper bound values
#       return None
#   Increment tree_info.root_index by 1
#   Set left_sub_tree = recursively call reConstructFromRange with lower_bound, root_value, array and tree_info object
#   Set right_sub_tree = recursively call reConstructFromRange with root_value, upper_bound, array, tree_info object
#   return BST node object with root_value, left_sub_tree and right_sub_tree
############################


class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.right = right
        self.left = left


class TreeInfo:
    def __init__(self, root_index):
        self.root_index = root_index


def reConstructBST(preOrderTraversalValues):
    tree_info = TreeInfo(0)
    return reConstructFromRange(float("-inf"), float("inf"), preOrderTraversalValues, tree_info)


def reConstructFromRange(minimum, maximum, array, sub_tree_info):
    if sub_tree_info.root_index == len(array):
        return None

    root_value = array[sub_tree_info.root_index]
    if root_value < minimum or root_value >= maximum:
        return None

    sub_tree_info.root_index += 1
    left_sub_tree = reConstructFromRange(minimum, root_value, array, sub_tree_info)
    right_sub_tree = reConstructFromRange(root_value, maximum, array, sub_tree_info)
    return BST(root_value, left_sub_tree, right_sub_tree)
