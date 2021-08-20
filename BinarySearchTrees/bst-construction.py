"""
 Write a BST class for a Binary Search Tree. The class should support:
    1. Inserting values with the insert method
    2. Removing values with the remove method; this method should only remove the first instance of a given value.
    3. Searching for values with the contains method
 Note that you can't remove values from a single-node tree. In other words, calling the remove method on a single-node
 tree should simply not do anything.
 Each BST node has an integer value, a left child not and a right child node. A node is said to be a valid BST node
 if and only if it satisfies the BST property: its value is strictly greater than the values of every node to its left;
 its value is less than or equal to the values of every node to its right; and its children node are either valid BST
 nodes themselves or None/NULL.
"""


# Recursive Method
# Time (Average): O(log(n)) | Space (Average): O(n)
# Time (Worst)  : O(n)      | Space (Worst)  : O(n)
####################################################
# Initialize BST Class
# 	Initialize constructor
# 		Initialize value, left, right properties
#
# 	Initialize insert(self, value)
# 		If value < self.value
# 			If left node is null
# 				Set the left node to value
# 			else
# 				Call insert method on left node with value
# 		else
# 			If right node is null
# 				Set the right node to value
# 			else
# 				Call insert method on right node with value
# 		return self
#
# 	Initialize contains(self, value)
# 		If value < self.value
# 			If left node is null
# 				return False
# 			else
# 				call contains method on left node with value
# 		else if value > self.value
# 			If right node is null
# 				return False
# 			else
# 				call contains method on right node with value
# 		else
# 			return True
#
# 	Initialize remove(self, value, parentNode = None)
# 		If value < self.value
# 			If the node is not null
# 				call remove method on left node with value and self as parent
# 		else if value > self.value
# 			If the node is not null
# 				call remove method on right node with value and self as parent
# 		else
# 			If the node has two children (left and right are not null)
# 				Set the node value to minimum node value from right sub tree (or maximum from left sub tree) -> get MinValue()
# 				call remove method on right node with self.value and self as parent
# 			If the node is root (has no parent)
# 				If there is a left node
# 					Set the current node value to left node value
# 					Set the right to current node's left node's right node
# 					Set the left to current node's left node's left node
# 				else if there is right node
# 					Set the current node value to right node value
# 					Set the left to current node's right node's left node
# 					Set the right to current node's right node's right node
# 				else
# 					pass
#           else if current node is parent node's left child
#               Set the parent node's left child to current node's left or right
#           else if current node is parent node's right child
#               Set the parent node's right child to current node's left or right
#       return current node
#
#   Initialize getMinValue(self):
#       If the current node's left child is null
#           return current node value
#       else
#           call getMinValue recursively on the left child
####################################################


