"""
 You're give a Node class that has a name and an optional children nodes. When put together, nodes form
 an acyclic tree-like structure.
 Implement the breadthFirstSearch method in the Node class, which takes in an empty array, traverses the tree using the
 Breadth-First-Search approach (specifically navigating the tree from left to right), stores all the node's names in the
 input array, and returns it.
"""

# Using queue
# Time: O(V + E) | Space: O(V)
############################
# Each node has a name and children nodes
# breadthFirstSearch(self, array)
#   Initialize a queue
#   Add the current node to queue
#   Loop till the queue is not empty
#       Pop the first item from queue and assign it to current_element
#       Append the current_element's name to array
#       Loop through current_element's children -> child
#           Append the child object to queue
#
#   return array
############################


class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self

    def breadthFirstSearch(self, array):
        queue = []
        queue.append(self)

        while queue:
            current_element = queue.pop(0)
            array.append(current_element.name)
            for child in current_element.children:
                queue.append(child)
        return array
