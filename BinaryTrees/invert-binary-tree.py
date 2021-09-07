"""
 Write a function that takes in a Binary Tree and inverts it. In other words, the function should swap every left node
 in the tree for its corresponding right node.
 Each Binary Tree node has an integer value, a left child node and a right child node. Children nodes can either be
 Binary Tree node themselves or NULL/None.
"""


# Recursive method
# Time: O(n) | Space: O(h)
##########################
# This problem can be solved by traversing the tree in post order and swapping the left and right subtrees of a node.
#
# call post_order_traverse(root), this returns the inverted tree's root
# return inverted tree's node
#
# Declare a function --> post_order_traverse(node):
#   If the node is not null
#       recursively call post_order_traverse(node's left subtree)
#       recursively call post_order_traverse(node's right subtree)
#       If the node has either left or right node
#           swap the left and right subtree nodes
#   return node
##########################


def invertBinaryTree(tree):
    inverted_tree = post_order_traverse(tree)
    return inverted_tree


def post_order_traverse(node):
    if node:
        post_order_traverse(node.left)
        post_order_traverse(node.right)
        if node.left or node.right:
            temp = node.left
            node.left = node.right
            node.right = temp
    return node


class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


# AlgoExpert Solution (BFS approach)
# Time: O(n) | Space: O(n)
###########################
# Initialize a queue & add root node ot it
# Loop till there are no elements in the queue
#   Get the first element from the queue
#   If the current node is null
#       continue
#   Swap the left and right subtree of current node
#   Append current node's left subtree to queue
#   Append current node's right subtree to queue
###########################


def invertBinaryTree(tree):
    queue = [tree]
    while len(queue):
        current_node = queue.pop(0)
        if not current_node:
            continue
        swapLeftAndRight(current_node)
        queue.append(current_node.left)
        queue.append(current_node.right)


def swapLeftAndRight(node):
    node.left, node.right = node.right, node.left


class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

