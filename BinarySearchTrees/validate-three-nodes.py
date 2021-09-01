"""
 You're given three nodes that are contained in the same Binary Search Tree: nodeOne, nodeTwo, nodeThree.
 Write a function that returns a boolean representing whether one of nodeOne or nodeThree is an ancestor of nodeTwo
 and the other node is the descendant of nodeTwo. For example, if your function determines that nodeOne is an ancestor
 of nodeTwo, then it needs to see if nodeThree is an descendant of nodeTwo. If your function determines that nodeThree
 is an ancestor, then it needs to see if nodeOne is a descendant.
 A descendant of a node N is defined as a node contained in the tree rooted at N. A node N is an ancestor od another
 node M if M is a descendant of N.
 It isn't guaranteed that nodeOne or nodeThree will be ancestors or descendants of nodeTwo, but it is guaranteed that
 all three nodes will be unique and will never be NULL. In other words, you'll be given valid input nodes.
 Each BST node has an integer value, a left child not and a right child node. A node is said to be a valid BST node
 if and only if it satisfies the BST property: its value is strictly greater than the values of every node to its left;
 its value is less than or equal to the values of every node to its right; and its children node are either valid BST
 nodes themselves or None/NULL.
"""


# Iterative method
# Time (Average): O(log(n)) | Space (Average): O(1)
# Time (Worst)  : O(n)      | Space (Worst)  : O(1)
###############################################
# The traversal can be either nodeOne --> nodeTwo --> nodeThree (or) nodeThree --> nodeTwo --> nodeOne
# Validate whether a path exists as nodeOne -> nodeTwo -> nodeThree
# Set one_to_three = call visit_nodes(nodeOne, nodeThree, nodeTwo, False, False)
# If one_to_three is true
#   return True
# else
#   Validate whether a path exists as nodeThree -> nodeTwo -> nodeOne
#   Set three_to_one = call visit_nodes(nodeThree, nodeOne, nodeTwo, False, False)
#   return one_to_three or three_to_one
#
# Declare a function --> visit_nodes(parent, child, nodeTwo, is_node_two_visited, is_parent_to_child_visited)
#   This function check whether a path exists from parent to child and also checks whether it passes through nodeTwo.
#   Set current_node to parent
#   Run infinite loop
#       If current_node is not null
#           If the current_node's value equals nodeTwo.value
#               Set is_node_two_visited to True
#           If current_node's value is less than child node's value
#               Set current_node to current_node's right node
#           Else if current_node's value is greater than child node's value
#               Set current_node to current_node's left node
#           Else if current_node's value is equal to child node's value
#               Set is_parent_to_child_visited to True
#               break out of infinite loop
#       else
#           break
#   return is_node_two_visited and is_parent_to_child_visited
###############################################


class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def validateThreeNodes(nodeOne, nodeTwo, nodeThree):
    one_to_three = visit_nodes(nodeOne, nodeThree, nodeTwo, False, False)
    if not one_to_three:
        three_to_one = visit_nodes(nodeThree, nodeOne, nodeTwo, False, False)
        return one_to_three or three_to_one
    return one_to_three


def visit_nodes(parent, child, nodeTwo, is_node_two_visited, is_parent_to_child_visited):
    current_node = parent
    while True:
        if current_node:
            if current_node.value == nodeTwo.value:
                is_node_two_visited = True

            if current_node.value < child.value:
                current_node = current_node.right
                continue
            elif current_node.value > child.value:
                current_node = current_node.left
                continue
            elif current_node.value == child.value:
                is_parent_to_child_visited = True
                break
        else:
            break
    return is_node_two_visited and is_parent_to_child_visited


# AlgoExpert Solution


class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def validateThreeNodes(nodeOne, nodeTwo, nodeThree):
    searchOne = nodeOne
    searchTwo = nodeThree

    while True:
        foundThreeFromOne = searchOne is nodeThree
        foundOneFromThree = searchTwo is nodeOne
        foundNodeTwo = searchOne is nodeTwo or searchTwo is nodeTwo
        finishedSearching = searchOne is None and searchTwo is None

        if foundThreeFromOne or foundOneFromThree or foundNodeTwo or finishedSearching:
            break

        if searchOne:
            searchOne = searchOne.left if searchOne.value > nodeTwo.value else searchOne.right

        if searchTwo:
            searchTwo = searchTwo.left if searchTwo.value > nodeTwo.value else searchTwo.right

        foundNodeFromOther = searchOne is nodeThree or searchTwo is nodeOne
        foundNodeTwo = searchOne is nodeTwo or searchTwo is nodeTwo
        if not foundNodeTwo or foundNodeFromOther:
            return False

        return searchForTarget(nodeTwo, nodeThree if searchOne is nodeTwo else nodeOne)


def searchForTarget(node, target):
    while node is not None and node is not target:
        node = node.left if target.value < node.value else node.right

    return node is target
