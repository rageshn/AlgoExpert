"""
 The distance between a node in a Binary Tree and the tree's root is called the node's depth.
 Write a function that takes in a Binary Tree and returns the sum of its nodes' depths.
 Each Binary Tree node has an integer value, a left child node and a right child node. Children nodes can either be
 Binary Tree node themselves or NULL/None
"""


# Recursive Method - Additional space
# Time: O(n) | Space: O(n)
##########################
# This approach gets the current depth of a node and appends it to an array
# Sum of the array is the total node depths
#
# Initialize current_depth to 0
# Initialize tree_depth to empty array
# Call getDepths method on root by passing current_depth and tree_depth --> getDepths(node, current_depth, tree_depth)
# Above method call returns the array of depth of all node
# return the sum of array elements
#
# Declare a function --> getDepths(node, current_depth, tree_depth)
#   If the current node is null
#       Do nothing
#   If the node is not null
#       Append the current_depth to tree_depth
#       recursively call getDepths on left subtree, increment the current_depth by 1 and tree_depth
#       recursively call getDepths on right subtree, increment the current_depth by 1 and tree_depth
#   return tree_depth
##########################


def nodeDepths(root):
    current_depth = 0
    tree_depth = []
    all_depths = getDepths(root, current_depth, tree_depth)
    return sum(all_depths)


def getDepths(node, current_depth, tree_depth):
    if not node:
        return

    if node:
        tree_depth.append(current_depth)
        getDepths(node.left, current_depth + 1, tree_depth)
        getDepths(node.right, current_depth + 1, tree_depth)
    return tree_depth


class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


# Recursive Method - Without using array to save depths
# Time: O(n) | Space: O(h)
##########################
# This approach maintains a global variable to save the depth of the tree, by using the current depth of the node
#
# Call getDepths on root, with current_depth and tree_depth as 0. This returns the total_depth of the tree.
# return the total_depth
#
# Declare a function --> getDepths(node, current_depth, tree_depth)
#   If the node is null
#       return the total_depth
#   If the node is not null
#       Set tree_depth = tree_depth + current_depth
#       Increment current_depth by 1
#       Recursively call getDepths on left subtree with current_depth and tree_depth
#       Recursively call getDepths on right subtree with current_depth and tree_depth
#   return tree_depth
##########################


def nodeDepths(root):
    total_depth = getDepths(root, 0, 0)
    return total_depth


def getDepths(node, current_depth, tree_depth):
    if not node:
        return tree_depth

    if node:
        tree_depth += current_depth
        tree_depth = getDepths(node.left, current_depth + 1, tree_depth)
        tree_depth = getDepths(node.right, current_depth + 1, tree_depth)
    return tree_depth


class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


# Iterative approach - With stack to save
# Time: O(n) | Space: O(h)
###########################
# Initialize sumOfDepths = 0
# Initialize a stack with the node and its depth -> node: root, depth: 0
# While len(stack) > 0:
#   Pop an element from stack -> nodeInfo
#   Get the node and depth from nodeInfo
#   If the node is null
#       continue
#   set sumOfDepths = sumOfDepths + depth
#   append node's left subtree by incrementing depth by 1, and push is to stack
#   append node's right subtree by incrementing depth by 1, and push it to stack
# return sumOfDepths
###########################


def nodeDepths(root):
    sumOfDepths = 0
    stack = [{"node": root, "depth": 0}]
    while len(stack) > 0:
        nodeInfo = stack.pop()
        node, depth = nodeInfo["node"], nodeInfo["depth"]
        if node is None:
            continue
        sumOfDepths += depth
        stack.append({"node": node.left, "depth": depth + 1})
        stack.append({"node": node.right, "depth": depth + 1})
    return sumOfDepths


class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
