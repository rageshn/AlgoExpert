"""
  You're given the root node of a Binary Tree, a target value of a node that's contained in the tree,
  and a positive integer k. Write a function that returns the values of all the nodes that are exactly
  distance k from the node with target value.
  The distance between two nodes is defined as the number of edges that must be traversed to go from
  one node to the other. For example, the distance between a node and its immediate left or right child is 1.
  The same holds in reverse: the distance between a node and its parent is 1. In a tree of three nodes
  where the root node has a left and right child, the left and right children are distance 2 from each other.
  Each Binary Tree node has an integer value, a left child node and a right child node. Children nodes can either be
  Binary Tree node themselves or NULL/None.
  Note that all BinaryTree node values will be unique, and your function can return the output values in any order.
"""


# Using Breadth First Search
# Time: O(n) | Space: O(n)
###########################
# This can be achieved by using BFS from the target node. We have to maintain the level of the nodes we are traversing
# and if the node's level is equal to 'k', we can return the nodes in that level.
#
# First step is to get the parent nodes of all the nodes in the tree
# Declare a function --> get_parent_map(node, parent_node, parent_map)
#   Use any of the tree traversal technique to visit the nodes
#   If the node is not null
#       recursively call get_parent_map on left sub tree by passing current node and dictionary as arguments
#       set the current node as key adn value as its parent node
#       recursively call get_parent_map on right sub tree by passing current node and dictionary as arguments
#   return parent_map
#
# Use the parent map dictionary to get the parent node of the node with target value.
# From the parent node, check the left and right sub tree to get the target node object
# Call bfs function by passing parent map, target node, node level and k as parameters --> bfs(queue, visited, parent_map, node, node_level, k)
#
# Declare a function --> bfs(queue, visited, parent_map, node, node_level, k)
# Append the node value to visited list
# Append the tuple (node, node_level) to queue
# Initialize result as empty list
# while the queue is not empty:
#   Pop the first element from queue as set it to node_to_explore, node_distance
#   If node_distance == k
#       Append the node_to_explore.value to result list
#   If node_to_explore is not null
#       Get the left_node, right_node and parent_node of node_to_explore
#       If the left_node is not null and left_node's value is not in visited
#           Append left_node's value to visited
#           (Increment node_distance, as the left/right/parent node is one level outwards from the current node)
#           Append the tuple (left_node, node_distance+1) to queue.
#       If the right_node is not null and right_node's value is not in visited
#           Append right_node's value to visited
#           Append the tuple (right_node, node_distance+1) to queue
#       If the parent_node is not null and parent_node's value is not in visited
#           Append parent_node's value to visited
#           Append the tuple (parent_node, node_distance+1) to queue
#   return result
###########################


# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def findNodesDistanceK(tree, target, k):
    parent_map = {}
    parent_mapping = get_parent_map(tree, None, parent_map)
    parent_mapping[str(tree.value)] = None

    target_node_parent = parent_mapping[str(target)]
    target_node = None
    if target_node_parent:
        if target_node_parent.left and target_node_parent.left.value == target:
            target_node = target_node_parent.left
        if target_node_parent.right and target_node_parent.right.value == target:
            target_node = target_node_parent.right
    else:
        target_node = tree
    result = bfs([], [], parent_mapping, target_node, 0, k)
    return result


def get_parent_map(node, parent_node, parent_map):
    if node:
        get_parent_map(node.left, node, parent_map)
        parent_map[str(node.value)] = parent_node
        get_parent_map(node.right, node, parent_map)
    return parent_map


def bfs(queue, visited, parent_map, node, node_level, k):
    visited.append(node.value)
    queue.append((node, node_level))
    result = []
    while queue:
        node_to_explore, node_distance = queue.pop(0)
        if node_distance == k:
            result.append(node_to_explore.value)

        if node_to_explore:
            left_node = node_to_explore.left
            right_node = node_to_explore.right
            parent_node = parent_map[str(node_to_explore.value)]

            if left_node and left_node.value not in visited:
                visited.append(left_node.value)
                queue.append((left_node, node_distance + 1))
            if right_node and right_node.value not in visited:
                visited.append(right_node.value)
                queue.append((right_node, node_distance + 1))
            if parent_node and parent_node.value not in visited:
                visited.append(parent_node.value)
                queue.append((parent_node, node_distance + 1))

    return result


# Using Depth First Search
###########################
# Time: O(n) | Space: O(n)
###########################
# Rather than starting at target node, this approach starts at root node and perform a regular DFS.
# This approach doesn't require to find the target node before the process.
# Recursive bases cases are the below:
#   If node = target node
#       Look in the subtree rooted at target node, and find all nodes located at distance K from this node.
#   If the target node is in the left subtree of the current node
#       We must check in the right subtree of the current node that is K - L distance away.
#   If the target node is in the right subtree of the current node
#       We must check in the left subtree of the current node that is K - L distance away.
#   If the target node is not in either left or right subtree of the current node
#       Stop the recursion
#
#          1
#        /   \
#       2      3 (target)
#     /  \       \
#   4     5       6
#               /   \
#              7     8
# Sample logic:
#   dfs(1)
#       left = dfs(2) (-1) --> Unable to find the target node in subtrees under (2)
#       right = dfs(3) (1) --> Target node (3) is 1 [L] distance away from (1).
#                              So we have to find all nodes in the left subtree under (1) that are K - L distance away.
#   dfs(2)
#       left = dfs(4) (-1)
#       right = dfs(5) (-1)
#   dfs(3)
#       right = dfs(6)
#   dfs(6)
#       left = dfs(7)
#       right = dfs(8)


class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def findNodesDistanceK(tree, target, k):
    # Write your code here.
    nodesDistanceK = []
    findDistanceFromNodeToTarget(tree, target, k, nodesDistanceK)
    return nodesDistanceK


def findDistanceFromNodeToTarget(node, target, k, nodesDistanceK):
    if node is None:
        return -1

    if node.value == target:
        addSubtreeNodesAtDistanceK(node, 0, k, nodesDistanceK)
        return 1

    leftDistance = findDistanceFromNodeToTarget(node.left, target, k, nodesDistanceK)
    rightDistance = findDistanceFromNodeToTarget(node.right, target, k, nodesDistanceK)

    if leftDistance == k or rightDistance == k:
        nodesDistanceK.append(node.value)

    if leftDistance != -1:
        addSubtreeNodesAtDistanceK(node.right, leftDistance + 1, k, nodesDistanceK)
        return leftDistance + 1

    if rightDistance != -1:
        addSubtreeNodesAtDistanceK(node.left, rightDistance + 1, k, nodesDistanceK)
        return rightDistance + 1

    return -1


def addSubtreeNodesAtDistanceK(node, distance, k, nodesDistanceK):
    if node is None:
        return

    if distance == k:
        nodesDistanceK.append(node.value)
    else:
        addSubtreeNodesAtDistanceK(node.left, distance + 1, k, nodesDistanceK)
        addSubtreeNodesAtDistanceK(node.right, distance + 1, k, nodesDistanceK)
