"""
 You're give a Node class that has a name and an optional children nodes. When put together, nodes form
 an acyclic tree-like structure.
 Implement the depthFirstSearch method in the Node class, which takes in an empty array, traverses the tree using the
 Depth-first Search approach (specifically navigating the tree from left to right),
 stores all of the nodes' names in the input array, and returns it.
"""


# Recursive algorithm
##############################
# Time: O(V + E) | Space: O(V)
##############################
# Each node has a name and children nodes
# depthFirstSearch(self, array)
#   Append the node's name to array
#   Loop through each child node
#       recursively call depthFirstSearch method on each child node
#   return array


class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self

    def depthFirstSearch(self, array):
        array.append(self.name)
        for child in self.children:
            child.depthFirstSearch(array)
        return array
