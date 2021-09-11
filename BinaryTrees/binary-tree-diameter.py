"""
 Write a function that takes in a Binary Tree and returns its diameter. The diameter of a binary tree is defined as
 the length of its longest path, even if that path doesn't pass through the root of the tree.
 A path is a collection of connected nodes in a tree, where no node is connected to more than two other nodes.
 The length of a path is the number of edges between the path's first node and its last node.
 Each Binary Tree node has an integer value, a left child node and a right child node. Children nodes can either be
 Binary Tree node themselves or NULL/None.
"""


# Recursive method
# Time (Average): O(n) | Space (Average): O(h)
# Time (Worst)  : O(n) | Space (Worst)  : O(n)
###############################################
# This can be achieved by calculating the longest path from both left and right subtree and return the diameter
# and current height from leaf till the current node for every node.
#
# If the tree node is null, i.e., empty tree
#   return 0
# traverse the nodes recursively and get the final diameter and height of the tree --> traverse_nodes(node)
# return the diameter
#
# Declare a function --> traverse_nodes(node)
#   This method recursively traverses the left and right subtree and calculates the diameter and height w.r.t to
#   the current node.
#   We maintain two values for each node [X, Y] -> X denotes the diameter of the left and right subtree along with
#   current node and Y denotes the height from leaf node till the current node
#
#   If the node is null
#       return [0, 0]
#   Recursively traverse left subtree --> left
#   Recursively traverse right subtree --> right
#   Set the longest path as sum of heights from left and right subtree
#   Set max diameter as max of left and right subtree's diameter
#   Set current diameter as max of longest path and max diameter
#   Set current height as max of left and right subtree's heights + 1
#   return [current diameter, current height]
###############################################


class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def binaryTreeDiameter(tree):
    if not tree:
        return 0
    final_value = traverse_nodes(tree)
    diameter = final_value[0]
    return diameter


def traverse_nodes(node):
    if not node:
        return [0, 0]

    left = traverse_nodes(node.left)
    right = traverse_nodes(node.right)

    longest_path = left[1] + right[1]
    max_diameter = max(left[0], right[0])
    current_diameter = max(longest_path, max_diameter)
    current_height = max(left[1], right[1]) + 1

    return [current_diameter, current_height]
