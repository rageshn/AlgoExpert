"""
 Write a function that takes in a Binary Tree (where nodes have an additional pointer to their parent node)
 as well as a node contained in that tree and returns the given node's successor.
 A node's successor is the next node to be visited (immediately after the given node) when traversing its tree
 using the in-order tree-traversal technique. A node has no successor if it's the last node to be visited in the
 in-order traversal.
 If a node has no successor, your function should return None/NULL.
 Each Binary Tree node has an integer value, a left child node and a right child node. Children nodes can either be
 Binary Tree node themselves or NULL/None.
"""


# Naive approach (without using the parent pointer)
# Time: O(n) | Space: O(n)
##########################
# In-order Traversal: Left -> Root -> Right
# This approach traverses the tree in in-order approach and adds it to another array.
# Loops the in-order result array and gets the index of the node to find and returns the next index value.
#
# Set inorder_results = resultant array from inorder traversing the tree. --> inorder_traverse(tree, array)
# Initialize successor_index value to positive infinity
# Loop through the inorder_results
#   If the current element == node to find
#       Set successor_index to next index to current element
# return element at the successor_index
# return NULL when there is no successor_index
#
# Declare a function --> inorder_traverse(node, array)
#   If the node is not null
#       recursively call inorder_traverse on left subtree --> inorder_traverse(node.left, array)
#       append the current node to array
##########################


class BinaryTree:
    def __init__(self, value, left=None, right=None, parent=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent


def findSuccessor(tree, node):
    inorder_results = inorder_traverse(tree, [])
    successor_index = float("inf")
    for index in range(len(inorder_results)):
        if inorder_results[index].value == node.value:
            successor_index = index + 1
            break

    if successor_index <= len(inorder_results) - 1:
        return inorder_results[successor_index]
    return None


def inorder_traverse(node, array):
    if node:
        inorder_traverse(node.left, array)
        array.append(node)
        inorder_traverse(node.right, array)
    return array


# Optimized approach
# Time: O(h) | Space: O(1)
##########################
# In-order Traversal: Left -> Root -> Right
# This approach uses the below basic concepts:
#   1. If the current node has a right subtree, the successor should be the right node's left most child.
#   2. Else, Get the current node's right most parent.
#
# If the current node doesn't have a right subtree (has only left child or leaf node), then the successor will be the
# immediate parent node.
# If the current node is its parent's right node, then the successor will be parent node's parent.
# If the current node is its parent's left node, then the successor will be its parent node.
#
# If the node has a right subtree
#   return the left most child of the node's right subtree --> getLeftmostChild(node)
# Else
#   return the right most parent of the node --> getRightmostParent(node)
#
# Declare a function --> getLeftmostChild(node)
#   Set current_node to node
#   Loop till current_node's left subtree is not null
#       Set current_node = current_node's left node
#   return current_node
#
# Declare a function --> getRightmostParent(node)
#   Set current_node to node
#   Loop till the current_node's parent is not null and current_node is it's parent's right child
#       Set current_node as current_node's parent
#   return current_node's parent
##########################


class BinaryTree:
    def __init__(self, value, left=None, right=None, parent=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent


def findSuccessor(tree, node):
    if node.right:
        return getLeftmostChild(node.right)

    return getRightmostParent(node)


def getLeftmostChild(node):
    current_node = node
    while current_node.left:
        current_node = current_node.left

    return current_node


def getRightmostParent(node):
    current_node = node
    while current_node.parent and current_node.parent.right == current_node:
        current_node = current_node.parent

    return current_node.parent

