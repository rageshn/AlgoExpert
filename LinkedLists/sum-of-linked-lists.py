"""
 You're given two Linked Lists of potentially unequal length. Each Linked List represents a non-negative integer,
 where each node in the Linked List is a digit of that integer, and the first node in each Linked List always represents
 the least significant digit of the integer. Write a function that returns the head of a new Linked List that
 represents the sum of the integers represented by the two input Linked Lists.
 Each LinkedList node has an integer value as well as a next node pointing to the next node in the list or to None / Null
 if it's the tail of the list. The value of each LinkedList node is always in the range of 0 - 9.
 Note: your function must create and return a new Linked List, and you're not allowed to modify either of the input Linked Lists.
"""


# Traversing two linked list in parallel
# Time: O(max(n,m)) | Space: O(max(n,m))
########################################
# Initialize two pointers, one for each linked list. Iterate both pointers in parallel from head till tail.
# Initialize a list which will hold the final linked list values.
# Add the current two values, and the final value is the reminder, and we carry the quotient to the next sum.
# Continue this till we reach the tail of the longest linked list.
# From the final list, create linked list using the values and assign the next pointers
#
# Initialize current_one = head in first linked list
# Initialize current_two = head in second linked list
# Initialize ll = empty list (This holds the node values for final linked list)
# Initialize carry_value & sum_val = 0
# Loop till either current_one or current_two is not null
#   If current_one is not None
#       Set sum_val = current sum_val + current_one value
#   If current_two is not None
#       Set sum_val = current sum_val + current_two value
#   Set sum_val = sum_val + carry_value
#   If sum_val < 10 (No carry)
#       Set current_node_value = sum_val
#       Append current_node_value to ll list
#       Set carry_value = 0
#   else
#       Set current_node_value = sum_val % 10 (Remainder)
#       Append current_node_value to ll list
#       Set carry_value = int(sum_val / 10) (Quotient)
#
#   Set sum_val = 0
#   If current_one is not None
#       Set current_one = current_one.next
#   If current_two is not None
#       Set current_two = current_two.next
# If carry_value > 0 (Sum of tail node - carry should be added as next node)
#   Append carry_value to ll list
#
# Initialize prev_node = None
# Initialize head= None
# Loop through the ll list
#   Create Node object with value at current index
#   If prev_node is notNone
#       Set prev_node.next  = current_node
#   else
#       head = current_node
#   Set prev_node = current_node
# return head
########################################


class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def sumOfLinkedLists(linkedListOne, linkedListTwo):
    current_one = linkedListOne
    current_two = linkedListTwo

    ll = []
    carry_value = 0
    sum_val = 0
    while current_one or current_two:
        if current_one:
            sum_val += current_one.value
        if current_two:
            sum_val += current_two.value
        sum_val += carry_value

        if sum_val < 10:
            current_node_value = sum_val
            ll.append(current_node_value)
            carry_value = 0
        else:
            current_node_value = sum_val % 10
            ll.append(current_node_value)
            carry_value = int(sum_val / 10)

        sum_val = 0
        if current_one:
            current_one = current_one.next
        if current_two:
            current_two = current_two.next

    if carry_value > 0:
        ll.append(carry_value)

    prev_node = None
    head = None
    for index in range(len(ll)):
        current_node = LinkedList(ll[index])
        if prev_node:
            prev_node.next = current_node
        else:
            head = current_node
        prev_node = current_node

    return head


# AlgoExpert Solution
#####################


# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def sumOfLinkedLists(linkedListOne, linkedListTwo):
    result_head_pointer = LinkedList(0)
    current_node = result_head_pointer
    carry = 0

    node_one = linkedListOne
    node_two = linkedListTwo
    while node_one or node_two or carry != 0:
        value_one = node_one.value if node_one else 0
        value_two = node_two.value if node_two else 0
        sum_value = value_one + value_two + carry

        new_value = sum_value % 10
        new_node = LinkedList(new_value)
        current_node.next = new_node
        current_node = new_node

        carry = sum_value // 10
        node_one = node_one.next if node_one else None
        node_two = node_two.next if node_two else None

    return result_head_pointer.next
