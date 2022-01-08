"""
 Write a function that takes in the head of a Singly Linked List and an integer 'k', shifts the list in place
 (i.e., doesn't create a brand-new list) by k positions, and returns its new head.
 Shifting a Linked List means moving its nodes forward or backward and wrapping them around the list where appropriate.
 For example, shifting a Linked List forward by one position would make its tail become the new head of the linked
 list.
 Whether nodes are moved forward or backward is determined by whether 'k' is positive or negative.
 Each LinkedList node has an integer "value" as well as a "next" node pointing to the next node in the list or to
 None/Null if it's the tail of the list.
 You can assume that the input linked list wil always have at least one node; in other words, head will never be
 None / Null.
"""


# Getting the 4 critical nodes from linked list
# Time: O(n) | Space: O(1)
##########################
# In this approach, we get the position of 4 nodes from linked list
#   1. Current head
#   2. Current tail
#   3. New head
#   4. New tail
# With these 4 nodes, we will be able to create the shifted linked list by just updating the next pointers.
# Set New head as New tail's next node
# Update Current tail's next to current head
# Update New tail's next to Null
# Set head = New head
#
# If k == 0 (No need to shift)
#   return head
# Initialize linked list length = 0
# Set current_node = head
# Initialize tail to Null
# Loop till current_node is not Null
#   If current-nodes' next is Null
#       Set tail = current_node
#   Increment linked list length by 1
#   Set current_node = current_node.next
# Set k = k % linked list length (If k is very large, or it's a negative number)
# Set current_node = head
# If k > 0:
#   New tail position = linked list length - k
#   Initialize index = 1
#   Loop till index < new tail position
#       Set current_node = current_node.next
#       Increment index by 1
#   Set new_tail = current_node
#   Set new_head = new_tail.next
#   Set tail.next = head
#   Set new_tail.next = Null
#   Set head = new _head
# return head
##########################


class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def shiftLinkedList(head, k):
    if k == 0:
        return head
    length_linked_list = 0
    current_node = head
    tail = None
    while current_node:
        if current_node.next is None:
            tail = current_node
        length_linked_list += 1
        current_node = current_node.next
    k = k % length_linked_list
    current_node = head
    if k > 0:
        new_tail_position = length_linked_list - k
        index = 1
        while index < new_tail_position:
            current_node = current_node.next
            index += 1
        new_tail = current_node
        new_head = new_tail.next
        tail.next = head
        new_tail.next = None
        head = new_head
    return head
