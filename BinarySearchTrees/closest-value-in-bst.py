"""
 Write a function that takes in a Binary Search Tree (BST) and a target integer value and returns the closest value
 to that target value contained in the BST.
 You can assume that there will only be one closest value.
 Each BST node has an integer value, a left child not and a right child node. A node is said to be a valid BST node
 if and only if it satisfies the BST property: its value is strictly greater than the values of every node to its left;
 its value is less than or equal to the values of every node to its right; and its children node are either valid BST
 nodes themselves or None/NULL.
"""


# Recursive method
# Time (Average): O(log(n)) | Space (Average): O(log(n))
# Time (Worst)  : O(n)      | Space (Worst)  : O(n)
#########################################################
# Initialize closest_node = positive infinity
# return traverseTree(tree, target, closest)
#
# Declare a function --> traverseTree(node, target, closest_node)
#   If node is not null
#       Get the absolute difference between target and current node value -> abs_diff
#       If abs_diff = 0,
#           return the node value -> We reached the same number
#       If abs_diff < absolute difference between target and closest
#           Set closest_node = current node value
#       If the current node value > target
#           traverse the left tree --> traverseTree(node.left, target, closest_node)
#       else
#           traverse the right tree --> traverseTree(node.right, target, closest_node)
#   else
#       return closest_node
#########################################################

def findClosestValueInBst(tree, target):
    closest = float("inf")
    return traverseTree(tree, target, closest)


def traverseTree(node, target, closest_node):
    if node:
        abs_diff = abs(target - node.value)
        if abs_diff == 0:
            return node.value
        if abs_diff < abs(target - closest_node):
            closest_node = node.value
        if target < node.value:
            return traverseTree(node.left, target, closest_node)
        else:
            return traverseTree(node.right, target, closest_node)
    else:
        return closest_node


# Iterative Method
# Time (Average): O(log(n)) | Space (Average): O(log(n))
# Time (Worst)  : O(n)      | Space (Worst)  : O(1)
#########################################################
# Initialize closest_node = positive infinity
# return traverseTree(tree, target, closest)
#
# Declare a function --> traverseTree(node, target, closest_node)
#   Set current_node to current node
#   Loop till current_node is not null
#       Get the absolute difference between target value and current_node value -> abs_diff
#       If abs_diff < absolute difference between target and closest_node
#           Set closest_node to current node value
#       If target < current node value
#           Set current_node = current_node.left
#       If target > current node value
#           Set current_node = current_node.right
#       else
#           break the loop
#   return closest_node
#########################################################


def findClosestValueInBst(tree, target):
    closest_node = float("inf")
    return traverseTree(tree, target, closest_node)


def traverseTree(node, target, closest_node):
    current_node = node
    while current_node:
        abs_diff = abs(target - current_node.value)
        if abs_diff < abs(target - closest_node):
            closest_node = current_node.value
        if target < current_node.value:
            current_node = current_node.left
        elif target > current_node.value:
            current_node = current_node.right
        else:
            break
    return closest_node


# This is the class of the input tree.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
