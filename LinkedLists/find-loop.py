"""
 Write a function that takes in the head of a Singly Linked List that contains a loop (in other words, the list's tail
 node points to some node in the list instead of None/Null). The function should return the node (the actual node--not
 just its value) from which the loop originates in constant space.
 Each LinkedList node has an integer "value" as well as a "next" node pointing to the next node in the list or to
 None/Null if it's the tail of the list.
 Sample Input:
 head  =  0 -> 1 -> 2 -> 3 -> 4 -> 5 -> 6
                              ^         v
                              9 <- 8 <- 7

 Sample Output:
              4 -> 5 -> 6 // node with value 4
              ^         v
              9 <- 8 <- 7
"""


# Using two points which traverses at two different speeds
# Time: O(n) | Space: O(1)
##########################
# We use two pointers first & second. Both start traversing from head node. First pointer iterate by the step of 1
# and second pointer iterate by the step by 2. We have to iterate till the two pointers meet.
# Assume the distance from head till the node which starts the loop is 'D' => distance from 0 to 4 (0->1->2->3->4).
# Assume the distance between the node which starts the loop and the node at which the both pointers meet is 'P'.
# E.g., If the first & second nodes meet at '7', then P = distance from 4 to 7 (4->5->6->7)
# When they meet, the total distance travelled by first node = D + P (0->1->2->3->4->5->6->7), and the
# total distance travelled by second node is 2D + 2P (step = 2 i.e., it iterates twice the speed as first node).
# Assume the remaining distance that needs to be travelled by two nodes to reach the node which forms the loop as
# 'R' => distance from 7 to 4 (7->8->9->4).
# If P = distance from 4 to 7, then the distance travelled by second node from head, form a loop around the nodes
# and reach the node which forms the loop (1->2->3->4->5->6->7->8->9->4) 'T' => 2D + 2P - P => 2D + P
# From the variables, we can derive that R = T - (D + P) = 2D - P - D - P = D. This is equal to the distance from head
# till the node which forms the loop.
# As we don't know the exact distance of R, we can derive it as the distance covered by first pointer till it reaches the
# node which forms the loop. So we again set the first pointer to head. Then we traverse both first node (head)
# and second node by step of 1. So, they both meet at node 4.
#
# Set first = head.next
# Set second = head.next.next (step = 2)
# Loop till first is not equal to second
#   Set first = first.next
#   Set second = second.next.next
# Set first = head
# Loop till first is not equal to second
#   Set first = first.next
#   Set second = second.next
# return first
##########################


class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def findLoop(head):
    first = head.next
    second = head.next.next
    while first != second:
        first = first.next
        second = second.next.next
    first = head
    while first != second:
        first = first.next
        second = second.next
    return first
