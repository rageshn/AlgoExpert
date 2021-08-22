"""
 Write a function that takes in a non-empty sorted array of distinct integers, constructs a BST from the integers,
 and returns the root of the BST.
 The function should minimize the height of the BST.
 You've been provided with a BST class that you'll have to use to construct the BST.
 Each BST node has an integer value, a left child not and a right child node. A node is said to be a valid BST node
 if and only if it satisfies the BST property: its value is strictly greater than the values of every node to its left;
 its value is less than or equal to the values of every node to its right; and its children node are either valid BST
 nodes themselves or None/NULL.
"""


# Recursive method
# Time: O(n*log(n)) | Space: O(n)
#################################
# Declare a function --> minHeightBst(array)
#   Initialize start to 0
#   Initialize end to last index in array
#   call addToBST(start, end, array) --> addToBST(start, end, array)
#
# Declare a function --> addToBST(start, end, array)
#   If start > end
#       return null
#   Set mid to (start + end) / 2
#   Set root as a BST node with mid element in array as value
#   Loop the array in binary search approach and add the elements
#   Set root's left node = recursively call addToBST(start, mid-1, array)
#   Set root's right node = recursively call addToBST(mid + 1, end, array)
#   return root
#################################


def minHeightBst(array):
    start = 0
    end = len(array) - 1
    return addToBST(start, end, array)


def addToBST(start, end, array):
    if start > end:
        return None
    mid = int((start + end) / 2)
    root = BST(array[mid])
    root.left = addToBST(start, mid - 1, array)
    root.right = addToBST(mid + 1, end, array)
    return root


class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BST(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BST(value)
            else:
                self.right.insert(value)


# AlgoExpert Solutions
#######################

def minHeightBst(array):
    return constructMinHeightBst(array, None, 0, len(array)-1)


# Approach - 1
def constructMinHeightBst(array, bst, startIndex, endIndex):
    if startIndex > endIndex:
        return
    midIndex = (startIndex + endIndex) // 2
    valueToAdd = array[midIndex]
    if bst is None:
        bst = BST(valueToAdd)
    else:
        bst.insert(valueToAdd)
    constructMinHeightBst(array, bst, startIndex, midIndex-1)
    constructMinHeightBst(array, bst, midIndex+1, endIndex)
    return bst

# Approach - 2
def constructMinHeightBst(array, bst, startIndex, endIndex):
    if endIndex < startIndex:
        return

    midIndex = (startIndex + endIndex) // 2
    newBstNode = BST(array[midIndex])
    if bst is None:
        bst = newBstNode
    else:
        if array[midIndex] < bst.value:
            bst.left = newBstNode
            bst = bst.left
        else:
            bst.right = newBstNode
            bst = bst.right
    constructMinHeightBst(array, bst, startIndex, midIndex - 1)
    constructMinHeightBst(array, bst, midIndex + 1, endIndex)
    return bst

# Approach - 3
def constructMinHeightBst(array, startIndex, endIndex):
    if endIndex < startIndex:
        return None
    
    midIndex = (startIndex + endIndex) // 2
    bst = BST(array[midIndex])
    bst.left = constructMinHeightBst(array, startIndex, midIndex-1)
    bst.right = constructMinHeightBst(array, midIndex + 1, endIndex)
    return bst


class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BST(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BST(value)
            else:
                self.right.insert(value)

