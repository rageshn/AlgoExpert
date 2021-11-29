"""
 You're given three inputs, all of which are instances of an AncestralTree class that have an ancestor property
 pointing to their youngest ancestor. The first input is the top ancestor in an ancestral tree
 (i.e., the only instance that has no ancestor--its ancestor property points to None/Null), and the
 other two inputs are descendants in the ancestral tree.
 Write a function that returns the youngest common ancestor to the two descendants.
 Note that a descendant is considered its own ancestor. So in the simple ancestral tree below,
 the youngest common ancestor to nodes A and B is node A.
      A
    /
  B
"""


# Naive approach
# Time: O(depth) | Space: O(depth)
####################################
# Loop through the ancestor nodes till the topAncestor
# Maintain tow lists for first and second descendant nodes
# Iterate through the lists from back (from root to the nodes) till we reach the last common node value
#
# Initialize first_ancestors and second_ancestors to empty list
# Set node = descendantOne
# Loop till the node is not null
#   Append the current node to first_ancestors list   (Leaf to topAncestor)
#   Break the loop if the current node is topAncestor node
#   Set node to node's ancestor
#
# Repeat the same loop with descendantTwo
# Get the minimum length among the tow lists -> min_index
# Reverse the first_ancestors and second_ancestors list (topAncestor to Leaf)
# Initialize common_ancestor to Null
# Iterate the lists from 0 to min_index
#   If the elements in the two list at index are same
#       Set common_ancestor = Current element at index
# return common_ancestor
####################################


class AncestralTree:
    def __init__(self, name):
        self.name = name
        self.ancestor = None


def getYoungestCommonAncestor(topAncestor, descendantOne, descendantTwo):
    first_ancestors = []
    second_ancestors = []

    node = descendantOne
    while node:
        first_ancestors.append(node)
        if node.name == topAncestor.name:
            break
        node = node.ancestor

    node = descendantTwo
    while node:
        second_ancestors.append(node)
        if node.name == topAncestor.name:
            break
        node = node.ancestor

    min_index = min(len(first_ancestors), len(second_ancestors))
    first_ancestors = list(reversed(first_ancestors))
    second_ancestors = list(reversed(second_ancestors))

    common_ancestor = None
    for index in range(0, min_index):
        if first_ancestors[index].name == second_ancestors[index].name:
            common_ancestor = first_ancestors[index]

    return common_ancestor


# Without using additional space
# Time: O(depth) | Space: O(1)
################################
# Get the depths of two descendants from the top ancestor.
# Move the lower descendant upwards to the same level as the other descendant
# Iterate through both node's ancestor nodes till they are equal to each other
#
# Initialize depths of first and second descendants to 0
# Loop the first descendant's ancestral tree till the top ancestor and get the node depth
# Loop the second descendant's ancestral tree till the top ancestor and get the node depth
# If the first descendant depth is greater than second descendant depth
#   Get the depth difference
#   Loop the ancestral tree till the difference becomes 0
#   Now both the nodes are at the same level.
#   Loop the two node's ancestral tree till the two nodes are not equal
#   return any of the descendant node
# else
#   Perform the same operation but with the opposite descendant nodes
################################


class AncestralTree:
    def __init__(self, name):
        self.name = name
        self.ancestor = None


def getYoungestCommonAncestor(topAncestor, descendantOne, descendantTwo):
    descendant_one_depth = 0
    descendant_two_depth = 0

    node = descendantOne
    while node != topAncestor:
        descendant_one_depth += 1
        node = node.ancestor

    node = descendantTwo
    while node != topAncestor:
        descendant_two_depth += 1
        node = node.ancestor

    if descendant_one_depth > descendant_two_depth:
        diff = descendant_one_depth - descendant_two_depth
        while diff > 0:
            descendantOne = descendantOne.ancestor
            diff -= 1

        while descendantOne != descendantTwo:
            descendantOne = descendantOne.ancestor
            descendantTwo = descendantTwo.ancestor
        return descendantOne
    else:
        diff = descendant_two_depth - descendant_one_depth
        while diff > 0:
            descendantTwo = descendantTwo.ancestor
            diff -= 1

        while descendantOne != descendantTwo:
            descendantOne = descendantOne.ancestor
            descendantTwo = descendantTwo.ancestor
        return descendantOne


# Using helper functions
# Time: O(depth) | Space: O(1)
##############################
# Has helper functions to calculate the node depth and backtrack the ancestral tree
##############################


class AncestralTree:
    def __init__(self, name):
        self.name = name
        self.ancestor = None


def getYoungestCommonAncestor(topAncestor, descendantOne, descendantTwo):
    depth_one = get_descendant_depth(descendantOne, topAncestor)
    depth_two = get_descendant_depth(descendantTwo, topAncestor)
    if depth_one > depth_two:
        return backtrack_ancestral_tree(descendantOne, descendantTwo, depth_one - depth_two)
    else:
        return backtrack_ancestral_tree(descendantTwo, descendantOne, depth_two - depth_one)


def get_descendant_depth(descendant, top_ancestor):
    depth = 0
    while descendant != top_ancestor:
        depth += 1
        descendant = descendant.ancestor
    return depth


def backtrack_ancestral_tree(lower_descendant, higher_descendant, diff):
    while diff > 0:
        lower_descendant = lower_descendant.ancestor
        diff -= 1

    while lower_descendant != higher_descendant:
        lower_descendant = lower_descendant.ancestor
        higher_descendant = higher_descendant.ancestor

    return lower_descendant