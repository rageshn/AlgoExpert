"""
 Write three functions that take in a Binary Search Tree (BST) and an empty
 array, traverse the BST, add its nodes' values to the input array, and return
 that array. The three functions should traverse the BST using the in-order,
 pre-order, and post-order tree-traversal techniques, respectively.
 Each BST node has an integer value, a left child not and a right child node. A node is said to be a valid BST node
 if and only if it satisfies the BST property: its value is strictly greater than the values of every node to its left;
 its value is less than or equal to the values of every node to its right; and its children node are either valid BST
 nodes themselves or None/NULL.
"""


# Recursive method
# Time: O(n) | Space: O(d)
###########################
# Inorder: left subtree -> root -> right subtree
#   If the node is not None
#       Call inOrderTraverse for left subtree & array as parameters
#       append the current node value to array
#       Call inOrderTraverse for right subtree & array as parameters
#   return array
#
# Preorder: root -> left subtree -> right subtree
#   If the node is not None
#       append the current node value to array
#       Call preOrderTraverse for left subtree & array as parameters
#       Call preOrderTraverse for right subtree & array as parameters
#   return array
#
# Postorder: left subtree -> right subtree -> root
#   If the node is not None
#       Call postOrderTraverse for left subtree & array as parameters
#       Call postOrderTraverse for right subtree & array as parameters
#       append the current node value to array
#   return array
###########################


def inOrderTraverse(tree, array):
    # left subtree -> root -> right subtree
    if tree:
        inOrderTraverse(tree.left, array)
        array.append(tree.value)
        inOrderTraverse(tree.right, array)
    return array


def preOrderTraverse(tree, array):
    # root -> left subtree -> right subtree
    if tree:
        array.append(tree.value)
        preOrderTraverse(tree.left, array)
        preOrderTraverse(tree.right, array)
    return array


def postOrderTraverse(tree, array):
    # left subtree -> right subtree -> root
    if tree:
        postOrderTraverse(tree.left, array)
        postOrderTraverse(tree.right, array)
        array.append(tree.value)
    return array
