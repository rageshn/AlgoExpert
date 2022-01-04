"""
 Write a DoublyLinkedList that has a head and a tail, both of which point to either a linked list Node or Null.
 The class should support:
    1. Setting the head and tail of the linked list.
    2. Inserting nodes before and after other nodes as well as at given positions (the position of the head node is 1).
    3. Removing given nodes and removing nodes with given values.
    4. Searching for nodes with given values.
 Note that the setHead, setTail, insertBefore, insertAfter, insertAtPosition and remove methods all take in actual
 Nodes as input parameters—not integers (except for insertAtPosition, which also takes in an integer representing the
 position); this means that you don't need to create any new Nodes in these methods. The input nodes can be either
 stand-alone nodes or nodes that are already in the linked list. If they're nodes that are already in the linked list,
 the methods will effectively be moving the nodes within the linked list. You won't be told if the input nodes are
 already in the linked list, so your code will have to defensively handle this scenario.
 If you're doing this problem in an untyped language like Python or JavaScript, you may want to look at the various
 function signatures in a typed language like Java or TypeScript to get a better idea of what each input parameter is.
 Each Node has an integer value as well as a prev node and a next node, both of which can point to either another node
 or Null.

 Sample Usage:
 Assume the following linked list has already been created:
 1 <-> 2 <-> 3 <-> 4 <-> 5
 Assume that we also have the following stand-alone nodes:
 3, 3, 6
 setHead(4): 4 <-> 1 <-> 2 <-> 3 <-> 5 // set the existing node with value 4 as the head
 setTail(6): 4 <-> 1 <-> 2 <-> 3 <-> 5 <-> 6 // set the stand-alone node with value 6 as the tail
 insertBefore(6, 3): 4 <-> 1 <-> 2 <-> 5 <-> 3 <-> 6 // move the existing node with value 3 before the existing node with value 6
 insertAfter(6, 3): 4 <-> 1 <-> 2 <-> 5 <-> 3 <-> 6 <-> 3 // insert a stand-alone node with value 3 after the existing node with value 6
 insertAtPosition(1, 3): 3 <-> 4 <-> 1 <-> 2 <-> 5 <-> 3 <-> 6 <-> 3 // insert a stand-alone node with value 3 in position 1
 removeNodesWithValue(3): 4 <-> 1 <-> 2 <-> 5 <-> 6 // remove all nodes with value 3
 remove(2): 4 <-> 1 <-> 5 <-> 6 // remove the existing node with value 2
 containsNodeWithValue(5): true
"""


# Doubly Linked List construction
######################################
# setHead               -> Time: O(1) | Space: O(1)
# setTail               -> Time: O(1) | Space: O(1)
# insertBefore          -> Time: O(1) | Space: O(1)
# insertAfter           -> Time: O(1) | Space: O(1)
# insertAtPosition      -> Time: O(p) | Space: O(1)
# removeNodesWithValue  -> Time: O(n) | Space: O(1)
# remove                -> Time: O(1) | Space: O(1)
# containsNodeWithValue -> Time: O(n) | Space: O(1)
######################################


class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def setHead(self, node):
        if not self.head:
            self.head = node
            self.tail = node
            return
        self.insertBefore(self.head, node)

    def setTail(self, node):
        if not self.tail:
            self.setHead(node)
            return
        self.insertAfter(self.tail, node)

    def insertBefore(self, node, nodeToInsert):
        if nodeToInsert == self.head and nodeToInsert == self.tail:
            return

        self.remove(nodeToInsert)
        nodeToInsert.prev = node.prev
        nodeToInsert.next = node
        if not node.prev:
            self.head = nodeToInsert
        else:
            node.prev.next = nodeToInsert
        node.prev = nodeToInsert

    def insertAfter(self, node, nodeToInsert):
        if nodeToInsert == self.head and nodeToInsert == self.tail:
            return
        self.remove(nodeToInsert)
        nodeToInsert.prev = node
        nodeToInsert.next = node.next
        if not node.next:
            self.tail = nodeToInsert
        else:
            node.next.prev = nodeToInsert

        node.next = nodeToInsert

    def insertAtPosition(self, position, nodeToInsert):
        if position == 1:
            self.setHead(nodeToInsert)
            return

        current = self.head
        index = 1
        while current and index != position:
            current = current.next
            index += 1

        if current:
            self.insertBefore(current, nodeToInsert)
        else:
            self.setTail(nodeToInsert)

    def removeNodesWithValue(self, value):
        current = self.head
        while current:
            to_remove = current
            current = current.next
            if to_remove.value == value:
                self.remove(to_remove)

    def remove(self, node):
        if node == self.head:
            self.head = self.head.next
        if node == self.tail:
            self.tail = self.tail.prev
        self.removeNodeBindings(node)

    def containsNodeWithValue(self, value):
        current = self.head
        while current:
            if current.value == value:
                return True
            current = current.next
        return False

    def removeNodeBindings(self, node):
        if node.prev:
            node.prev.next = node.next
        if node.next:
            node.next.prev = node.prev
        node.next = None
        node.prev = None
