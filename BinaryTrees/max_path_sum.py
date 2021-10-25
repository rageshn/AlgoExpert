"""
 Write a function that takes in a Binary Tree and returns its max path sum.
 A path is a collection of connected nodes in a tree, where no node is connected to more than two other nodes;
 a path sum is the sum of the values of the nodes in a particular path.
 Each Binary Tree node has an integer value, a left child node and a right child node. Children nodes can either be
 Binary Tree node themselves or NULL/None.
"""

# Method 1
# Time: O(n) | Space: O(log(n))
###############################
# This method will work only if all the nodes in the tree is >= 1
# If the tree is null
#   return 0
#
# Call the function max_path_sum by passing tree nodes, this returns the max path
# return the max path
#
# Declare a function --> max_path_sum(node, tree)
#   If the current node is null
#       return 0
#   If the node has either left or right subtree (not a leaf)
#       max_path_left = recursively call max_path_sum on left subtree and pass root node as second parameter
#       max_path_right = recursively call max_path_sum on right subtree and pass root node as second parameter
#       If current node is root and max_path_left > 0 and max_path_right > 0
#           set max_path = max_path_left + max_path_right + current node value
#       else
#           set max_path = max(max_path_left, max_path_right) + current node value
#       return max_path
###############################


def maxPathSum(tree):
    # Write your code here.
    if not tree:
        return 0

    max_path = max_path_sum(tree, tree)
    return max_path


def max_path_sum(node, tree):
    if not node:
        return 0

    if node.left or node.right:
        max_path_left = max_path_sum(node.left, tree)
        max_path_right = max_path_sum(node.right, tree)

        if node == tree and (max_path_left > 0 and max_path_right > 0):
            max_path = max_path_left + max_path_right + node.value
        else:
            max_path = max(max_path_left, max_path_right) + node.value
        return max_path

    return node.value


# Method 2
# Time: O(n) | Space: O(log(n))
###############################
# This method works even when the tree has nodes with negative values
#
# Initialize a function --> get_max_path_sum(node)
#   If the node is null
#       return 0, float("-inf") # Base case for leaf node
#
#   LSB, LS = get_max_path_sum(left subtree)
#   RSB, RS = get_max_path_sum(right subtree)
#   MCSB = max(LSB, RSB)
#   MSB = max(MCSB + current node value, current node value)
#   MSR = max(MSB, LSB + current node value + RSB)
#   MPS = max(LS, RS, MSR)
#   return MSB, MPS
###############################

def maxPathSum(tree):
    # Write your code here.
    _, max_sum = get_max_path_sum(tree)
    return max_sum


def get_max_path_sum(node):
    if not node:
        return 0, float("-inf")

    left_max_sum_as_branch, left_max_path_sum = get_max_path_sum(node.left)
    right_max_sum_as_branch, right_max_path_sum = get_max_path_sum(node.right)
    max_child_sum_as_branch = max(left_max_sum_as_branch, right_max_sum_as_branch)

    value = node.value
    max_sum_as_branch = max(max_child_sum_as_branch + value, value)
    max_sum_as_root_node = max(left_max_sum_as_branch + value + right_max_sum_as_branch, max_sum_as_branch)
    max_path_sum = max(left_max_path_sum, right_max_path_sum, max_sum_as_root_node)

    return max_sum_as_branch, max_path_sum

