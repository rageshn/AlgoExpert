"""
 You're given the head of a Singly Linked List whose nodes are in sorted order with respect to their values.
 Write a function that returns a modified version of the Linked List that doesn't contain any nodes with duplicate values.
 The Linked List should be modified in place (i.e., you shouldn't create a brand new list), and the modified
 Linked List should still have its nodes sorted with respect to their values.
 Each LinkedList node has an integer "value" as well as a "next" node pointing to the next node in the list or to
 None/Null if it's the tail of the list.
"""

# Iterative approach
# Time: O(n) | Space: O(1)
###########################
# Set current_node = linkedList
# Loop till current_node is not Null
#   Set next_node = current_node.next
#   Loop till next_node is not Null and next_node.value == current_node.value
#       Set next_node = next_node.next
#   Set current_node.next = next_node
#   Set current_node = next_node
# return linkedList
###########################


class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def removeDuplicatesFromLinkedList(linkedList):
    current_node = linkedList
    while current_node:
        next_node = current_node.next
        while next_node and next_node.value == current_node.value:
            next_node = next_node.next

        current_node.next = next_node
        current_node = next_node
    return linkedList