class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BST(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BST(value)
            else:
                self.right.insert(value)
        return self

    def contains(self, value):
        if value < self.value:
            if self.left is None:
                return False
            else:
                return self.left.contains(value)
        elif value > self.value:
            if self.right is None:
                return False
            else:
                return self.right.contains(value)
        else:
            return True

    def remove(self, value, parentNode=None):
        if value < self.value:
            if self:
                self.left.remove(value, self)
        elif value > self.value:
            if self:
                self.right.remove(value, self)
        else:
            if self.left and self.right:
                self.value = self.right.getMinValue()
                self.right.remove(self.value, self)
            elif parentNode is None:
                if self.left:
                    self.value = self.left.value
                    self.right = self.left.right
                    self.left = self.left.left
                elif self.right:
                    self.value = self.right.value
                    self.left = self.right.left
                    self.right = self.right.right
                else:
                    pass
            elif parentNode.left == self:
                parentNode.left = self.left if self.left else self.right
            elif parentNode.right == self:
                parentNode.right = self.left if self.left else self.right
        return self

    def getMinValue(self):
        if self.left is None:
            return self.value
        else:
            return self.left.getMinValue()


# Iterative Method
# Time (Average) : O(log(n)) | Space (Average): O(1)
# Time (Worst)   : O(n)      | Space (Worst)  : O(1)
#####################################################
# Initialize BST Class
# 	Initialize constructor
# 		Initialize value, left, right properties
#
# 	Initialize insert(self, value)
#       Set current_node to self
#       Run infinite loop
# 		    If value < current_node.value
# 			    If left node is null
# 				    Set the left node to value
# 			    else
# 				    Set current_node = current_node.left
# 		    else
# 			    If right node is null
# 				    Set the right node to value
# 			    else
# 				    Set current_node = current_node.right
#       return self
#
# 	Initialize contains(self, value)
#       Set current_node to self
#       Run infinite loop
# 		    If value < current_node.value
# 			    Set current_node = current_node.left
# 		    else if value > current_node.value
# 			    Set current_node = current_node.right
# 		    else
# 		        return True
#       return False
#
# 	Initialize remove(self, value, parentNode = None)
#       Set current_node to self
#       Run infinite loop
#     		If value < current_node.value
#     			Set parentNode to current_node
#     			Set current_node to current_node.left
#     		else if value > current_node.value
#     			Set parentNode to current_node
#     			Set current_node to current_node.right
#     		else
#     			If the node has two children (left and right are not null)
#     				Set the current_node value to minimum node value from right sub tree (or maximum from left sub tree) -> get MinValue()
#     				call remove method on current_node's right node with current_node.value and current_node as parent
#     			If the node is root (has no parent)
#     				If there is a left node
#     					Set the current node value to current_node's left node value
#     					Set the current_node's right to current node's left node's right node
#     					Set the current_node's left to current node's left node's left node
#     				else if there is right node
#     					Set the current node value to current_node's right node value
#     					Set the current_node's left to current node's right node's left node
#     					Set the current_node's right to current node's right node's right node
#     				else
#    					pass
#               else if current node is parent node's left child
#                   Set the parent node's left child to current node's left or right
#               else if current node is parent node's right child
#                   Set the parent node's right child to current node's left or right
#       return current node
#
#   Initialize getMinValue(self):
#       Set current_node to self
#       Loop till current_node's left node is not null
#           Set current_node to current_node's left
#       return current_node.value
#####################################################


class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        current_node = self
        while True:
            if value < current_node.value:
                if current_node.left is None:
                    current_node.left = BST(value)
                    break
                else:
                    current_node = current_node.left
            else:
                if current_node.right is None:
                    current_node.right = BST(value)
                    break
                else:
                    current_node = current_node.right

        return self

    def contains(self, value):
        current_node = self
        while current_node:
            if value < current_node.value:
                current_node = current_node.left
            elif value > current_node.value:
                current_node = current_node.right
            else:
                return True

        return False

    def remove(self, value, parent_node=None):
        current_node = self
        while current_node:
            if value < current_node.value:
                parent_node = current_node
                current_node = current_node.left
            elif value > current_node.value:
                parent_node = current_node
                current_node = current_node.right
            else:
                if current_node.left and current_node.right:
                    current_node.value = current_node.right.getMinValue()
                    current_node.right.remove(current_node.value, current_node)
                elif parent_node is None:
                    if current_node.left:
                        current_node.value = current_node.left.value
                        current_node.right = current_node.left.right
                        current_node.left = current_node.left.left
                    elif current_node.right:
                        current_node.value = current_node.right.value
                        current_node.left = current_node.right.left
                        current_node.right = current_node.right.right
                    else:
                        pass
                elif parent_node.left == current_node:
                    parent_node.left = current_node.left if current_node.left else current_node.right
                elif parent_node.right == current_node:
                    parent_node.right = current_node.left if current_node.left else current_node.right
                break

        return self

    def getMinValue(self):
        current_node = self
        while current_node.left:
            current_node = current_node.left
        return current_node.value
