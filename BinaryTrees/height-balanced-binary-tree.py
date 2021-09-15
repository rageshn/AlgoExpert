"""
 You're given the root node of a Binary Tree. Write a function that returns true if this Binary Tree is height balanced
 and false if it isn't.
 A Binary Tree is height balanced if for each node in the tree, the difference between the height of its
 left subtree and the height of its right subtree is at most 1.
 Each Binary Tree node has an integer value, a left child node and a right child node. Children nodes can either be
 Binary Tree node themselves or NULL/None.
"""


# Recursive approach
# Time: O(n) | Space: O(h)
###########################
# This approach recursively traverses every node and checks the balance status and height between its left and right
# subtrees.
# For each node, it returns the balance status in the form of array. 0th index represents whether the
# left and right subtree is balanced or not. 1st index represents the height of the current node from leaf.
#
# If the tree is null, its by default balanced. So we return True.
# Call get_height_balance function with root node --> get_height_balance(node).
# This returns an array as [X, Y]. X -> Balance status (True/False), Y -> Height
# return the 0th index value
#
# Declare a function --> get_height_balance(node)
#   If the node is null
#       return [True, 0] (null nodes are always balanced)
#   recursively call get_height_balance on left subtree -> left_subtree_height_balance
#   recursively call get_height_balance on right subtree -> right_subtree_height_balance
#   Initialize is_balanced = False
#   If balance status for both left and right subtree are True and absolute difference between their heights are <= 1
#       Set is_balanced = True
#   return [is_balanced, maximum height between left and right subtree + 1]
###########################


class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def heightBalancedBinaryTree(tree):
    if not tree:
        return True

    is_tree_balanced = get_height_balance(tree)
    return is_tree_balanced[0]


def get_height_balance(node):
    if not node:
        return [True, 0]

    left_subtree_height_balance = get_height_balance(node.left)
    right_subtree_height_balance = get_height_balance(node.right)

    is_balanced = False
    if (left_subtree_height_balance[0] and right_subtree_height_balance[0]) and (abs(left_subtree_height_balance[1] - right_subtree_height_balance[1]) <= 1):
        is_balanced = True

    return [is_balanced, max(left_subtree_height_balance[1], right_subtree_height_balance[1]) + 1]

