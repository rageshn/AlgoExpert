"""
 Write a function that takes in the heads of two Singly Linked Lists that are in sorted order, respectively.
 The function should merge the lists in place (i.e., it shouldn't create a brand new list) and return the head of the
 merged list; the merged list should be in sorted order.
 Each LinkedList node has an integer "value" as well as a "next" node pointing to the next node in the list or to
 None/Null if it's the tail of the list.
 You can assume that the input linked list wil always have at least one node; in other words, head will never be
 None / Null.
"""


# Iterative approach
# Time: O(n + m) | Space: O(1)
##############################
# In this approach, we have to check which value is the least among the two current nodes and create a pointer from
# smallest to largest. This should continue till we reach the tail in any one of the linked list.
#
# Initialize temp as a dummy node
# Set current_node = temp
# Loop till headOne and headTwo is not Null
#   If headOne.value < headTwo.value
#       current_node.next = headOne (set the pointer to the node with the least value)
#       headOne = headOne.next
#   else
#       current_node.next = headTwo
#       headTwo = headTwo.next
#   Set current_node = current_node.next
# If headOne is not Null (headTwo reached tail & headOne still has nodes)
#   Set current_node.next = headOne
#   Set headOne = headOne.next
# If headTwo is not Null (headOne reached tail & headTwo still has nodes)
#   Set current_node.next = headTwo
#   Set headTwo = headTwo.next
# return temp.next
##############################


class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def mergeLinkedLists(headOne, headTwo):
    temp = LinkedList(-1)
    current_node = temp
    while headOne and headTwo:
        if headOne.value < headTwo.value:
            current_node.next = headOne
            headOne = headOne.next
        else:
            current_node.next = headTwo
            headTwo = headTwo.next
        current_node = current_node.next

    if headOne:
        current_node.next = headOne
        headOne = headOne.next
    if headTwo:
        current_node.next = headTwo
        headTwo = headTwo.next
    return temp.next
