"""
 Write a function that takes in a Binary Search Tree (BST) and a positive integer 'k' and returns the kth largest integer
 contained in the BST.
 You can assume that there will only be integer values in the BST and that 'k' is less than or
 equal to the number of nodes in the tree.
 Also, for the purpose of this question, duplicate integers will be treated as distinct values.
 In other words, the second largest value in a BST containing values {5, 7, 7} will be 7 and not 5.
 Each BST node has an integer value, a left child not and a right child node. A node is said to be a valid BST node
 if and only if it satisfies the BST property: its value is strictly greater than the values of every node to its left;
 its value is less than or equal to the values of every node to its right; and its children node are either valid BST
 nodes themselves or None/NULL
"""


# Reverse Inorder traversal (Recursive approach)
# Time (Average): O(h + k) | Space (Average): O(k)
# Time (worst)  : O(n)     | Space (Worst)  : O(n)
###################################################
# Inorder traversal loops the BST in ascending order, so reverse inorder traversal can be used
# to retrieve the kth largest element as it loops in descending order.
#
# Set top_k_largest = revInOrderTraverse(tree, k, array)
# return top_k_largest[k-1]
#
# Declare a function --> revInOrderTraverse(tree, k, array)
#   If node is not null and length of array is less than k
#       call revInOrderTraverse for right subtree, k, array
#       append current node value to array
#       call revInOrderTraverse for left subtree, k, array
#   return array
###############################


class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def findKthLargestValueInBst(tree, k):
    top_k_largest = revInOrderTraverse(tree, k, [])
    return top_k_largest[k-1]


def revInOrderTraverse(tree, k, array):
    if tree and (len(array) < k):
        revInOrderTraverse(tree.right, k, array)
        array.append(tree.value)
        revInOrderTraverse(tree.left, k, array)
    return array


# AlgoExport Solution
######################

class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


class TreeInfo:
    def __init__(self, nodesVisited, nodeValue):
        self.nodesVisited = nodesVisited
        self.nodeValue = nodeValue


def findKthLargestValueInBst(tree, k):
    treeInfo = TreeInfo(0, -1)
    reverseInOrderTraverse(tree, k, treeInfo)
    return treeInfo.nodeValue


def reverseInOrderTraverse(node, k, treeInfo):
    if node is None or treeInfo.nodesVisited >= k:
        return

    reverseInOrderTraverse(node.right, k, treeInfo)
    if treeInfo.nodesVisited < k:
        treeInfo.nodesVisited += 1
        treeInfo.nodeValue = node.value
        reverseInOrderTraverse(node.left, k, treeInfo)
