"""
 Write a function that takes in the head of a Singly Linked List, reverses the list in place (i.e., doesn't create a
 brand-new list), and returns its new head.
 Each LinkedList node has an integer "value" as well as a "next" node pointing to the next node in the list or to
 None/Null if it's the tail of the list.
 You can assume that the input Linked List will always have at least one node; in other words, the head will never be
 None / Null.
"""


# Iterative approach
# Time: O(n) | Space: O(1)
##########################
# We need to maintain 3 pointers - previous node, current node, next node
# Initialize prev_node = None
# Initialize current_node = head
# Loop till current_node is not null
#   Set next_node = current_node.next
#   current_node.next = prev_node
#   prev_node = current_node
#   current_node = next_node
# return prev_node
##########################


class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def reverseLinkedList(head):
    prev_node = None
    current_node = head
    while current_node:
        next_node = current_node.next
        current_node.next = prev_node
        prev_node = current_node
        current_node = next_node
    return prev_node


# Recursive approach
# Time: O(n) | Space: O(1)
##########################
# Declare a function --> reverse(node)
#   If the node is null
#       return node
#   If node.next is null
#       return node
#   recursively call reverse on node.next --> node1 = reverse(node.next)
#   Once the base case (tail) is reached, the function exists and the call goes to the previous node.
#   We have to set the previous.next.next (next pointer of current node) to previous node -> pointer reverses
#   Set previous.next = Null
#   return node1
##########################


class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def reverseLinkedList(head):
    return reverse(head)


def reverse(node):
    if not node:
        return node
    if not node.next:
        return node

    node1 = reverse(node.next)
    node.next.next = node
    node.next = None
    return node1
