"""
 Write a function that takes in the head of a Singly Linked List and an integer "k" and removes the kth node from the
 end of the list.
 The removal should be done in place, meaning that the original data structure should be mutated
 (no new structure should be created).
 Furthermore, the input head of the linked list should remain the head of the linked list after the removal is done,
 even if the head is the node that's supposed to be removed. In other words, if the head is the node that's supposed
 to be removed, your function should simply mutate its value and next pointer.
 Note that your function doesn't need to return anything.
 You can assume that the input Linked List will always have at least two nodes and, more specifically, at least k nodes.
 Each LinkedList node has an integer "value" as well as a "next" node pointing to the next node in the list or to
 None/Null if it's the tail of the list.
"""


# Using two pointers
# Time: O(n) | Space: O(1)
##########################
# As it's a singly linked list, we can't traverse backwards.
# Two pointers must be used, which are k length apart from each other. Traverse the LL using two pointers in
# parallel and when the second pointer reaches the tail, its certain that first pointer is k length from the end.
# We can now remove the node at the first pointer.
#
# Initialize prev_node = head
# Initialize to_remove = head
# Initialize kth_node = head
# Initialize i = 1
# Loop till i < k
#   Set kth_node = kth_node.next
#   Increment i by 1
# Loop till kth_node is not Null (Till tail)
#   If kth_node.next is not Null
#       Set prev_node = to_remove (This variable maintains the previous node, to the node to be deleted)
#       Set to_remove = to_remove.next
#       Set kth_node = kth_node.next
#   else (If kth_node is tail)
#       remove the to_remove node from LL --> remove_node_bindings(head, prev_node, to_remove)
#       break
#
# Declare a function --> remove_node_bindings(head, prev_node, node)
#   If prev_node == node (If the node to remove is head)
#       Update head as next node to the node to be removed
#       Set head.value = node.next.value
#       Set head.next = node.next.next
#   else if node.next is Null (If the node to remove is tail)
#       Set prev_node.next = None
#   else (Any other node in LL)
#       If node.next is not Null
#           prev_node.next = node.next
#       Set node.next = Null
##########################


class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def removeKthNodeFromEnd(head, k):
    prev_node = head
    to_remove = head
    kth_node = head
    i = 1
    while i < k:
        kth_node = kth_node.next
        i += 1

    while kth_node:
        if kth_node.next:
            prev_node = to_remove
            to_remove = to_remove.next
            kth_node = kth_node.next
        else:
            remove_node_bindings(head, prev_node, to_remove)
            break


def remove_node_bindings(head, prev_node, node):
    if prev_node == node:
        head.value = node.next.value
        head.next = node.next.next
    elif not node.next:
        prev_node.next = None
    else:
        if node.next:
            prev_node.next = node.next
        node.next = None


# AlgoExpert Solution:
######################

class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def removeKthNodeFromEnd(head, k):
    counter = 1
    first = head
    second = head
    while counter <= k:
        second = second.next
        counter += 1

    if second is None:
        head.value = head.next.value
        head.next = head.next.next
        return
    while second.next is not None:
        second = second.next
        first = first.next
    first.next = first.next.next
