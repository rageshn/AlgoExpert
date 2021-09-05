"""
 Write a function that takes in a Binary Tree and returns a list of its branch sums ordered from
 leftmost branch sum to rightmost branch sum.
 A branch sum is the sum of all values in a Binary Tree branch. A Binary Tree branch is a path of nodes in a tree
 that starts at the root node and ends at any leaf node.
 Each Binary Tree node has an integer value, a left child node and a right child node. Children nodes can either be
 Binary Tree node themselves or NULL/None
"""


# Recursive Method
# Time (Average): O(n) | Space (Average): O(h)
# Time (worst)  : O(n) | Space (Worst)  : O(n)
##############################################
# Traverse the Binary Tree in inorder (ordered from left most branch to right most branch)
# Every time we visit a node, we keep track of the sum of all nodes we visited so far in the current_sum variable.
# When we visit a leaf node, we add the current node's value with current_sum and append it to array
#
# Call inorder_traverse(root, [], 0)
#
# Declare a function --> inorder_traverse(node, array, current_sum)
#   If the node is not null
#       Check if the node is a left node (both left and right subtree are none)
#       recursively call inorder_traverse(left subtree, array, current node value + current_sum)
#       if the current node is a leaf node
#           append te sum of current node's value + current_sum to array
#       recursively call inorder_traverse(right subtree, array, current node value + current_sum)
#   return array
##############################################


class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def branchSums(root):
    return inorder_traverse(root, [], 0)


def inorder_traverse(node, array, current_sum):
    if node:
        is_leaf_node = True if (not node.left) and (not node.right) else False
        inorder_traverse(node.left, array, (node.value + current_sum))
        if is_leaf_node:
            array.append(node.value + current_sum)
        inorder_traverse(node.right, array, (node.value + current_sum))
    return array


# AlgoExpert Solution


class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def branchSums(root):
    sums = []
    calculateBranchSums(root, 0, sums)
    return sums


def calculateBranchSums(node, runningSum, sums):
    if node is None:
        return

    newRunningSum = runningSum + node.value
    if node.left is None and node.right is None:
        sums.append(newRunningSum)
        return

    calculateBranchSums(node.left, newRunningSum, sums)
    calculateBranchSums(node.right, newRunningSum, sums)
